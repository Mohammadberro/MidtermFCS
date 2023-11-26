class Tab:
    def __init__(self, title, url):
        self.title = title
        self.url = url
        # self.nested_tabs = []
        self.nested_tabs_dict = []
        self.web_source = ""
        self.dict = {
            "title": title,
            "url": url,
            "nested_tabs": self.nested_tabs_dict,
            "website_source": self.web_source
        }
