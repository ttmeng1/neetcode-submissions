class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = SiteNode(homepage)
        self.curr = self.homepage

    def visit(self, url: str) -> None:
        new_site = SiteNode(url)
        self.curr.next = new_site
        new_site.prev = self.curr
        self.curr = new_site

    def back(self, steps: int) -> str:
        i = 0
        while self.curr.prev:
            self.curr = self.curr.prev
            i += 1
            if i == steps:
                return self.curr.url
        return self.homepage.url

    def forward(self, steps: int) -> str:
        i = 0
        while self.curr.next:
            self.curr = self.curr.next
            i += 1
            if i == steps:
                return self.curr.url
        return self.curr.url

class SiteNode:

    def __init__(self, url: str):
        self.next = None
        self.prev = None
        self.url = url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)