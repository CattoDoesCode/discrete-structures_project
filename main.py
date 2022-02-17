from operators import AND, OR, XOR, IMPLIES, IFF

# using this package for printing pReTtYy table
from prettytable import PrettyTable

print("\nTruth Table Generator v1.1")
print("version 1.1")
print("\t- only limited to 2 propositional variables")
print("\t- only limited to one operator")
print("\t- negate operator not available")
print("\t- no input error catcher")
print("\ncopy paste operators: NOT = '-', AND = '∧', OR = '∨', XOR = '⊕', IMPLIES = '→', IFF = '⟷'")

userInput = input("\nenter proposition: ")
print("\nproposition: ", userInput)

variables = []
# operators = []
operator = "invalid operator"
rows = 0

truth_table = PrettyTable()


def read_input(proposition):
    # limitation: only works for p and q

    operators_list = ["-", "∧", "∨", "⊕", "→", "⟷"]

    global operator, rows

    for char in proposition:
        if char.isspace():
            continue
        elif char.isalpha():
            variables.append(char)
        elif char in operators_list:
            operator = char
        else:
            print("invalid operator/input!")

    # variables = 3
    rows = pow(2, len(variables))
    # render_table(generate_truth_values())
    render_table_ver2()


def operator_truth_value(p_truth_value, q_truth_value):
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


def generate_truth_values():
    # generates the truth values of propositional variables stored in a list
    # works for n number of propositional variables

    # temporarily holds the  truth values of one propositional variable
    truth_values_temp = []
    # holds all the truth values of all propositional variables
    truth_values = []

    # can't explain dis sht
    rows_copy = rows

    for x in range(len(variables)):
        while len(truth_values_temp) < rows:
            truth_values_temp += int((rows_copy / 2)) * ["T"]
            truth_values_temp += int((rows_copy / 2)) * ["F"]
        truth_values.extend(truth_values_temp)
        truth_values_temp.clear()

        rows_copy /= 2

    # print(truth_values)
    return truth_values


def generate_truth_values_ver2():
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

    # print("\ntruth values: ", *truth_values)
    return truth_values


# def render_table(truth_val):
#     # TODO: render table for n number of propositional variables
#     # limitation: not scalable
#
#     if rows == 4:
#         print("\nTruth Table: ")
#         # TODO: make available for negate
#         print(" {} | {} | {} {} {} ".format(p, q, p, operator, q))
#         print("----------------")
#         for x in range(rows):
#             print(" {} | {} |   {}   ".format(truth_val[x], truth_val[rows + x],
#                                               operator_truth_value(truth_val[x], truth_val[rows + x])))


def render_table_ver2():
    # only works for 2 propositional variables and no values for column 3

    print("\nTruth Table: ")

    # printing the header (variables, operators)
    print('|', end='')
    for x in range(len(variables)):
        print(" {} |".format(variables[x]), end='')

    if operator == "-":
        print(" -{} |".format(variables[0]))
        print("----------")
    else:
        print(" {} {} {} |".format(variables[0], operator, variables[1]))
        print("_________________")

    # [ ['T', 'T', 'F', 'F'] ['T', 'F', 'T', 'F'] ]
    # T T T F F T F F
    # rearrange truth value of variables
    t_values = generate_truth_values_ver2()
    new_truth_values = []
    for sublist in range(1):
        for value in range(rows):
            new_truth_values.append(t_values[sublist][value])
            new_truth_values.append(t_values[sublist + 1][value])

    # print(new_truth_values)

    iter_t_val = iter(new_truth_values)
    for x in range(rows):
        print('\n|', end='')
        for y in range(len(variables)):
            item = next(iter_t_val)
            print("", item, "|", end='')


# driver code
read_input(userInput)
# generate_truth_values_ver2()
