from bs4 import BeautifulSoup
from urllib2 import urlopen
from time import sleep # be nice

BASE_URL = raw_input("Insert url http:// needed: ")
section_url = raw_input("Insert section url: ")

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")

def get_category_links(section_url):
    soup = make_soup(section_url)
    boccat = soup.find("dl", "boccat")
    category_links = [BASE_URL + dd.a["href"] for dd in boccat.findAll("dd")]
    return category_links

def get_category_winner(category_url):
    soup = make_soup(category_url)
    category = soup.find("h1", "headline").string
    winner = [h2.string for h2 in soup.findAll("h2", "boc1")]
    runners_up = [h2.string for h2 in soup.findAll("h2", "boc2")]
    return {"category": category,
            "category_url": category_url,
            "winner": winner,
            "runners_up": runners_up}


    print data
