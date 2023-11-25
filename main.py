from tab import Tab
import requests
import pandas as pd

tabs = []
tabs_dict_list = []


def open_tab(Title, URL):
    new_tab = Tab(Title, URL)
    tabs.append(new_tab)
    print(f"Tab has been opened successfully")
    return new_tab


def close_tab(index):
    try:
        index = int(index)
        tab_title = tabs[index].title
        tabs.pop(index)
    except IndexError:
        print(f"index '{index}' is out of range.")
    except ValueError:
        print(f"index should be an integer.")
    else:
        print(f"The tab: {tab_title} has been removed successfully.")


def switch_tab(index=-1):
    choice = input("View last tab? y/n")
    if choice == "y":
        pass
    else:
        try:
            index = int(input("Please specify the index of the tab you want to view:\t"))
        except ValueError:
            print(f"index should be an integer.")
            return
        except IndexError:
            print(f"index '{index}' is out of range.")
            return
    try:
        response = requests.get(tabs[index].url)
    except requests.exceptions.MissingSchema:
        print(f"The url: {tabs[index].url} is invalid."
              f"Make sure you added a URL Scheme (ex: https://). ")
        if input(f"Do you want to change the url : {requests.get(tabs[index].url)} y/n") == "y":
            tabs[index].url = input(f"Enter the new url for {requests.get(tabs[index].title)}")
            switch_tab()
        return
    website_html = response.text
    print(website_html)


def display_all_tabs():
    tabs_dict = [tab.dict for tab in tabs]
    df = pd.DataFrame(tabs_dict)
    df.index += 1
    print(df)


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
                    Title = input("Title:\t").title()
                    URL = input("Enter:\nURL:\t")
                    open_tab(Title, URL)
                if option == 2:
                    index = input("Enter the index of the tab you wish to close:")
                    close_tab(index)
                if option == 3:
                    switch_tab()
                if option == 4:
                    display_all_tabs()
            else:
                print("Choice does not exist. Try again.")


mainProgram()
