from src.model1 import *
from src.Time_Bound_Calucation import Calculate_Time_Bound
import numpy as np
import random
from z3 import *
from src.parser import check_Linearizability
import time
import re
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
def Linearizability_Verifi(Formula,Num,dts_file_location,method):
        start1 = time.time()
        # Planning problem as DTS
        Data = read_text_file(dts_file_location)
        Data = remove_spaces(Data)
        Data = Data.split(';')
        N = int(Data[0].split(':')[1])# Grid size, No. of states = N*N

        #nObs = 40 # No. of obstacles
        S = ['s_'+str(i)+'_'+str(j) for i in range(N) for j in range(N)]
        A = ['U', 'D', 'L', 'R']
        Inter = []
        for i in Data[5].split(':')[1].split(','):
            Inter.append(i)
        obs = []
        for i in Data[2].split(':')[1].split(','):
            obs.append(i)
        start_states = []
        for i in Data[1].split(':')[1].split(','):
            start_states.append(i)
        goals = []
        for i in Data[3].split(':')[1].split(','):
            goals.append(i)
        print("start : " + str(start_states))
        print("goals : " + str(goals))
        print("obs : " + str(obs))
        # Generating labels
        L = {}
        for s in S:
            _,i,j = s.split('_')
            L[s] = []
            if s in obs:
                L[s].append('X')
            if s in start_states:
                L[s].append('Ss')
            if s in goals:
                L[s].append('G')
            if s in Inter:
                L[s].append('I')
            L[s].append('O'+str(i))

        # Transition function
        def Tran(s,a):
            _,i,j = s.split('_')
            i = int(i)
            j = int(j)
            if a == 'D':
                i_ = i-1
                j_ = j
            if a =='U':
                i_ = i+1
                j_ = j
            if a == 'R':
                i_ = i
                j_ = j+1
            if a == 'L':
                i_ = i
                j_ = j-1
            s_ = 's_'+str(i_)+'_'+str(j_)
            if s_ in S and s_ not in obs and s not in obs:
                return s_
            else:
                return []

        # Generate CDTS from planning
        cdts = CDTS(S, A, Tran, L)
        #cdts.plot()

        # DTS from CDTS
        dts = DTS(cdts)
        # T=20

        check_Linearizability(Formula)
        # Define the pattern to match the numbers in square brackets
        pattern = r'\[(\d+),(\d+)\]'

        # Find all matches of the pattern in the cleaned formula
        matches = re.findall(pattern, Formula)

        # Extract the second numbers from each match
        Times = [int(match[1]) for match in matches]
        sum = 0
        for i in range(0, len(Times)):
            sum = sum + Times[i]
            Times[i] = sum
        print("Times:", Times)
        T=Times[-1]

        T=15
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
        # Generating z3 variables
        # Path 1 - state and label variables and constraints
        S1 = IntVector("s1", T)
        l1 = [[Bool("l1_%i_%i" % (t, labelToNum[l])) for l in labels] for t in range(T)]
        # Path 2 - state and label variables and constraints
        S2 = IntVector("s2", T)
        l2 = [[Bool("l2_%i_%i" % (t, labelToNum[l])) for l in labels] for t in range(T)]

        # z3 solver
        solver = Solver()
        negated_formula=And(
          [S1[t] >= 0 for t in range(T)] + [S1[t] < n for t in range(T)]  # Legal states in path1
                + [Implies(S1[t] == stateToNum[s], Or([S1[t + 1] == stateToNum[x] for x in trans[s]])) for t in
                   range(T - 1) for s in trans.keys()]  # Path1 transitions
                + [Implies(S1[t] == stateToNum[s],
                           And([l1[t][labelToNum[l]] if l in dts_labels[s] else Not(l1[t][labelToNum[l]]) for l in
                                labels])) for t in range(T) for s in states]  # Path1 state to labels
                + [S2[t] >= 0 for t in range(T)] + [S2[t] < n for t in range(T)]  # Legal states in path2
                + [Implies(S2[t] == stateToNum[s], Or([S2[t + 1] == stateToNum[x] for x in trans[s]])) for t in
                   range(T - 1) for s in trans.keys()]  # Path2 transitions
                + [Implies(S2[t] == stateToNum[s],
                           And([l2[t][labelToNum[l]] if l in dts_labels[s] else Not(l2[t][labelToNum[l]]) for l in
                                labels])) for t in range(T) for s in states]  # Path2 state to labels
                + [Or([S1[0] == stateToNum[s] for s in states if 'Ss' in dts_labels[s]])]
                + [Or([S2[0] == stateToNum[s] for s in states if 'Ss' in dts_labels[s]])]
                + [l2[0][labelToNum['Ss']]]
                + [l1[0][labelToNum['Ss']]]
                + [Or([l1[t][labelToNum['I']] for t in range(Times[1])])]
                + [Or([l2[t][labelToNum['I']] for t in range(Times[1])])]
                + Not(S1[0] == S2[0]),  # Negate equality constraint
                + Not(Or([l1[t][labelToNum['G']] for t in range(T)])),  # Negate OR condition
                + Not(Or([l2[t][labelToNum['G']] for t in range(T)])),  # Negate OR condition
                + ForAll(
                        [l1[t_][labelToNum['G']] for t_ in range(T)],  # Negate existential to universal quantifier
                        Exists(
                            [S2[t] for t in range(T)],  # Negate existential to universal quantifier
                            Not(Implies(
                                And([l1[t][labelToNum[l]] == l2[t][labelToNum[l]] for t in range(T) for l in ['U', 'R', 'D', 'L']]),
                                Or([l2[t][labelToNum['G']] for t in range(T)])
                            ))
                        )
                    )

            )
        """# Linearizability constraints
    # Ensure traces occupy the same states within the given mission time
    And([S1[t] == S2[t] for t in range(T)]),
    # Ensure the mission's primary goal is not violated
    Or(
        And(l1[2][labelToNum['I']], l1[3][labelToNum['G']]),  # R2 followed by R4
        And(l1[3][labelToNum['I']], l1[4][labelToNum['G']]),  # R3 followed by R5
    ),
    Or(
        And(l2[2][labelToNum['I']], l2[3][labelToNum['G']]),  # R2 followed by R4
        And(l2[3][labelToNum['I']], l2[4][labelToNum['G']]),  # R3 followed by R5
    )"""
        end1 = time.time()
        solver.add(negated_formula)
        start = time.time()
        res = solver.check()
        end = time.time()
        print("Linearizability solved in " + str(end - start) + " sec")
        print(" First order logic formula generated in " + str(end1 - start1) + " sec")
        print("Total Time:" + str(end1 - start1 + end - start))
        if str(res) == "sat":
            print("The negated formula is not satisfiable.")
        else:
            print("The negated formula is satisfiable.")



