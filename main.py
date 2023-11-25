from tab import Tab
import requests
import pandas as pd

tabs = []
tabs_dict_list = []


def open_tab(Title, URL, Sub_tab = False):
    new_tab = Tab(Title, URL)
    if not Sub_tab:
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
    desired_url = tabs[index].url
    choice = input("View last tab? y/n")
    if choice == "y":
        pass
    else:
        try:
            index = int(input("Please specify the index of the tab you want to view:\t"))
        except ValueError:
            print(f"index should be an integer.")
            return
    try:
        response = requests.get(desired_url)
    except IndexError:
        print(f"index '{index}' is out of range.")
        return
    except requests.exceptions.MissingSchema:
        print(f"The url: {desired_url} is invalid."
              f"Make sure you added a URL Scheme (ex: https://). ")
        if input(f"Do you want to change the url : {requests.get(desired_url)} y/n") == "y":
            tabs[index].url = input(f"Enter the new url for {requests.get(tabs[index].title)}")
            switch_tab(index)
        return
    website_html = response.text
    print(website_html)


def display_all_tabs():
    tabs_dict = [tab.dict for tab in tabs]
    # in case we want to print titles normally:
    # titles = [x.get("title") for x in tabs_dict]
    # print(titles)
    df = pd.DataFrame(tabs_dict)
    df.index += 1
    print(df)


def open_nested_tab(indicator):
    if indicator.isdigit():
        try:
            tabs[int(indicator)].nested_tabs.append(sub_tab)




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
                    open_tab(Title, URL)
                if option == 2:
                    index = input("Enter the index of the tab you wish to close:\t")
                    close_tab(index)
                if option == 3:
                    switch_tab()
                if option == 4:
                    display_all_tabs()
                if option == 5:
                    indicator = input("Indicate the title or index of the tab you want to open in new window:\t")
                    open_nested_tab(indicator)
            else:
                print("Choice is invalid. Try again.")


mainProgram()
