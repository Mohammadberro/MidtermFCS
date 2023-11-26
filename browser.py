from tab import Tab
import requests
import json


class Browser:
    def __init__(self):
        # self.tabs = []
        self.tabs_dict_list = []

    def open_tab(self, Title, URL, isParent=True):
        new_tab = Tab(Title, URL)
        if isParent:
            # self.tabs.append(new_tab)
            self.tabs_dict_list.append(new_tab.dict)
            print(f"Tab has been opened successfully")
        return new_tab

    def close_tab(self, index):
        try:
            index = int(index)
            tab_title = self.tabs_dict_list[index]["title"]
            self.tabs_dict_list.pop(index)
        except IndexError:
            print(f"index '{index}' is out of range.")
        except ValueError:
            print(f"index should be an integer.")
        else:
            print(f"The tab: {tab_title} has been removed successfully.")

    def switch_tab(self, index=-1):
        desired_url = self.tabs_dict_list[index]["url"]
        choice = input("View last tab? y/n\t").lower()
        while choice != ("y" or "n"):
            choice = input("Invalid choice. Please answer with 'y' or 'n' ")
        if choice == "y":
            pass
        else:
            try:
                index = int(input("Please specify the index of the tab you want to view:\t"))
            except ValueError:
                print(f"index should be an integer. Try again.")
                return
        try:
            response = requests.get(desired_url)
        except IndexError:
            print(f"index '{index}' is out of range. Try again")
            return
        except requests.exceptions.MissingSchema:
            print(f"The url: {desired_url} is invalid."
                  f"Make sure you added a URL Scheme (ex: https://). ")
            if input(f"Do you want to change the url : {desired_url} y/n\t") == "y":
                self.tabs_dict_list[index]["url"] = input(f"Enter the new url for"
                                                          f" {self.tabs_dict_list[index]['title']}\t")
                self.switch_tab(index)
            return
        except requests.exceptions.ConnectionError:
            print(f"The url: {desired_url} is invalid.")
            if input(f"Do you want to change the url : {desired_url} y/n\t") == "y":
                self.tabs_dict_list[index]["url"] = input(f"Enter the new url for"
                                                          f" {self.tabs_dict_list[index]['title']}\t")
                self.switch_tab(index)
            return
        website_html = response.text
        self.tabs_dict_list[index]["website_source"] = website_html
        print(website_html)

    def display_all_tabs(self):
        for n in range(0, len(self.tabs_dict_list)):
            print(f"{n + 1}.\t{self.tabs_dict_list[n]['title']}")
            if self.tabs_dict_list[n]["nested_tabs"]:
                for i in range(0, len(self.tabs_dict_list[n]["nested_tabs"])):
                    print(f"\t{n + 1}.{i + 1}\t{self.tabs_dict_list[n]['nested_tabs'][i]['title']}")

    def open_nested_tab(self, indicator):
        print("To add a nested tab, Enter:")
        Title = input("Title:\t").title()
        URL = input("Enter:\nURL:\t")
        sub_tab = self.open_tab(Title, URL, False)
        if indicator.isdigit():
            parent_tab = self.tabs_dict_list[int(indicator)]
            try:
                # parent_tab.nested_tabs.append(sub_tab)
                parent_tab.nested_tabs_dict.append(sub_tab.dict)
            except IndexError:
                print(f"index '{indicator}' is out of range.")
                return
            else:
                print(f"{sub_tab.title} has been opened inside {parent_tab['title']}")
        else:
            for tab in self.tabs_dict_list:
                if tab['title'] == indicator:
                    tab.nested_tabs_dict.append(sub_tab.dict)
                    print(f"{sub_tab.title} has been opened inside {tab.title}")
                    break
                else:
                    print(f"There is no tab with the title {indicator}")

    def sort_all_opened_tabs(self):
        Titles = self.get_all_tab_titles()
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

    def get_all_tab_titles(self):
        Titles = []
        for tab in self.tabs_dict_list:
            Titles.append(tab['title'])
            for sub_tab in tab.nested_tabs_dict:
                Titles.append(sub_tab['title'])
        return Titles

    def save_tabs(self, directory):
        string = json.dumps(self.tabs_dict_list)
        with open(directory, 'w') as file:
            file.write(string)

    def import_tabs(self, directory):
        with open(directory, 'r') as f:
            lines = f.read()
            self.tabs_dict_list = json.loads(lines)
