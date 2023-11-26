from tab import Tab
import requests
import json

tabs = []
tabs_dict_list = []


def open_tab(Title, URL, isParent=True):
    new_tab = Tab(Title, URL)
    if isParent:
        tabs.append(new_tab)
        tabs_dict_list.append(new_tab)
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
    tabs[index].web_source = website_html
    print(website_html)


def display_all_tabs():
    for n in range(0, len(tabs)):
        print(f"{n+1}.\t{tabs[n].title}")
        if tabs[n].nested_tabs:
            for i in range(0, len(tabs[n].nested_tabs)):
                print(f"\t{n+1}.{i+1}\t{tabs[n].nested_tabs[i].title}")


def open_nested_tab(indicator):
    print("To add a nested tab, Enter:")
    Title = input("Title:\t").title()
    URL = input("Enter:\nURL:\t")
    sub_tab = open_tab(Title, URL, False)
    if indicator.isdigit():
        parent_tab = tabs[int(indicator)]
        try:
            parent_tab.nested_tabs.append(sub_tab)
            parent_tab.nested_tabs_dict.append(sub_tab.dict)
        except IndexError:
            print(f"index '{indicator}' is out of range.")
            return
        else:
            print(f"{sub_tab.title} has been opened inside {parent_tab.title}")
    else:
        for tab in tabs:
            if tab.title == indicator:
                tab.nested_tabs.append(sub_tab)
                print(f"{sub_tab.title} has been opened inside {tab.title}")
                break
            else:
                print(f"There is no tab with the title {indicator}")


def sort_all_opened_tabs(tab_list):
    Titles = get_all_titles(tab_list)
    boarder = 0
    while boarder < (len(Titles) - 1):
        minIndex = boarder
        for i in range(boarder + 1, len(Titles)):
            if Titles[minIndex].lower() > Titles[i].lower():
                minIndex = i
        temp = Titles[boarder]
        Titles[boarder] = Titles[minIndex]
        Titles[minIndex] = temp
        boarder += 1
    print(Titles)


def get_all_titles(tab_list):
    Titles = []
    for tab in tab_list:
        Titles.append(tab.title)
        for sub_tab in tab.nested_tabs:
            Titles.append(sub_tab.title)
    return Titles


def save_tabs(directory):
    string = json.dumps(tabs_dict_list)
    with open(directory, 'w') as file:
        file.write(string)


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
                    indicator = input("Indicate the Title or index Parent Tab:\t")
                    open_nested_tab(indicator)
                if option == 6:
                    sort_all_opened_tabs(tabs)
                if option == 7:
                    directory = input("Please specify a directory to save to")
                    save_tabs(directory)
                if option == 8:
                    directory = input("Please specify a directory to load from")
                    load_tabs(directory)
            else:
                print("Choice is invalid. Try again.")


mainProgram()
