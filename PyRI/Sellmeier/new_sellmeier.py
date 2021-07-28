import json
import os
import requests
from bs4 import BeautifulSoup


def LoadSellmeier(url):

    page = requests.get(url)
    assert page.status_code != 404, "There is no formula at the URL you have entered!"
    soup = BeautifulSoup(page.content, 'html.parser')
    formulas = soup.find_all("code")
    sellmeier = str(formulas[1])[8:-7]

    assert "sudo" not in sellmeier, "Something dangerous happining here!"

    return(sellmeier)


def SaveSellmeier(url, filename):
    sellmeier = LoadSellmeier(url)

    with open(os.path.join('../Data', 'Meta.json'), 'r+') as f:
        META = json.load(f)
        META['remote_sellmeier'][filename] = url
        META['local_sellmeier'][filename] = sellmeier
        f.seek(0)
        json.dump(META, f, indent=4)
