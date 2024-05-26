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
    pattern1 = r'E_V\d+\s*F_V\d+\s*\.\s*\[H\^\d+\s*I_V\d+\s*=\s*H\^\d+\s*I_V\d+\]\s*\^\s*\[\d+,\d+\]\s*(?:\*\s*\[H\^\d+\s*P\d+_V\d+\s*&\s*H\^\d+\s*P\d+_V\d+\]\s*\^\s*\[\d+,\d+\]\s*)*\*\s*\(\[H\^\d+\s*G_V\d+\]\s*\^\s*\[\d+,\d+\]\s*&\s*\[H\^\d+\s*G_V\d+\]\s*->\s*\[H\^\d+\s*G_V\d+\]\s*\^\s*\[\d+,\d+\]\)'
    if(re.search(pattern1,Formula)):
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
def check_Formula(Formula):
    pattern1 = r'E_V\d+\s*F_V\d+\s*\.\s*\[H\^\d+\s*I_V\d+\s*=\s*H\^\d+\s*I_V\d+\]\s*\^\s*\[\d+,\d+\]\s*\*\s*\[H\^\d+\s*P\d+_V\d+\s*&\s*H\^\d+\s*P\d+_V\d+\]\s*\^\s*\[\d+,\d+\]\s*\*\s*\(\[H\^\d+\s*G_V\d+\]\s*\^\s*\[\d+,\d+\]\s*&\s*\[H\^\d+\s*G_V\d+\]\s*->\s*\[H\^\d+\s*G_V\d+\]\s*\^\s*\[\d+,\d+\]\)'
    pattern2= (
    r'E_V\d+\s*'  # Matches "E_V" followed by digits
    r'F_V\d+\s*\.\s*'  # Matches "F_V" followed by digits and a period
    r'\[H\^\d+\s*I_V\d+\s*!=\s*H\^\d+\s*I_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "[H^<number> I_V<number> != H^<number> I_V<number>]^[<number>,<number>]"
    r'\*\s*\[H\^\d+\s*P\d+_V\d+\s*&\s*H\^\d+\s*P\d+_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "[H^<number> P<number>_V<number> & H^<number> P<number>_V<number>]^[<number>,<number>]"
    r'\*\s*\[H\d+\s*G_V\d+\s*&\s*H\d+\s*G_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "[H<number> G_V<number> & H<number> G_V<number>]^[<number>,<number>]"
    r'&\s*\[H\^\d+\s*A_V\d+\s*!=\s*H\^\d+\s*A_V\d+\]\s*\^\s*\[\d+,\d+\]'  # Matches "[H^<number> A_V<number> != H^<number> A_V<number>]^[<number>,<number>]"
    )
    pattern3 = (
        r'E_V\d+\s*'  # Matches "E_V" followed by digits
        r'F_V\d+\s*\.\s*'  # Matches "F_V" followed by digits and a period
        r'\(\s*'  # Matches opening parenthesis with optional whitespace
        r'\[H\^\d+\s*I_V\d+\s*&\s*H\^\d+\s*I_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "[H^<number> I_V<number> & H^<number> I_V<number>]^[<number>,<number>]"
        r'\*\s*\[H\^\d+\s*P\d+_V\d+\s*&\s*H\^\d+\s*P\d+_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "[H^<number> P<number>_V<number> & H^<number> P<number>_V<number>]^[<number>,<number>]"
        r'\*\s*\[H\^\d+\s*G_V\d+\s*&\s*H\^\d+\s*G_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "[H^<number> G_V<number> & H^<number> G_V<number>]^[<number>,<number>]"
        r'\)\s*&\s*'  # Matches closing parenthesis and "&" with optional whitespace
        r'\[H\^\d+\s*A_V\d+\s*!=\s*H\^\d+\s*A_V\d+\]\s*'  # Matches "[H^<number> A_V<number> != H^<number> A_V<number>]"
        r'->\s*\[H\^\d+\s*A_V\d+\s*=\s*H\^\d+\s*A_V\d+\]\s*\^\s*\[\d+,\d+\]'
    # Matches "->[H^<number> A_V<number> = H^<number> A_V<number>]^[<number>,<number>]"
    )
    pattern4 = (
        r'E_V\d+\s*'  # Matches "E_V" followed by digits
        r'E_V\d+\s*\.\s*'  # Matches "E_V" followed by digits and a period
        r'\[H\^\d+\s*I_V\d+\s*!=\s*H\^\d+\s*I_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "[H^<number> I_V<number> != H^<number> I_V<number>]^[<number>,<number>]"
        r'\*\s*\[H\^\d+\s*P\d+_V\d+\s*&\s*H\^\d+\s*P\d+_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "*[H^<number> P<number>_V<number> & H^<number> P<number>_V<number>]^[<number>,<number>]"
        r'&\s*\[H\^\d+\s*A_V\d+\s*=\s*H\^\d+\s*A_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "&[H^<number> A_V<number> = H^<number> A_V<number>]^[<number>,<number>]"
        r'\*\s*\[H\^\d+\s*G_V\d+\s*&\s*H\^\d+\s*G_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "*[H^<number> G_V<number> & H^<number> G_V<number>]^[<number>,<number>]"
    )
    pattern5 = (
        r'E_V\d+\s*'  # Matches "E_V" followed by digits
        r'E_V\d+\s*\.\s*'  # Matches "E_V" followed by digits and a period
        r'\[H\^\d+\s*I_V\d+\s*&\s*H\^\d+\s*I_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "[H^<number> I_V<number> & H^<number> I_V<number>]^[<number>,<number>]"
        r'\*\s*\[H\^\d+\s*P\d+_V\d+\s*&\s*H\^\d+\s*P\d+_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "*[H^<number> P<number>_V<number> & H^<number> P<number>_V<number>]^[<number>,<number>]"
        r'\*\s*\[H\^\d+\s*G_V\d+\s*&\s*H\^\d+\s*G_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "*[H^<number> G_V<number> & H^<number> G_V<number>]^[<number>,<number>]"
        r'&\s*\[H\^\d+\s*A_V\d+\s*!=\s*H\^\d+\s*A_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "&[H^<number> A_V<number> != H^<number> A_V<number>]^[<number>,<number>]"
        r'&\s*\[H\^\d+\s*O_V\d+\s*=\s*H\^\d+\s*O_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'
    # Matches "&[H^<number> O_V<number> = H^<number> O_V<number>]^[<number>,<number>]"
    )
    pattern6 = (
        r'E_V\d+\s*'  # Matches "E_V" followed by digits
        r'F_V\d+\s*\.\s*'  # Matches "F_V" followed by digits and a period
        r'\[H\^\d+\s*I_V\d+\s*&\s*H\^\d+\s*I_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "[H^<number> I_V<number> & H^<number> I_V<number>]^[<number>,<number>]"
        r'->\s*\[H\^\d+\s*G_V\d+\s*&\s*H\^\d+\s*G_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "->[H^<number> G_V<number> & H^<number> G_V<number>]^[<number>,<number>]"
        r'\*\s*\[H\d+\s*G_V\d+\s*&\s*H\d+\s*G_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'
    # Matches "*[H<number> G_V<number> & H<number> G_V<number>]^[<number>,<number>]"
    )
    pattern7 = (
        r'E_V\d+\s*'  # Matches "E_V" followed by digits
        r'F_V\d+\s*\.\s*'  # Matches "F_V" followed by digits and a period
        r'\[H\^\d+\s*I_V\d+\s*!=\s*H\^\d+\s*I_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "[H^<number> I_V<number> != H^<number> I_V<number>]^[<number>,<number>]"
        r'->\s*\[H\^\d+\s*P\d+_V\d+\s*&\s*H\^\d+\s*P\d+_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "->[H^<number> P<number>_V<number> & H^<number> P<number>_V<number>]^[<number>,<number>]"
        r'\*\s*\[H\^\d+\s*G_V\d+\s*=\s*H\^\d+\s*G_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "*[H^<number> G_V<number> = H^<number> G_V<number>]^[<number>,<number>]"
    )
    pattern8 = (
        r'E_V\d+\s*'  # Matches "E_V" followed by digits
        r'F_V\d+\s*\.\s*'  # Matches "F_V" followed by digits and a period
        r'\[H\^\d+\s*I_V\d+\s*=\s*H\^\d+\s*I_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "[H^<number> I_V<number> = H^<number> I_V<number>]^[<number>,<number>]"
        r'\*\s*\[H\^\d+\s*P\d+_V\d+\s*&\s*H\^\d+\s*P\d+_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "*[H^<number> P<number>_V<number> & H^<number> P<number>_V<number>]^[<number>,<number>]"
        r'\*\s*\[H\^\d+\s*G_V\d+\s*=\s*H\^\d+\s*G_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "*[H^<number> G_V<number> = H^<number> G_V<number>]^[<number>,<number>]"
    )
    pattern9 = (
        r'E_V\d+\s*'  # Matches "E_V" followed by digits and optional whitespace
        r'F_V\d+\s*\.\s*'  # Matches "F_V" followed by digits, a period, and optional whitespace
        r'\[H\^\d+\s*t_V\d+\s*&\s*H\^\d+\s*t_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "[H^<number> t_V<number> & H^<number> t_V<number>]^[<number>,<number>]" and optional whitespace
        r'&\s*\[H\^\d+\s*I_V\d+\s*=\s*H\^\d+\s*I_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "& [H^<number> I_V<number> = H^<number> I_V<number>]^[<number>,<number>]" and optional whitespace
        r'\*\s*\[H\^\d+\s*P\d+_V\d+\s*&\s*H\^\d+\s*P\d+_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "* [H^<number> P<number>_V<number> & H^<number> P<number>_V<number>]^[<number>,<number>]" and optional whitespace
        r'\*\s*\[H\^\d+\s*G_V\d+\s*!=\s*H\^\d+\s*G_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'
    # Matches "* [H^<number> G_V<number> != H^<number> G_V<number>]^[<number>,<number>]" and optional whitespace
    )
    pattern10 = (
        r'F_V\d+\s*'  # Matches "F_V" followed by digits and optional whitespace
        r'F_V\d+\s*\.\s*'  # Matches "F_V" followed by digits, a period, and optional whitespace
        r'A_P\s*E_P\s*\.\s*'  # Matches "A_P E_P ." with optional whitespace
        r'\[H\^\d+\s*I_V\d+\s*&\s*H\^\d+\s*I_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "[H^<number> I_V<number> & H^<number> I_V<number>]^[<number>,<number>]" and optional whitespace
        r'->\s*\[H\^\d+\s*P\d+_V\d+\s*&\s*H\^\d+\s*P\d+_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "->[H^<number> P<number>_V<number> & H^<number> P<number>_V<number>]^[<number>,<number>]" and optional whitespace
        r'\*\s*\[H\^\d+\s*G_V\d+\s*&\s*H\^\d+\s*G_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "*[H^<number> G_V<number> & H^<number> G_V<number>]^[<number>,<number>]" and optional whitespace
    )
    pattern11 = (
        r'E_V\d+\s*'  # Matches "E_V" followed by digits and optional whitespace
        r'F_V\d+\s*\.\s*'  # Matches "F_V" followed by digits, a period, and optional whitespace
        r'A_P\s*\.\s*'  # Matches "A_P ." with optional whitespace
        r'\[H\^\d+\s*I_V\d+\s*=\s*H\^\d+\s*I_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "[H^<number> I_V<number> = H^<number> I_V<number>]^[<number>,<number>]" and optional whitespace
        r'->\s*\[H\^\d+\s*P\d+_V\d+\s*&\s*H\^\d+\s*P\d+_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'  # Matches "->[H^<number> P<number>_V<number> & H^<number> P<number>_V<number>]^[<number>,<number>]" and optional whitespace
        r'\*\s*\[H\^\d+\s*G_V\d+\s*=\s*H\^\d+\s*G_V\d+\]\s*\^\s*\[\d+,\d+\]\s*'
    # Matches "*[H^<number> G_V<number> = H^<number> G_V<number>]^[<number>,<number>]" and optional whitespace
    )
    if re.fullmatch(pattern1, Formula):
        return 1
    elif re.fullmatch(pattern2, Formula):
        return 2
    elif re.fullmatch(pattern3, Formula):
        return 3
    elif re.fullmatch(pattern4, Formula):
        return 4
    elif re.fullmatch(pattern5, Formula):
        return 5
    elif re.fullmatch(pattern6, Formula):
        return 6
    elif re.fullmatch(pattern7, Formula):
        return 7
    elif re.fullmatch(pattern8, Formula):
        return 8
    elif re.fullmatch(pattern9, Formula):
        return 9
    elif re.fullmatch(pattern10, Formula):
        return 10
    elif re.fullmatch(pattern11, Formula):
        return 11
    else:
        return 12