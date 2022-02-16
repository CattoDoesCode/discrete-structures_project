from operators import AND, OR, XOR, IMPLIES, IFF

print("\nTruth Table Generator v1.1")
print("version 1.0:")
print("\t- only limited to 2 propositional variables")
print("\t- only limited to one operator")
print("\t- negate operator not available")
print("\t- no input error catcher")
print("\ncopy paste operators: NOT = '-', AND = '∧', OR = '∨', XOR = '⊕', IMPLIES = '→', IFF = '⟷'")


userInput = input("\nenter proposition: ")
print("\nproposition: ", userInput)

p = "x"
q = "y"
operator = "invalid operator"
variables = 0
rows = 0


def read_input(proposition):
    # limitation: only works for p and q
    p_done = False

    operators_list = ["-", "∧", "∨", "⊕", "→", "⟷"]

    global p, q, operator, variables, rows

    for char in proposition:
        if char.isspace():
            continue
        elif char.isalpha():
            if not p_done:
                p = char.lower()
                p_done = True
                variables += 1
            else:
                q = char.lower()
                variables += 1
        elif char in operators_list:
            operator = char
        else:
            print("invalid operator/input!")

    # variables = 3
    rows = pow(2, variables)
    render_table(generate_truth_values())


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

    for x in range(variables):
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

    for y in range(variables):
        truth_values.append([])
        while len(truth_values[y]) < rows:
            truth_values[y].extend(int((rows_copy / 2)) * ["T"])
            truth_values[y].extend(int((rows_copy / 2)) * ["F"])

        rows_copy /= 2

    print(truth_values)
    return truth_values


def render_table(truth_val):
    # TODO: render table for n number of propositional variables
    # limitation: not scalable

    if rows == 4:
        print("\nTruth Table: ")
        # TODO: make available for negate
        print(" {} | {} | {} {} {} ".format(p, q, p, operator, q))
        print("----------------")
        for x in range(rows):
            print(" {} | {} |   {}   ".format(truth_val[x], truth_val[rows + x],
                                              operator_truth_value(truth_val[x], truth_val[rows + x])))


# driver code
read_input(userInput)
generate_truth_values_ver2()
