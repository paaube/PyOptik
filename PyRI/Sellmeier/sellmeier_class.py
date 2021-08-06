import json


class Sellmeier:
    """The Sellmeier class is used to compute the refractive index from the
    locally saved Sellmeier formula.

    Arguments:
    name -- the name of the material you wish to import
    """

    def __init__(self, name):
        self.__name__ = name

        with open('PyRI/Data/meta_sellmeier.json', 'r+') as f:
            meta_sellmeier = json.load(f)
            assert name in meta_sellmeier['sellmeier_formula'],\
                "Material not in the local sellmeier bank."\
                "To add it, visit the documentation."

        self.Formula = meta_sellmeier['sellmeier_formula'][name]

    def sellmeier_ri(self, wl):
        """Returns the refractive index of the material given the wavelength
        used using Sellmeier's formula.

        Arguments:
        wl -- wavelength
        """
        x = wl
        n = eval(self.Formula)

        return(n)

    def __repr__(self):
        return self.__name__

    def __str__(self):
        return self.__name__
