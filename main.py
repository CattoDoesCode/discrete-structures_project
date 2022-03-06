# from operators import AND, OR, XOR, IMPLIES, IFF, negate, op_and
import re

from operators import op_and

# using this package for printing pReTtYy truth table
from prettytable import PrettyTable

print("\nTruth Table Generator v1.1")
print("version 1.1")
print("\t- only limited to one operator")

print("\ncopy paste operators: NOT = '-', AND = '∧', OR = '∨', XOR = '⊕', IMPLIES = '→', IFF = '⟷'")

# limitations:
# no input error catcher
# only limited to one operator


# user_proposition = input("\nenter proposition: ")
user_proposition = "(p ∧ (q ∧ r)) ∧ s"
print("\nproposition: ", user_proposition)

# global variables
variables = []
rows = 0

nested_propositions = []
nested_propositions_truth_values = {}

# constants
operators_list = ["-", "∧", "∨", "⊕", "→", "⟷"]

for char in user_proposition:
    if char.isspace():
        continue
    elif char.isalpha():
        variables.append(char)
    # else:
    #     # Todo: input error catcher
    #     print("invalid operator/input!")


def parenthetic_contents(string):
    # https://stackoverflow.com/a/4285211/16027681
    """Generate parenthesized contents in string as pairs (level, contents)."""
    stack = []
    for i, c in enumerate(string):
        if c == '(':
            stack.append(i)
        elif c == ')' and stack:
            start = stack.pop()
            yield string[start + 1: i]


nested_propositions = list(parenthetic_contents(user_proposition))
nested_propositions.append(user_proposition)
print("nested props:", nested_propositions)

rows = pow(2, len(variables))


def generate_truth_values():
    # generates the truth values of propositional variables stored in a nested list
    # works for n number of propositional variables

    # temporarily holds the truth values of all propositional variables
    temp_truth_values = []

    # holds the truth values of all propositional variables
    # with its corresponding propositional variables
    truth_values = {}

    # temp variable
    rows_copy = rows

    for v in range(len(variables)):
        temp_truth_values.append([])
        while len(temp_truth_values[v]) < rows:
            temp_truth_values[v].extend(int((rows_copy / 2)) * ["T"])
            temp_truth_values[v].extend(int((rows_copy / 2)) * ["F"])

        rows_copy /= 2

    # distribute truth values to respective propositional variables
    for x in range(len(variables)):
        truth_values[variables[x]] = temp_truth_values[x]

    return truth_values


def calculate_operations():
    temp_propositional_variables = []
    temp_operator = ""

    global nested_propositions_truth_values

    variables_truth_values = generate_truth_values()

    for proposition in nested_propositions:
        solved_proposition = ""

        is_solved_proposition = False
        for p in nested_propositions_truth_values.keys():
            there_is = re.search(p, proposition)
            if there_is:
                solved_proposition = p
                is_solved_proposition = True
                break

        if is_solved_proposition:
            new_proposition = re.sub(proposition, "", proposition)
            for x in new_proposition:
                if x.isalpha():
                    temp_propositional_variables.append(x)
                elif x in operators_list:
                    temp_operator = x

            if temp_operator == "∧":
                # append to global nested propositional variables
                nested_propositions_truth_values[proposition] = op_and(
                    variables_truth_values[temp_propositional_variables[0]],
                    nested_propositions_truth_values[solved_proposition])

            # reset values
            temp_propositional_variables.clear()
            temp_operator = ""
            solved_proposition = ""
            is_solved_proposition = False
        else:

            for x in proposition:
                if x.isalpha():
                    temp_propositional_variables.append(x)
                elif x in operators_list:
                    temp_operator = x

            if temp_operator == "∧":
                # append to global nested propositional variables
                # nested_propositions_truth_values.update({proposition: result})
                nested_propositions_truth_values[proposition] = op_and(
                    variables_truth_values[temp_propositional_variables[0]],
                    variables_truth_values[temp_propositional_variables[1]])

            # reset values
            temp_propositional_variables.clear()
            temp_operator = ""


def render_table():
    # initiate pretty table object
    # for printing the truth table
    truth_table = PrettyTable()

    print("\nTruth Table:")

    # adding the propositional variables' column to the table
    truth_values_dict = generate_truth_values()
    for x in truth_values_dict:
        truth_table.add_column(x, truth_values_dict[x])

    # adding the operation column to the table
    # Todo: make multiple operators available

    # for x, y in nested_propositions_truth_values:
    #     truth_table.add_column(x, y)
    for z in nested_propositions_truth_values:
        truth_table.add_column(z, nested_propositions_truth_values[z])

    print(truth_table)


# driver code
calculate_operations()
print("nested: ", nested_propositions_truth_values)
render_table()
