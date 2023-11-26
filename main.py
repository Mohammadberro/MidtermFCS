from browser import Browser

browser = Browser()


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
                    print("To add a tab, Enter:")
                    Title = input("Title:\t").title()
                    URL = input("Enter:\nURL:\t")
                    browser.open_tab(Title, URL)
                if option == 2:
                    index = input("Enter the index of the tab you wish to close:\t")
                    browser.close_tab(index)
                if option == 3:
                    browser.switch_tab()
                if option == 4:
                    browser.display_all_tabs()
                if option == 5:
                    indicator = input("Indicate the Title or index Parent Tab:\t")
                    browser.open_nested_tab(indicator)
                if option == 6:
                    browser.sort_all_opened_tabs()
                if option == 7:
                    directory = input("Please specify a directory to save to\t")
                    browser.save_tabs(directory)
                if option == 8:
                    directory = input("Please specify a directory to load from\t")
                    browser.import_tabs(directory)
                if option == 9:
                    print("Exiting the program...")
                    break
            else:
                print("Choice is invalid. Try again.")


mainProgram()
