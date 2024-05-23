import os
from synthesis import synthesis_method
from verification import verification_method
def read_text_file(file_path):
    Formula=""
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                Formula=Formula+line.strip()
            return Formula
    except FileNotFoundError:
        print("File not found at the given location.")
    except Exception as e:
        print("An error occurred:", e)
def remove_spaces(input_string):
    return input_string.replace(" ", "")
# Function to execute specific tasks based on user's choice
def execute_task(choice):
    #uncomment shortest path or any other for its function to work
    switch = {
        1: "shortest_path",
        2: "Robustness under initial uncertainty",
        3: "Robustness under action uncertainty",
        4: "Initial-state opacity",
        5: "Current-state opacity",
        6: "Service Level Agreement",
        7: "Non Interference",
        8: "Linearizability",
        9: "Mutation Testing",
        10: "side channel timing attacks",
        11: "observational Determinism"
    }
    task = switch.get(choice, "Invalid choice")
    if callable(task):
        task()  # Execute the function
    elif task != "Invalid choice":
        print("Algorithm : ", task)
        return task
        # Here you can perform any specific action related to the chosen task
    else:
        print("Invalid choice. Please select a number from 1 to 11.")

# Function for Shortest Path algorithm
def shortest_path():
    # Write your shortest path algorithm implementation here
    print("Executing Shortest Path algorithm...")

def is_valid_file_path(file_path):
    return os.path.isfile(file_path)

def is_valid_input(user_input):
    return user_input.lower() in ['yes', 'no']

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #file_location =("C:/Users/v revanth reddy/Downloads/pythonProject/pythonProject/input_files/text")
    file_location = ("input_files/text")
    dts_file_location =("input_files/dts.txt")
    Formula=read_text_file(file_location)
    print("Formula : "+Formula)
    print("==========================================================================================")
    while True:
        print("Choose from the following tasks:")
        print("1. Shortest path")
        print("2. Robustness under initial uncertainty")
        print("3. Robustness under action uncertainty")
        print("4. Initial-state opacity")
        print("5. Current-state opacity")
        print("6: Service Level Agreement")
        print("7. Non Interference")
        print("8. Linearizability")
        print("9. Mutation Testing")
        print("10. side channel timing attacks")
        print("11. observational Determinism")

        choice = input("Enter the number corresponding to your choice: ")
        if choice.isdigit():
            choice = int(choice)
            if choice in range(1, 12):
                break
            else:
                print("Invalid choice. Please select a number from 1 to 12.")
        else:
            print("Invalid input. Please enter a number.")
    Algorithm = execute_task(choice) #use this to write functions to specific task
    Num_Algorithm = choice
    print("==============================================================================================")
    choice = read_text_file(dts_file_location)
    choice = remove_spaces(choice)
    choice = choice.split(';')[4]
    print(choice)
    if choice.lower() == "verification":
        method = "verification"
        verification_method(Formula, Num_Algorithm,dts_file_location,method)
    elif choice.lower()== "synthesis":
        method = "synthesis"
        synthesis_method(Formula, Num_Algorithm,dts_file_location,method)

    #print("Method : "+ method)
    print("===============================================================================================")

