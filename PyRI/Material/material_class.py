import json
import numpy as np


class Material:
    def __init__(self, name):
        self._Data = None
        self.__name__ = name

        with open("PyRI/Data/meta_material.json", 'r+') as f:
            meta_material = json.load(f)
            assert name in meta_material["local_data"],\
                "Material not in the local bank. "\
                "Please refer to Documentation Material section: "\
                # TO DO: update the URL
            "https://pymiesim.readthedocs.io/en/latest/Material.html"

        self.DirFilename = meta_material["local_data"][name]
        self.ExpData = np.load("PyRI/Data/npz/" + self.DirFilename)

    def GetRI(wl):
        if float(self.ExpData['wl_n'][0]) <= wl <= float(self.ExpData['wl_n'][-1]):
            if wl in self.ExpData['wl_n']:
                list_data = list(self.ExpData['wl_n'])
                index = list_data.index(wl)
                return float(self.ExpData['n'][index])
            else:

    def GetCoefficient(wl):

    def __repr__(self):
        return self.__name__

    def __str__(self):
        return self.__name__
