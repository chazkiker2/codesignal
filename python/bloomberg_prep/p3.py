"""

addNews(title, text) -> void
lookupNews(title) -> text

X most recently added stories our system; otherwise throw em out

autoComplete(str) -> []

abc


V abcdef
V abc
x adb

-----

class NewsItem:
    title
    text
    num_calls


class NewsRoom:
    # stores all of our news

    news: {
        title: text
    }

    Most Recently Used Cache
        - X
        - whatever is the "last"
        - dict as an underlying structure
        - queue


"""

from collections import deque

class NewsItem:
    def __init__(self, title, text):
        self.title = title
        self.text = text
        # self.pub_date = Date()

"""
In terms of N titles added & X number of recent

Time Complexity?
    - addNews
        - O(1)
    - lookUp
        - O(1)
    -

"""


class NewsRoom:
    def __init__(self, number_of_recent):
        self.news = {}
        self.current = deque()
        self.number_of_recent = number_of_recent
        self.trie = Trie()


    def addNews(self, title, text):

        self.news[title] = NewItem(title, text)

        if len(self.current) == number_of_recent:
            self.current.append(title)
            self.trie.append(title)

            remove_title = self.current.popleft()
            self.news.delete(remove_title)
        else:
            self.trie.append(title)
            self.current.append(title)


    def lookupNews(self, title) -> str:
        return self.news[title]


    def autoComplete(self, partial_title: str) -> []:
        res = []

        # use a Prefix Tree (Trie)
        #

        self.trie.look_up(title);

        return res


"""
add_news
- for reports
- put into system

lookup
- for readers
- return text

"""


