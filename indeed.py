import requests
from bs4 import BeautifulSoup

URL = "https://www.indeed.com"

last_page = -1

INDEED_URL = URL + "/jobs?q=python&limit=50"

while(True):
    indeed_result = requests.get(INDEED_URL)
    indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

    pagination = indeed_soup.find("div", {"class":"pagination"})

    links = pagination.find_all("li")
    
    if not links[-1].find("a", {"aria-label":"Next"}):
        last_page = links[-1].find("b")["aria-label"]
        break
    
    else:
        INDEED_URL = URL + links[-2].find("a")["href"]

print(last_page)
