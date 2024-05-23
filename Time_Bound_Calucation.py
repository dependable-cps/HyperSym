import re
def reduce_formula(formula):
  values = []
  symbols =[]
  reduced_formula = ""
  value = re.split(r'[*|&]', formula)
  for i in formula:
    if i == "*" or i=="|" or i=="&" or i==".":
      symbols.append(i)
  for i in value:
    values.append(i)
  for i in range(0,len(symbols)):
    left=values[i]
    right=values[i+1]
    # Remove the square brackets
    left = left.strip("[]")
    num1, num2 = map(int, left.split(','))
    right = right.strip("[]")
    num3, num4 = map(int, right.split(','))
    if symbols[i]=="*":
      if not (num1==num3 and num2 == num4):
        num3=num3+num1
        num4=num4+num2+1
    else:
      num3=min(num1,num3)
      num4=max(num2,num4)
    values[i+1]="["+str(num3)+","+str(num4)+"]"
  return values[-1]

def extract_symbols(twtl_formula):
    # Define the regular expression pattern to match symbols
    pattern = r'\[\d+,\s*\d+\]|&|\*|\(|\)|\|'

    # Find all matches of the pattern in the TWTL formula
    matches = re.findall(pattern, twtl_formula)

    # Join the matches to form the extracted symbols
    extracted_symbols = ''.join(matches)

    return extracted_symbols
def replace_substrings(input_string):
    # Define the regular expression pattern to match substrings with [ strings & strings ] pattern
    pattern = r'\[[^]]* & [^]]*\]'

    # Replace all matches of the pattern with an empty space
    replaced_string = re.sub(pattern, '', input_string)

    return replaced_string

def replace_inside_parentheses(formula):
    # Define the regular expression pattern to match substrings inside parentheses
    pattern = r'\([^)]+\)'

    # Find all matches of the pattern in the formula
    matches = re.findall(pattern, formula)

    # Replace each match with "[x,y]"
    replaced_formula = formula
    for match in matches:
        string_to_replace = reduce_formula(match[1:-1])
        replaced_formula = replaced_formula.replace(match, string_to_replace)

    return replaced_formula


# Call the function to extract symbols


def Calculate_Time_Bound(formula):
    print(formula)
    result_string = replace_substrings(formula)
    symbols = extract_symbols(result_string)

    # Remove spaces from the extracted symbols
    symbols_no_space = symbols.replace(" ", "")
    print(symbols_no_space)
    replaced_formula = replace_inside_parentheses(symbols_no_space)
    final_bound = reduce_formula(str(replaced_formula))
    final_bound = final_bound.strip("[]")
    min, time_bound = map(int, final_bound.split(','))
    return time_bound