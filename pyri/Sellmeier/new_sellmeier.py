import json
import os
import requests
from bs4 import BeautifulSoup


def load_sellmeier(url):
    """Loads Sellmeier's formula from RefractiveIndex.INFO.

    Arguments:
    url -- link to the material's formula page
    """
    page = requests.get(url)
    assert page.status_code != 404, "No formula found at the given URL"
    soup = BeautifulSoup(page.content, 'html.parser')
    formulas = soup.find_all("code")
    sellmeier = str(formulas[1])[8:-7]

    assert "sudo" not in sellmeier, "Something dangerous happining here!"

    return(sellmeier)


def save_sellmeier(url, filename):
    """Loads and saves Sellmeier's formula from RefractiveIndex.INFO in a
    json file.

    Arguments:
    url -- link to the material's formula page
    filename -- name of the material used as the index in the json file
    """
    sellmeier = load_sellmeier(url)

    with open(os.path.join('pyri/Data', 'meta_sellmeier.json'), 'r+') as f:
        META = json.load(f)
        META['remote_sellmeier'][filename] = url
        META['sellmeier_formula'][filename] = sellmeier
        f.seek(0)
        json.dump(META, f, indent=4)
