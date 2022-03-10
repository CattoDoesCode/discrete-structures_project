from logic import user_input, calculate_nested_propositions, render_table, check_validity, print_menu

# driver code
while True:
    print_menu()
    user_input()
    calculate_nested_propositions()
    check_validity()
    render_table()

    replay = input("\ninput new proposition? y/n: ")
    if replay == "n":
        break
