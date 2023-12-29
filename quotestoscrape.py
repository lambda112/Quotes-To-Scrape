import requests as r
from bs4 import BeautifulSoup
import pandas as pd

response = r.get("http://quotes.toscrape.com/")
soup =  BeautifulSoup(response.content, "html.parser")

def get_authors():
    authors = []
    [authors.append(i.text) for i in soup.find_all("small", class_ = "author")]
    return authors

def get_quotes():
    quotes = []
    [quotes.append(i.text) for i in soup.find_all("span", class_ = "text")]
    return quotes

def get_tags():
    tags = []
    [tags.append(i["content"]) for i in soup.find_all("meta", class_ = "keywords")]
    return tags

def create_table():
    table = pd.DataFrame({
        "Authors": get_authors(),
        "Quotes": get_quotes(),
        "Tags": get_tags()                
    })
    table = table.set_index("Authors")
    return table

print(create_table())

