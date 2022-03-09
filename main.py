# Regular Expression module
import re

# using this package for printing pReTtYy truth table
from prettytable import PrettyTable

from operators import op_and, op_or, op_xor, op_implies, op_iff, op_negate

print("\nTruth Table Generator v1.1")
print("version 1.5")
print("\t- compound proposition supported (beta)")

print("\ncopy paste operators: NOT = '-', AND = '∧', OR = '∨', XOR = '⊕', IMPLIES = '→', IFF = '⟷'")

# limitations:
# no input error catcher
# negate operator not supported


# user_proposition = input("\nenter proposition: ")
# user_proposition = "(p ∧ (q ∧ r)) ∧ s" - solved | compound proposition
# user_proposition = "(q ∧ r) ∧ (s ∧ t)" - solved | compound proposition | case 3
# user_proposition = "(q ∨ r) ∧ (s → q)" - solved | same variable present
# user_proposition = "((p ∧ q) ∧ r) ∧ (s ∧ t)" - solved | compound prop 4 operations
# user_proposition = "(p ∨ ((p ∧ (q ∨ r)) ∨ (s → t))) ∨ u" - solved | compound prop 6 operations
# user_proposition = "(q ∧ r) ∧ (q ∧ r)" - won't work if same proposition present
# user_proposition = "(q ∧ r) ∧ (q ∧ r)"
# user_proposition = "-p ∧ q"
user_proposition = "(-p ∧ q) ∨ (-r)"
# user_proposition = "-p ∧ q" - won't work with negate
# user_proposition = "p ∨ ((p ∧ (q ∨ r)) ∨ (s → t))"
print("\nproposition: ", user_proposition)
# TODO: if input has '()' at the end beginning, remove.

# global variables
variables = []
rows = 0

# read user input
for char in user_proposition:
    if char.isspace():
        continue
    elif char.isalpha():
        variables.append(char)
    # else:
    #     # Todo: input error catcher
    #     print("invalid operator/input!")

# remove duplicate variables
variables = list(dict.fromkeys(variables))


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
print("nestp", nested_propositions)

# detect if there's negate
for q in range(len(nested_propositions)):
    print(q)
    iter_prop = iter(nested_propositions[q])
    for w in nested_propositions[q]:
        print(w)
        if w == "-":
            print("next:", next(iter_prop))
            nested_propositions.insert(0, "-{}".format(next(iter_prop)))


print("nested props to solve:", nested_propositions)

rows = pow(2, len(variables))


def generate_truth_values():
    # generates the truth values of propositional variables stored in a dictionary
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
    # holds the truth values of nested propositions
    # with its corresponding proposition
    nested_propositions_truth_values = {}

    def generate_truth_values_nested(op, op_p, op_q):
        # append to nested propositional variables dictionary
        if op == "∧":
            nested_propositions_truth_values[proposition] = op_and(op_p, op_q)
        elif op == "∨":
            nested_propositions_truth_values[proposition] = op_or(op_p, op_q)
        elif op == "⊕":
            nested_propositions_truth_values[proposition] = op_xor(op_p, op_q)
        elif op == "→":
            nested_propositions_truth_values[proposition] = op_implies(op_p, op_q)
        elif op == "⟷":
            nested_propositions_truth_values[proposition] = op_iff(op_p, op_q)
        elif op == "-":
            nested_propositions_truth_values[proposition] = op_negate(op_p)

    variables_truth_values = generate_truth_values()

    for proposition in nested_propositions:
        print("solved propositions:", nested_propositions_truth_values.keys())
        print("current proposition:", proposition)

        temp_propositional_variables = []
        temp_operator = []

        temp_solved_propositions = []
        new_proposition = ""

        # analyze current proposition
        # case 1: p ^ q - unsolved propositions
        # case 2: (p ^ q) ^ r - with solved proposition and one variable
        # case 3: ((p ^ q) ^ r) ^ (p ^ q) - two solved proposition
        #   case 3.1: (p ^ q) ^ (p ^ q) - two (solved) same proposition

        # check current proposition
        # either case 1, case 2, or case 3

        # check if proposition already has truth values
        is_solved_proposition = False
        temp_new_proposition = []
        for p in reversed(nested_propositions_truth_values.keys()):
            print("iterating through solved propositions:", p)

            temp_prop_1 = re.sub(r"\(", " ", proposition)
            temp_prop_2 = re.sub(r"\)", " ", temp_prop_1)

            temp_p_1 = re.sub(r"\(", " ", p)
            temp_p_2 = re.sub(r"\)", " ", temp_p_1)

            there_is = re.search(temp_p_2, temp_prop_2)
            if there_is:
                print("solved props detected...", p)
                if temp_prop_2 != temp_p_2:
                    temp_solved_propositions.append(p)
                    is_solved_proposition = True

                    if len(temp_new_proposition) == 0:
                        # remove the solved proposition from the current proposition
                        new_proposition = re.sub(temp_p_2, " ", temp_prop_2)
                        temp_new_proposition.append(new_proposition)
                        print("new proposition1:", new_proposition)
                    else:
                        # remove the solved proposition from the current proposition
                        new_proposition = re.sub(temp_p_2, " ", temp_new_proposition[-1])
                        print("new proposition2:", new_proposition)
                        break

        # case 1
        if not is_solved_proposition:
            for x in proposition:
                if x.isalpha():
                    temp_propositional_variables.append(x)
                elif x in ["-", "∧", "∨", "⊕", "→", "⟷"]:
                    temp_operator = x

            if temp_operator == "-":
                generate_truth_values_nested(temp_operator, variables_truth_values[temp_propositional_variables[0]],
                                             variables_truth_values[temp_propositional_variables[0]])
            else:

                generate_truth_values_nested(temp_operator, variables_truth_values[temp_propositional_variables[0]],
                                             variables_truth_values[temp_propositional_variables[1]])

        else:
            # case 2
            if len(temp_solved_propositions) == 1:
                print("case 2 detected...")

                for x in new_proposition:
                    if x.isalpha():
                        temp_propositional_variables.append(x)
                    elif x in ["-", "∧", "∨", "⊕", "→", "⟷"]:
                        temp_operator = x

                generate_truth_values_nested(temp_operator, variables_truth_values[temp_propositional_variables[0]],
                                             nested_propositions_truth_values[temp_solved_propositions[0]])

            # case 3
            elif len(temp_solved_propositions) == 2:
                print("case 3 detected...")
                print("case 3 prop:", new_proposition)
                for x in new_proposition:
                    if x in ["-", "∧", "∨", "⊕", "→", "⟷"]:
                        temp_operator.append(x)
                print(temp_solved_propositions[0])
                print(temp_solved_propositions[1])
                generate_truth_values_nested(temp_operator[0],
                                             nested_propositions_truth_values[temp_solved_propositions[0]],
                                             nested_propositions_truth_values[temp_solved_propositions[1]])

    return nested_propositions_truth_values


def render_table():
    # initiate pretty table object
    # for printing the truth table
    truth_table = PrettyTable()

    print("\nTruth Table:")

    # adding the propositional variables' column to the table
    variables_truth_values = generate_truth_values()
    for x in variables_truth_values:
        truth_table.add_column(x, variables_truth_values[x])

    # adding the operation column to the table
    nested_propositions_truth_values = calculate_operations()
    for z in nested_propositions_truth_values:
        truth_table.add_column(z, nested_propositions_truth_values[z])

    print(truth_table)


# driver code
calculate_operations()
render_table()
