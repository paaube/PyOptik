import json
import os
import csv
import urllib.request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


PATH = 'Data/'


class Sellmeier:
    def __init__(self, name):
        self.__name__ = name

        with open(os.path.join(PATH, 'Meta.json'), 'r+') as f:
            META = json.load(f)
            assert name in META['local_sellmeier'],\
                "Material {name} not in the local sellmeier bank"\
                "Please refer to Documentation Material section"\
                # TODO: update the URL
            "https://URL"

    def __repr__(self):
        return self.__name__

    def __str__(self):
        return self.__name__
