from tab import Tab
# Importing requests for web scraping.
import requests
# Importing json to write and read files.
import json


# Class Browser to handle Browsing Tasks.
class Browser:
    # Dictionary list to store tabs Dictionaries
    def __init__(self):
        self.tabs_dict_list = []

    # Opening a tab. Parent by default.
    def open_tab(self, Title, URL, isParent=True):
        new_tab = Tab(Title, URL)
        if isParent:    # To avoid confusion, only parent tabs will be appended to initial tabs dictionary list.
            self.tabs_dict_list.append(new_tab.dict)
            print(f"Tab has been opened successfully")
        return new_tab

    # Closing a tab by Index or Title
    def close_tab(self, indicator):
        if indicator.isdigit():
            try:
                index = int(indicator)
                tab_title = self.tabs_dict_list[index]["title"]
                self.tabs_dict_list.pop(index)  # By the removal of dictionary, sub-tabs will be removed as well.
            except IndexError:
                print(f"index '{indicator}' is out of range.")
            else:
                print(f"The tab: {tab_title} has been removed successfully.")
        else:
            success = False  # For feedback in case tab doesn't exist.
            for tab in self.tabs_dict_list:
                if tab['title'] == indicator.title():
                    self.tabs_dict_list.remove(tab)
                    print(f"The tab: {tab['title']} has been removed successfully.")
                    success = True
            if not success:
                print(f"There is no tab with title: {indicator}")

    # View tab's web source by Index or Title.
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

    # Displaying data in sequential form.
    def display_all_tabs(self):
        print("\n\tTitle\t\tUrl")
        for n in range(0, len(self.tabs_dict_list)):
            print(f"{n + 1}.\t {self.tabs_dict_list[n]['title']}\t\t {self.tabs_dict_list[n]['url']}")
            if self.tabs_dict_list[n]["nested_tabs"]:   # To display nested tabs under parent tabs
                print(f"\n|\tnested tabs in\t{self.tabs_dict_list[n]['title']} window:\n|\t\tTitle\t\tUrl")
                for i in range(0, len(self.tabs_dict_list[n]["nested_tabs"])):
                    print(f"|\t{n + 1}.{i + 1}\t{self.tabs_dict_list[n]['nested_tabs'][i]['title']}"
                          f"\t\t{self.tabs_dict_list[n]['nested_tabs'][i]['url']}\n")
        print("")

    # Opening nested tabs based on title or index by Stating isParent: False.
    def open_nested_tab(self, indicator):
        print("To add a nested tab, Enter:")
        Title = input("Title:\t").title()
        URL = input("Enter:\nURL:\t")
        sub_tab = self.open_tab(Title, URL, False)
        if indicator.isdigit():  # Determine whether the user indicated an index or a title.
            parent_tab = self.tabs_dict_list[int(indicator)]
            try:
                parent_tab['nested_tabs'].append(sub_tab.dict)
            except IndexError:
                print(f"index '{indicator}' is out of range.")
                return
            else:
                print(f"{sub_tab.dict['title']} has been opened inside {parent_tab['title']}")
        else:
            success = False
            for tab in self.tabs_dict_list:
                if tab['title'] == indicator.title():
                    tab['nested_tabs'].append(sub_tab.dict)
                    print(f"{sub_tab.title} has been opened inside {tab['title']}")
                    success = True
                    break
            if not success:
                print(f"There is no tab with title: {indicator}")

    # Sorting title by alphabetical order using selection sort.
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
        print("\nSorted Titles:\n", Titles)

    # Getting all titles to be used in sorting method.
    def get_all_tab_titles(self):
        Titles = []
        for tab in self.tabs_dict_list:
            Titles.append(tab['title'])
            for sub_tab in tab['nested_tabs']:
                Titles.append(sub_tab['title'])
        return Titles

    # Saving dictionary list as json. Handling errors.
    def save_tabs(self, directory):
        string = json.dumps(self.tabs_dict_list)
        try:
            with open(directory, 'w') as file:  # write mode to make sure we create a file if not found.
                file.write(string)
                file.close()
        except FileNotFoundError:
            print("File name doesn't exist. Please Specify a valid File Name to Save to.")
        except PermissionError:
            print("Directory not writable. Please Specify a valid Directory to Save to")
        except OSError:
            print("Invalid Directory. Please enter a valid directory and try again.")

    # Importing json data as a Dictionary list. appending every tab to opened_tab_list.
    def import_tabs(self, directory):
        try:
            with open(directory, 'r') as f:
                lines = f.read()
                data = json.loads(lines)
                for item in data:
                    self.tabs_dict_list.append(item)  # By just appending, we preserve temporary data after loading.
                f.close()
        except PermissionError:
            print("Directory not readable. Please Specify a Valid Directory to Read from")
        except FileNotFoundError:
            print("File not found. Please Specify a Valid File Name to Read from.")
        except OSError:
            print("Invalid Directory. Please enter a valid directory and try again.")
