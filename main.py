from logic import read_input, calculate_operations, render_table

print("\nTruth Table Generator")
print("+=========================================================================================+")
print("version 1.5")
print("\t- compound proposition supported (beta)")
print("\t- won't work with duplicate nested proposition e.g. (q ∧ r) ∧ (q ∧ r)")

print("\nnote: \n\t- wrap negated variables with parenthesis e.g. (-p) ∧ q")
print("\t- remove outer parenthesis e.g. do: (-p) ∧ q | don't: ((-p) ∧ q)")
print("\ncopy paste operators: NOT = '-', AND = '∧', OR = '∨', XOR = '⊕', IMPLIES = '→', IFF = '⟷'")
print("sample input: p ∨ ((p ∧ (q ∨ r)) ∨ (s → (-t)))")
print("+=========================================================================================+")

# driver code
while True:
    read_input()
    calculate_operations()
    render_table()

    replay = input("\ninput new proposition? y/n: ")
    if replay == "n":
        break
