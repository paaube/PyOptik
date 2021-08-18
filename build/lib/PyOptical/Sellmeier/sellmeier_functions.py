import json
import requests
from bs4 import BeautifulSoup


def LoadSellmeier(url):
    """Loads Sellmeier's formula from RefractiveIndex.INFO.

    Arguments:
    url -- link to the material's formula page
    """
    page = requests.get(url)
    assert page.status_code != 404, "No formula found at the given URL"
    soup = BeautifulSoup(page.content, 'html.parser')
    formulas = soup.find_all("code")
    sellmeier = str(formulas[1])[8:-7]

    return(sellmeier)


def SaveSellmeier(url, name):
    """Loads and saves Sellmeier's formula from RefractiveIndex.INFO in a
    json file.

    Arguments:
    url -- link to the material's formula page
    filename -- name of the material used as the index in the json file
    """
    sellmeier = LoadSellmeier(url)

    with open('PyOptik/Data/meta_sellmeier.json', 'r+') as f:
        meta_sellmeier = json.load(f)
        meta_sellmeier['remote_sellmeier'][name] = url
        meta_sellmeier['sellmeier_formula'][name] = sellmeier
        f.seek(0)
        json.dump(meta_sellmeier, f, indent=4)


def RemoveSellmeier(name):
    """Removes Sellmeier's formula stored locally for a given material.

    Arguments:
    name -- name of the material to remove
    """
    with open('PyOptik/Data/meta_sellmeier.json', 'r+') as f:
        meta_sellmeier = json.load(f)
        assert name in meta_sellmeier['sellmeier_formula'],\
            "The material you are trying to remove is not in the local data."
        del meta_sellmeier['remote_sellmeier'][name]
        del meta_sellmeier['sellmeier_formula'][name]

    with open('PyOptik/Data/meta_sellmeier.json', 'w') as f:
        json.dump(meta_sellmeier, f)
