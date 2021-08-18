import json
import numpy as np
import matplotlib.pyplot as plt
from os.path import join

from PyOptik.Directories import *

class Sellmeier:
    """The Sellmeier class is used to compute the refractive index from the
    locally saved Sellmeier formula.

    Arguments:
    name -- the name of the material you wish to import
    unit -- unit use for the wavelength
    """

    def __init__(self, name, unit = 1e-06):
        self.__name__ = name
        self.unit = unit

        with open(join(DataPath, 'meta_sellmeier.json'), 'r+') as f:
            meta_sellmeier = json.load(f)
            assert name in meta_sellmeier['sellmeier_formula'],\
                "Material not in the local sellmeier bank."\
                "To add it, visit the documentation."

        self.Formula = meta_sellmeier['sellmeier_formula'][name]

    def SellmeierRI(self, wl):
        """Returns the refractive index of the material given the wavelength
        used using Sellmeier's formula.

        Arguments:
        wl -- wavelength
        """
        x = wl * self.unit / 1e-06
        n = eval(self.Formula)

        return(n)

    def PlotSellmeier(self, min, max, nb_pts=100):
        """Plots the refractive index as a function of the wavelength using
        Sellmeier's formula.

        Arguments:
        min -- minimum wavelength value
        max -- maximum wavelength value
        nb_pts -- number of points to compute, default set to 100
        """
        min = min * self.unit / 1e-06
        max = max * self.unit / 1e-06
        gap = (max - min) / nb_pts
        x_sellmeier = []
        current_wl=min
        for i in range(nb_pts+1):
            x_sellmeier.append(current_wl)
            current_wl += gap
        y_sellmeier = []
        for wl in x_sellmeier:
            x=wl
            n = eval(self.Formula)
            y_sellmeier.append(n)
        fig, ax = plt.subplots()
        ax.plot(x_sellmeier, y_sellmeier)
        ax.set(xlabel='wavelength (m)', ylabel='n',
               title=f'Extinction coefficient graph of {self.__name__}')
        ax.grid()
        plt.ylim(0, 2)
        plt.show()


    def __repr__(self):
        return self.__name__

    def __str__(self):
        return self.__name__
