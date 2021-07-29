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

    def GetRI(self, wl):
        assert float(self.ExpData['wl_n'][0]) <= wl <= float(self.ExpData['wl_n'][-1]),\
            "The wavelength value you entered is out of range. True using GetSellmeier "\
            "to use the formula. You can refer to the documentation: "\
            # TO DO: update the URL
        "https://URL"

        if wl in self.ExpData['wl_n']:
            list_wl = list(self.ExpData['wl_n'])
            wl_index = list_wl.index(wl)

            return float(self.ExpData['n'][wl_index])

        else:
            ind_count = 0
            wl_inf = self.ExpData['wl_n'][ind_count]
            while wl_inf < wl:
                ind_count += 1
                wl_inf = self.ExpData['wl_n'][ind_count]
            wl_inf = self.ExpData['wl_n'][(ind_count-1)]
            wl_sup = self.ExpData['wl_n'][ind_count]
            ratio = (wl - wl_inf)/(wl_sup - wl_inf)

            n_inf = self.ExpData['n'][(ind_count-1)]
            n_sup = self.ExpData['n'][ind_count]
            wl = n_inf+((n_sup-n_inf)*ratio)

            return wl

    def __repr__(self):
        return self.__name__

    def __str__(self):
        return self.__name__
