from tab import Tab

tabs = []


def open_tab(Title, URL):
    new_tab = Tab(Title, URL)
    tabs.append(new_tab)


def close_tab(index):
    try:
        tab_title = tabs[index].title
        tabs.pop(index)
    except IndexError:
        print(f"index '{index}' is out of range.")
    except ValueError:
        print(f"index should be and integer.")
    else:
        print(f"The tab: {tab_title} has been removed.")


def mainProgram():
    while True:
        print("Enter your choice:"
              "\n1. Open a Tab"
              "\n2. Close a Tab"
              "\n3. Switch Tab"
              "\n4. Display All Tabs"
              "\n5. Open Nested Tab"
              "\n6. Sort All Tabs"
              "\n7. Save Tabs"
              "\n8. Import Tabs"
              "\n9. Exit")
        try:
            option = int(input("Choice:\t"))
        except ValueError:
            print("Please enter a valid option and try again")
        else:
            if 0 < option <= 9:
                if option == 1:
                    URL = input("Enter:\nURL:\t")
                    Title = input("Title:\t").title()
                    open_tab(URL, Title)
                if option == 2:
                    index = int(input("Enter the index of the tab you wish to close:"))
                    close_tab(index)
            else:
                print("Choice does not exist. Try again.")


mainProgram()
