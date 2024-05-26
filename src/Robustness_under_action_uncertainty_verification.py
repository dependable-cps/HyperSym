#!/usr/bin/python3

from src.model1 import *
import numpy as np
import random
from z3 import *
import time
import re
from src.Time_Bound_Calucation import Calculate_Time_Bound

# Transition function
def read_text_file(file_path):
    Data=""
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                Data=Data+line.strip()
            return Data
    except FileNotFoundError:
        print("File not found at the given location.")
    except Exception as e:
        print("An error occurred:", e)
def remove_spaces(input_string):
    return input_string.replace(" ", "")
def robustness_U_A_U_V(Formula,Num,dts_file_location,method):
    # Planning problem as DTS
    Data=read_text_file(dts_file_location)
    Data=remove_spaces(Data)
    Data=Data.split(';')
    N = int(Data[0].split(':')[1])  # Grid size, No. of states = N*N
    Inter = []
    for i in Data[5].split(':')[1].split(','):
        Inter.append(i)
    # nObs = 40 # No. of obstacles
    S = ['s_' + str(i) + '_' + str(j) for i in range(N) for j in range(N)]
    A = ['U', 'D', 'L', 'R']
    obs = []
    for i in Data[2].split(':')[1].split(','):
        obs.append(i)
    start_states = []
    for i in Data[1].split(':')[1].split(','):
        start_states.append(i)
    goals = []
    for i in Data[3].split(':')[1].split(','):
        goals.append(i)
    print("start : "+ str(start_states))
    print("goals : "+str(goals))
    print("obs : " + str(obs))
    print("Inter: "+ str(Inter))
    # Generating labels
    L = {}
    for s in S:
        _, i, j = s.split('_')
        L[s] = []
        if s in obs:
            L[s].append('X')
        if s in start_states:
            L[s].append('S')
        if s in goals:
            L[s].append('G')
        if s in Inter:
            L[s].append('I')

    for s in S:
        _, i, j = s.split('_')
        if s in obs:
            s_ = 's_' + str(int(i) + 1) + '_' + j
            if s_ in S:
                L[s_].append('NX')
            s_ = 's_' + str(int(i) - 1) + '_' + j
            if s_ in S:
                L[s_].append('NX')
            s_ = 's_' + i + '_' + str(int(j) + 1)
            if s_ in S:
                L[s_].append('NX')
            s_ = 's_' + i + '_' + str(int(j) - 1)
            if s_ in S:
                L[s_].append('NX')

    def Tran(s, a):
        _, i, j = s.split('_')
        i = int(i)
        j = int(j)
        if a == 'D':
            i_ = i - 1
            j_ = j
        if a == 'U':
            i_ = i + 1
            j_ = j
        if a == 'R':
            i_ = i
            j_ = j + 1
        if a == 'L':
            i_ = i
            j_ = j - 1
        s_ = 's_' + str(i_) + '_' + str(j_)
        if s_ in S:
            return s_
        else:
            return []
    # Generate CDTS from planning
    cdts = CDTS(S, A, Tran, L)
    # cdts.plot()

    # DTS from CDTS
    dts = DTS(cdts)
    # robustness under action uncertanity

    # Define the pattern to match the common part at the end of the formula
    pattern = r'& \[H\^\d+ A_V1 != H\^\d+ A_V2\] -> \[H\^\d+ A_V1 = H\^\d+ A_V2\]\[\d+,\d+\]$'

    # Remove the common part using regular expression substitution
    cleaned_formula = re.sub(pattern, '', Formula)
    cleaned_formula = cleaned_formula.split(".")[1]
    #print("Cleaned Formula:", cleaned_formula)

    # Bound on path length
    T = Calculate_Time_Bound(cleaned_formula)
    #T=20

    # Define the pattern to match the numbers in square brackets
    pattern = r'\[(\d+),(\d+)\]'

    # Find all matches of the pattern in the cleaned formula
    matches = re.findall(pattern, cleaned_formula[1:-1])

    # Extract the second numbers from each match
    Times = [int(match[1]) for match in matches]
    sum = 0
    for i in range(0, len(Times)):
        sum = sum + Times[i]
        Times[i] = sum
    print("Times:", Times)

    # Mapping states and labels to numbers
    stateToNum = {}
    numToState = {}
    states = dts.getStates()
    n = len(states)
    i = 0
    for s in states:
        stateToNum[s] = i
        numToState[i] = s
        i += 1
    labelToNum = {}
    numToLabel = {}
    labels = []
    dts_labels = dts.getLabels()
    for s in states:
        for l in dts_labels[s]:
            if l not in labels:
                labels.append(l)
    i = 0
    for l in labels:
        labelToNum[l] = i
        numToLabel[i] = l
        i += 1
    trans = dts.getTrans()

    next_obs = []
    # Generating z3 variables
    # Path 1 - state and label variables and constraints
    S1 = IntVector("s1", T)
    l1 = [[Bool("l1_%i_%i" % (t, labelToNum[l])) for l in labels] for t in range(T)]
    # Path 2 - state and label variables and constraints
    S2 = IntVector("s2", T)
    l2 = [[Bool("l2_%i_%i" % (t, labelToNum[l])) for l in labels] for t in range(T)]

    # z3 solver
    solver = Solver()
    solver.push()
    solver.add(
        And(
            [S1[t] >= 0 for t in range(T)] + [S1[t] < n for t in range(T)]  # Legal states in path1
            + [Implies(S1[t] == stateToNum[s], Or([S1[t + 1] == stateToNum[x] for x in trans[s]])) for t in range(T - 1)
               for s in trans.keys()]  # Path1 transitions
            + [Implies(S1[t] == stateToNum[s],
                       And([l1[t][labelToNum[l]] if l in dts_labels[s] else Not(l1[t][labelToNum[l]]) for l in labels]))
               for t in range(T) for s in states]  # Path1 state to labels
            + [S2[t] >= 0 for t in range(T)] + [S2[t] < n for t in range(T)]  # Legal states in path2
            + [Implies(S2[t] == stateToNum[s], Or([S2[t + 1] == stateToNum[x] for x in trans[s]])) for t in range(T - 1)
               for s in trans.keys()]  # Path2 transitions
            + [Implies(S2[t] == stateToNum[s],
                       And([l2[t][labelToNum[l]] if l in dts_labels[s] else Not(l2[t][labelToNum[l]]) for l in labels]))
               for t in range(T) for s in states]  # Path2 state to labels
            + [l1[0][labelToNum['S']]]
            + [l2[0][labelToNum['S']]]
            + [Or([l1[t][labelToNum['I']] for t in range(Times[1])])]
            + [Or([l2[t][labelToNum['I']] for t in range(Times[1])])]
            + [Or([l1[t][labelToNum['G']] for t in range(T)])]
            + [Or([l2[t][labelToNum['G']] for t in range(T)])]
            + [S1[t] != stateToNum[s] for t in range(T) for s in states if 'NX' in dts_labels[s]]
            + [S2[t] != stateToNum[s] for t in range(T) for s in states if 'NX' in dts_labels[s]]
            + [Not(Or([l1[t][labelToNum['X']] for t in range(T)]))]
            + [Not(Or([l2[t][labelToNum['X']] for t in range(T)]))]
            + [Or([l1[t][labelToNum[l]] != l2[t][labelToNum[l]] for t in range(T) for l in ['U', 'R', 'L', 'D']])]
            + [Implies(
                Or([l1[t][labelToNum[l]] != l2[t][labelToNum[l]] for l in ['U', 'R', 'L', 'D']]),
                And([Not(l2[t][labelToNum['G']])] + [Not(l1[t][labelToNum['G']])] + [
                    l1[t_][labelToNum[l]] == l2[t_][labelToNum[l]] for l in ['U', 'R', 'L', 'D'] for t_ in
                    range(t + 1, T)])
                # And([l1[t_][labelToNum[l]] == l2[t_][labelToNum[l]] for l in ['U', 'R', 'L', 'D'] for t_ in range(t+1,T)])

            ) for t in range(T)]
            + [ForAll(
                [S2[t] for t in range(T)],
                # [Or([l2[t][labelToNum['G']] for t in range(T)])]
                [Implies(
                    Or([l1[t][labelToNum[l]] != l2[t][labelToNum[l]] for l in ['U', 'R', 'L', 'D']]),
                    Or([l2[t_][labelToNum['G']] for t_ in range(t + 1, T)])

                ) for t in range(T)]

            )]
        )
    )

    start = time.time()
    res = solver.check()
    if(method=="verification"):
        print("Result : "+str(res))
        sys.exit()
    end = time.time()
    print(" Action robustness solved in " + str(end - start) + " sec")
    print("result of verification : "+str(res))



