from tab import Tab

tabs = []


def open_tab():
    print("Enter:\n")
    URL = input("URL:\t")
    Title = input("Title:\t").title()
    new_tab = Tab(Title, URL)
    tabs.append(new_tab)


def close_tab():
    index = int(input("Enter the index of the tab you wish to close:"))
    tabs.pop(index)


def mainProgram():
    while True:
        print("Hello! Enter your choice:"
              "\n1. Open a Tab"
              "\n2. Close a Tab"
              "\n3. Switch Tab"
              "\n4. Display All Tabs"
              "\n5. Open Nested Tab"
              "\n6. Sort All Tabs"
              "\n7. Save Tabs"
              "\n8. Import Tabs"
              "\n9. Exit")
        option = int(input(""))
        while not option.isdigit() or not (0 < option <= 9):
            option = input("Please enter a valid option\t")
        if option == 1:
            open_tab()
        if option == 2:
            close_tab()


mainProgram()
