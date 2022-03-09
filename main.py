from logic import read_input, calculate_operations, render_table, check_validity

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

# driver code
while True:
    read_input()
    calculate_operations()
    check_validity()
    render_table()

    replay = input("\ninput new proposition? y/n: ")
    if replay == "n":
        break
