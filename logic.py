# Regular Expression module
import re

# using this package for printing pReTtYy truth table
from prettytable import PrettyTable

from operators import op_and, op_or, op_xor, op_implies, op_iff, op_negate

# global variables
user_proposition = ""
variables = []
operators = []
rows = 0
nested_propositions = []


def user_input():
    """
    Asks for the user input proposition,
    checks if input has unbalanced parenthesis or invalid operator,
    splits nested propositions from the input proposition.
    """

    global variables, rows, nested_propositions, user_proposition

    is_valid_input = False
    invalid_operator = False

    while not is_valid_input:

        # variables and lists needs to be reset
        # since user could input new proposition without terminating the program
        # where values of variables and lists are still present
        variables.clear()
        rows = 0
        nested_propositions.clear()
        user_proposition = ""
        operators.clear()

        # ask user for input proposition
        user_proposition = input("\nenter proposition: ")
        print("\nproposition: ", user_proposition)

        # read user input
        for char in user_proposition:
            if char.isspace() or char == "(" or char == ")":
                continue
            elif char.isalpha():
                variables.append(char)
            else:
                operators.append(char)

        # input error catcher -  unbalanced parenthesis
        open_paren = re.findall(r"\(", user_proposition)
        close_paren = re.findall(r"\)", user_proposition)

        if len(open_paren) != len(close_paren):
            print("unbalanced parenthesis, re-enter proposition.")
            continue

        # input error catcher - invalid operator
        valid_operators = 0
        for con in operators:
            if con not in ["-", "∧", "∨", "⊕", "→", "⟷"]:
                print("invalid operator: '{}\',".format(con), "re-enter proposition")
                invalid_operator = True
                continue
            else:
                valid_operators += 1

        if len(operators) == valid_operators:
            invalid_operator = False

        # TODO: input error catcher - invalid proposition (excess variable and operator), and incomplete proposition.
        if invalid_operator:
            is_valid_input = False
        else:
            is_valid_input = True

    # remove duplicate variables
    variables = list(dict.fromkeys(variables))

    # dissect input proposition
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

    # remove duplicate propositions
    nested_propositions = list(dict.fromkeys(nested_propositions))

    rows = pow(2, len(variables))


def generate_truth_values():
    """ Generates and returns the truth values of propositional variables.
    Works for n number of propositional variables. """

    # holds the truth values of all propositional variables (value)
    # with its corresponding propositional variables (key)
    variables_truth_values = {}

    # temporarily holds the truth values of all propositional variables
    temp_truth_values = []

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
        variables_truth_values[variables[x]] = temp_truth_values[x]

    return variables_truth_values


def calculate_nested_propositions():
    """ Generates and returns truth values for nested propositions and input proposition.
    Works for n number of nested propositions. """

    # holds the truth values of nested propositions (value)
    # with its corresponding proposition (key)
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

        temp_propositional_variables = []
        temp_operator = []

        temp_solved_propositions = []
        new_proposition = ""

        # analyze current proposition
        # case 1: p ^ q - unsolved propositions
        # case 2: (p ^ q) ^ r - with solved proposition and one variable
        # case 3: ((p ^ q) ^ r) ^ (p ^ q) - two solved proposition

        # check current proposition
        # either case 1, case 2, or case 3

        # check if proposition has solved propositions inside.
        is_solved_proposition = False
        there_is_still_solved = True
        temp_new_proposition = []
        for p in reversed(nested_propositions_truth_values.keys()):

            temp_prop_1 = re.sub(r"\(", " ", proposition)
            temp_prop_2 = re.sub(r"\)", " ", temp_prop_1)

            temp_p_1 = re.sub(r"\(", " ", p)
            temp_p_2 = re.sub(r"\)", " ", temp_p_1)

            there_is_solved = re.search(temp_p_2, temp_prop_2)

            if there_is_solved and there_is_still_solved:
                if temp_prop_2 != temp_p_2:
                    temp_solved_propositions.append(p)
                    is_solved_proposition = True

                    # remove the solved proposition from the current proposition
                    if len(temp_new_proposition) == 0:
                        new_proposition = re.sub(temp_p_2, " ", temp_prop_2)
                        temp_new_proposition.append(new_proposition)
                    else:
                        new_proposition = re.sub(temp_p_2, " ", temp_new_proposition[-1])
                        break

                    # check new proposition
                    for c in nested_propositions_truth_values.keys():
                        there_is_still_solved = re.search(c, new_proposition)

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

                for x in new_proposition:
                    if x.isalpha():
                        temp_propositional_variables.append(x)
                    elif x in ["-", "∧", "∨", "⊕", "→", "⟷"]:
                        temp_operator = x

                if len(temp_propositional_variables) != 0:
                    generate_truth_values_nested(temp_operator, variables_truth_values[temp_propositional_variables[0]],
                                                 nested_propositions_truth_values[temp_solved_propositions[0]])
                else:
                    generate_truth_values_nested(temp_operator,
                                                 nested_propositions_truth_values[temp_solved_propositions[0]],
                                                 nested_propositions_truth_values[temp_solved_propositions[0]])

            # case 3
            elif len(temp_solved_propositions) == 2:
                for x in new_proposition:
                    if x in ["-", "∧", "∨", "⊕", "→", "⟷"]:
                        temp_operator.append(x)
                generate_truth_values_nested(temp_operator[0],
                                             nested_propositions_truth_values[temp_solved_propositions[0]],
                                             nested_propositions_truth_values[temp_solved_propositions[1]])

    return nested_propositions_truth_values


def check_validity():
    """ Evaluates input proposition if it is Valid or Invalid Proposition. """

    is_invalid_proposition = False

    proposition_truth_values = calculate_nested_propositions()

    input_proposition_truth_values = proposition_truth_values[user_proposition]

    for truth_value in input_proposition_truth_values:
        if truth_value == "F":
            is_invalid_proposition = True
            break

    if is_invalid_proposition:
        print("\nproposition is INVALID")
    else:
        print("\nproposition is VALID")


def render_table():
    """ Prints the truth table from variables and nested_propositions truth values using the PrettyTable package. """

    # initiate PrettyTable object
    truth_table = PrettyTable()

    print("\nTruth Table:")

    # adding the propositional variables' column to the table
    variables_truth_values = generate_truth_values()
    for x in variables_truth_values:
        truth_table.add_column(x, variables_truth_values[x])

    # adding the operation column to the table
    nested_propositions_truth_values = calculate_nested_propositions()
    for z in nested_propositions_truth_values:
        truth_table.add_column(z, nested_propositions_truth_values[z])

    print(truth_table)


def print_menu():
    print("\nTruth Table Generator")
    print("+=======================================================================================+")
    print("version 2.0")
    print("\t- compound proposition supported")
    print("\t- works for n number of variables and propositions")

    print("\nnote: \n\t- wrap negated variables with parenthesis e.g. (-p) ∧ q")
    print("\t- remove outer parenthesis e.g. do: (-p) ∧ q | don't: ((-p) ∧ q)")
    print("\ncopy paste operators: NOT = '-', AND = '∧', OR = '∨', XOR = '⊕', IMPLIES = '→', IFF = '⟷'")
    print("sample input: p ∨ ((p ∧ (q ∨ r)) ∨ (s → (-t)))")
    print("+=======================================================================================+")
