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
        min_wl = float(self.ExpData['wl_n'][0])
        max_wl = float(self.ExpData['wl_n'][-1])
        assert min_wl <= wl <= max_wl,\
            "The wavelength value you entered is out of range. Try using "\
            "GetSellmeier to use the formula. You can refer to the "\
            # TO DO: update the URL
        "documentation: https://URL"

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
            n = n_inf+((n_sup-n_inf)*ratio)

            return float(n)

    def GetEC(self, wl):
        assert 'wl_k' in self.ExpData, "Extinction coefficient unavailable "\
            "for this material."

        min_wl = float(self.ExpData['wl_k'][0])
        max_wl = float(self.ExpData['wl_k'][-1])
        assert min_wl <= wl <= max_wl,\
            "The wavelength value you entered is out of range. Try using "\
            "GetSellmeier to use the formula. You can refer to the "\
            # TO DO: update the URL
        "documentation: https://URL"

        if wl in self.ExpData['wl_k']:
            list_wl = list(self.ExpData['wl_k'])
            wl_index = list_wl.index(wl)

            return float(self.ExpData['k'][wl_index])

        else:
            ind_count = 0
            wl_inf = self.ExpData['wl_k'][ind_count]
            while wl_inf < wl:
                ind_count += 1
                wl_inf = self.ExpData['wl_k'][ind_count]
            wl_inf = self.ExpData['wl_k'][(ind_count-1)]
            wl_sup = self.ExpData['wl_k'][ind_count]
            ratio = (wl - wl_inf)/(wl_sup - wl_inf)

            n_inf = self.ExpData['k'][(ind_count-1)]
            n_sup = self.ExpData['k'][ind_count]
            n = n_inf+((n_sup-n_inf)*ratio)

            return float(n)

    def __repr__(self):
        return self.__name__

    def __str__(self):
        return self.__name__
