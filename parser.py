import re
import sys

def check_robustness_U_A_U(Formula):
    pattern = r'& \[H\^\d+ A_V1 != H\^\d+ A_V2\] -> \[H\^\d+ A_V1 = H\^\d+ A_V2\]\[\d+,\d+\]$'

    # Remove the common part using regular expression substitution
    cleaned_formula = re.sub(pattern, '', Formula)
    cleaned_formula = cleaned_formula.split(".")[1]
    return cleaned_formula

def check_robustness_U_I_U(Formula):
    pattern = r'&\[H\^\d+ A_V1 != H\^\d+ A_V2\]\^\[\d+,\d+\]'
    # Remove the common part using regular expression substitution
    cleaned_formula = re.sub(pattern, '', Formula)
    cleaned_formula = cleaned_formula.split(".")[1]
    return cleaned_formula

def check_Shortest_path(Formula):
    pattern = r"\[[^\]]+G_V2\] *\^ *\[(\d+),(\d+)\] *\& *\[[^\]]+G_V2\] *-> *\[[^\]]+G_V1\] *\^ *\[(\d+),(\d+)\]"

    # Use re.search to find the first occurrence of the pattern in the formula
    match = re.search(pattern, Formula)

    if match:
        # Extract the range from the matched pattern
        num1, num2 = match.group(1), match.group(2)
        # Construct the replacement string
        replacement = f"[{num1},{num2}]"
        # Use re.sub to replace the pattern with the extracted range
        new_formula = re.sub(pattern, replacement, Formula)
        # Output the new formula
        print(new_formula)
        return new_formula
    else:
        print("Incorrect formula syntax for shortest path.")
        sys.exit(1)
def check_Current_s_O(Formula):
    # Define the pattern to match the common part at the end of the formula
    pattern = r'& \[H\^\d+ A_V1 != H\^\d+ A_V2\]\^\[\d+,\d+\]&\[H\^\d+ O_V1 = H\^\d+ O_V2\]\^\[\d+,\d+\]$'
    # Remove the common part using regular expression substitution
    cleaned_formula = re.sub(pattern, '', Formula)
    cleaned_formula = cleaned_formula.split(".")[1]
    # print("Cleaned Formula:", cleaned_formula)
    return cleaned_formula

def check_Initial_s_o(Formula):
    # Define the pattern to match the common part at the end of the formula
    pattern = r'& \[H\^\d+ A_V1 = H\^\d+ A_V2\]\^\[\d+,\d+\]'
    # Remove the common part using regular expression substitution
    cleaned_formula = re.sub(pattern, '', Formula)
    cleaned_formula = cleaned_formula.split(".")[1]
    # print("Cleaned Formula:", cleaned_formula)
    return cleaned_formula
def check_Service_L_A(Formula):
    pattern = r'E_V1\s*F_V2\s*\.\s*\[H\^\d+\s*I_V1\s*&\s*H\^\d+\s*I_V2\]\s*\^\s*\[\d+,\d+\]\s*->\s*\[H\^\d+\s*G_V1\s*&\s*H\^\d+\s*G_V2\]\s*\^\s*\[\d+,\d+\]\s*'

    if re.match(pattern, Formula):
        print("Formula syntax is valid.")
    else:
        print("Formula syntax is not valid.")
        sys.exit(1)
def check_Non_Interference(Formula):
    pattern = r'E_V1\s*F_V2\s*\.\s*\[H\^\d+\s*I_V1\s*!=\s*H\^\d+\s*I_V2\]\s*\^\s*\[\d+,\d+\]\s*->\s*\[H\^\d+\s*P1_V1\s*&\s*H\^\d+\s*P1_V2\]\s*\^\s*\[\d+,\d+\]\s*\*\s*\[H\^\d+\s*G_V1\s*==\s*H\^\d+\s*G_V2\]\s*\^\s*\[\d+,\d+\]'
    if re.match(pattern, Formula):
        print("Formula syntax is valid.")
    else:
        print("Formula syntax is not valid.")
        sys.exit(1)

def check_Linearizability(Formula):
    pattern = r'E_V1\s*F_V2\s*\.\s*\[H\^\d+\s*I_V1\s*=\s*H\^\d+\s*I_V2\]\s*\^\s*\[\d+,\d+\]\s*\*\s*\[H\^\d+\s*P1_V1\s*&\s*H\^\d+\s*P1_V2\]\s*\^\s*\[\d+,\d+\]\s*\*\s*\[H\^\d+\s*G_V1\s*==\s*H\^\d+\s*G_V2\]\s*\^\s*\[\d+,\d+\]'
    if re.match(pattern, Formula):
        print("Formula syntax is valid.")
    else:
        print("Formula syntax is not valid.")
        sys.exit(1)
def check_Mutation_Testing(Formula):
    pattern = (r'E_V1\s*F_V2\s*\.\s*'
               r'\[H\^\d+\s*t_V1\s*&\s*H\^\d+\s*t_V2\]\s*\^\s*\[\d+,\d+\]\s*&\s*'
               r'\[H\^1\s*I_V1\s*=\s*H\^1\s*I_V2\]\s*\^\s*\[\d+,\d+\]\s*\*\s*'
               r'\[H\^1\s*P1_V1\s*&\s*H\^1\s*P1_V2\]\s*\^\s*\[\d+,\d+\]\s*\*\s*'
               r'\[H\^1\s*G_V1\s*!=\s*H\^1\s*G_V2\]\s*\^\s*\[\d+,\d+\]')

    if re.match(pattern, Formula):
        print("Formula syntax is valid.")
    else:
        print("Formula syntax is not valid.")
def check_Side_Channel_Timing_Attacks(Formula):
    pattern = (r'F_V1\s*F_V2\s*\.\s*A_P\s*E_P\s*\.\s*'
               r'\[H\^\d+\s*I_V1\s*&\s*H\^\d+\s*I_V2\]\s*\^\s*\[\d+,\d+\]\s*->\s*'
               r'\[H\^\d+\s*P1_V1\s*&\s*H\^\d+\s*P1_V2\]\s*\^\s*\[\d+,\d+\]\s*\*\s*'
               r'\[H\^\d+\s*G_V1\s*&\s*H\^\d+\s*G_V2\]\s*\^\s*\[\d+,\d+\]')

    if re.match(pattern, Formula):
        print("Formula syntax is valid.")
    else:
        print("Formula syntax is not valid.")


def check_Observational_Determinism(Formula):
    pattern = (r'E_V1\s*F_V2\s*\.\s*A_P\s*\.\s*'
               r'\[H\^\d+\s*I_V1\s*=\s*H\^\d+\s*I_V2\]\s*\^\s*\[\d+,\d+\]\s*->\s*'
               r'\[H\^\d+\s*P1_V1\s*&\s*H\^\d+\s*P1_V2\]\s*\^\s*\[\d+,\d+\]\s*\*\s*'
               r'\[H\^\d+\s*G_V1\s*=\s*H\^\d+\s*G_V2\]\s*\^\s*\[\d+,\d+\]')

    if re.match(pattern, Formula):
        print("Formula syntax is valid.")
    else:
        print("Formula syntax is not valid.")
