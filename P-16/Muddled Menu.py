"""Muddled Menu"""


def muddled():
    """Function"""
    lst_menu = []
    while True:
        menu = input()
        if menu == "DONE":
            break
        elif menu == "SOMETHING'S WRONG":
            lst_menu.clear()
        elif "Can't do: " in menu:
            lst_menu.remove(menu[10:])
        elif menu == "CLOSED":
            return print("Full Course: [] Reversed: []")
        else:
            splitter = menu.split(" #")
            if splitter[1].isnumeric():
                lst_menu.insert(int(splitter[1]) - 1, splitter[0])
            else:
                lst_menu.append(splitter[0])
    print("Full Course:", lst_menu, end="")
    lst_menu.reverse()
    print(" Reversed:", lst_menu)


muddled()
