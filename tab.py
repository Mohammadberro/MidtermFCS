class Tab:
    def __init__(self, title, url):
        self.title = title
        self.url = url
        self.nested_tabs = []
        self.dict = {
            "title": title,
            "url": url,
            "nested_tabs": self.nested_tabs,
        }
