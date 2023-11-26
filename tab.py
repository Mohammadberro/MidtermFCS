# Any opened tab will have a class "Tab".
class Tab:
    def __init__(self, title, url):
        self.title = title
        self.url = url
        self.web_source = ""
        self.dict = {
            "title": title,
            "url": url,
            "nested_tabs": [],
            "website_source": self.web_source
        }
