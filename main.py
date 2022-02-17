from operators import AND, OR, XOR, IMPLIES, IFF, negate

# using this package for printing pReTtYy truth table
from prettytable import PrettyTable

print("\nTruth Table Generator v1.1")
print("version 1.1")
print("\t- only limited to one operator")

print("\ncopy paste operators: NOT = '-', AND = '∧', OR = '∨', XOR = '⊕', IMPLIES = '→', IFF = '⟷'")

# limitations:
# no input error catcher
# only limited to one operator


userInput = input("\nenter proposition: ")
print("\nproposition: ", userInput)

variables = []
# operators = []
operator = "invalid operator"
rows = 0

truth_table = PrettyTable()

operators_list = ["-", "∧", "∨", "⊕", "→", "⟷"]


def read_input(proposition):
    global operator, rows

    for char in proposition:
        if char.isspace():
            continue
        elif char.isalpha():
            variables.append(char)
        elif char in operators_list:
            operator = char
        else:
            # Todo: input error catcher
            print("invalid operator/input!")

    rows = pow(2, len(variables))
    render_table(generate_truth_values())


def operators_logic(p_truth_value="n/a", q_truth_value="n/a"):
    if operator == "∧":
        return AND(p_truth_value, q_truth_value)
    elif operator == "∨":
        return OR(p_truth_value, q_truth_value)
    elif operator == "⊕":
        return XOR(p_truth_value, q_truth_value)
    elif operator == "→":
        return IMPLIES(p_truth_value, q_truth_value)
    elif operator == "⟷":
        return IFF(p_truth_value, q_truth_value)
    elif operator == "-":
        return negate(p_truth_value)


def generate_truth_values():
    # generates the truth values of propositional variables stored in a nested list
    # works for n number of propositional variables

    # holds the truth values of all propositional variables
    truth_values = []

    # can't explain dis sht
    rows_copy = rows

    for y in range(len(variables)):
        truth_values.append([])
        while len(truth_values[y]) < rows:
            truth_values[y].extend(int((rows_copy / 2)) * ["T"])
            truth_values[y].extend(int((rows_copy / 2)) * ["F"])

        rows_copy /= 2

    # print("\ntruth values: ", truth_values)
    return truth_values


def render_table(truth_values):
    print("\nTruth Table:")

    # adding the propositional variables' column to the table
    for x in range(len(variables)):
        truth_table.add_column(variables[x], truth_values[x])

    # adding the operation column to the table
    # medyo hard coded pa pro sige lg
    # Todo: make multiple operators available
    operation_truth_val = []

    if operator == "-":
        for z in range(rows):
            operation_truth_val.append(operators_logic(truth_values[0][z]))
        truth_table.add_column("-{} ".format(variables[0]), operation_truth_val)
    elif operator in operators_list:
        for z in range(rows):
            operation_truth_val.append(operators_logic(truth_values[0][z], truth_values[1][z]))
        truth_table.add_column("{} {} {}".format(variables[0], operator, variables[1]), operation_truth_val)

    print(truth_table)


# driver code
read_input(userInput)
