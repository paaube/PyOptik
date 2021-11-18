import json
import numpy as np
import matplotlib.pyplot as plt
from os.path import join

from PyOptik.Directories import *

class ExpData:
    """The ExpData class is used to import experimental data from the locally
    saved data.

    Arguments:
    name -- the name of the material you wish to import
    """

    def __init__(self, name):
        self._Data = None
        self.__name__ = name

        with open(join(DataPath, 'meta_expdata.json'), 'r+') as f:
            meta_expdata = json.load(f)
            assert name in meta_expdata['local_data'], "Material not in the local data bank. To add it, visit the documentation."

        self.DirFilename = meta_expdata["local_data"][name]
        self.ExpData = np.load( join(NPZPath, self.DirFilename) )

    def VerifyRange(self, values):
        values = np.asarray(values)

        min_wl = float(self.ExpData['wl_n'][0])
        max_wl = float(self.ExpData['wl_n'][-1])
        assert all(values<max_wl) and all(values>min_wl), f"The wavelength value you entered is out of range [{min_wl}, {max_wl}]. Visit the documentation to use Sellmeier's formula"

    def GetRI(self, wl):
        """Returns the refractive index of the material from the experimental
        data given the wavelength used.

        Arguments:
        wl -- wavelength
        """
        if isinstance(wl, float): wl = np.array( [wl] )
        self.VerifyRange(wl)

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
        """Returns the extinction coefficient of the material from the
        experimental data given the wavelength used.

        Arguments:
        wl -- wavelength
        """
        assert 'wl_k' in self.ExpData, "Extinction coefficient unavailable for this material on RefractiveIndex.INFO"

        min_wl = float(self.ExpData['wl_k'][0])
        max_wl = float(self.ExpData['wl_k'][-1])
        assert min_wl <= wl <= max_wl, "The wavelength value you entered is out of range."

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

    def PlotExpData(self, ri=True, ec=True):
        """Plots the experimental data of the material.

        Arguments:
        ri -- plot the refractive index as a function of the wavelength
        ec -- plot the extinction coefficient as a function of the wavelength
        """
        if ri and not ec:
            x_ri = self.ExpData['wl_n']
            y_ri = self.ExpData['n']
            fig, ax = plt.subplots()
            ax.plot(x_ri, y_ri, label='n')
            ax.set(xlabel='wavelength (m)', ylabel='n',
                   title=f'Refractive index graph of {self.__name__}')
            ax.grid()

        if ec and not ri:
            x_ec = self.ExpData['wl_k']
            y_ec = self.ExpData['k']
            fig, ax = plt.subplots()
            ax.plot(x_ec, y_ec, label='k')
            ax.set(xlabel='wavelength (m)', ylabel='k',
                   title=f'Extinction coefficient graph of {self.__name__}')
            ax.grid()

        if ri and ec:
            x_ri = self.ExpData['wl_n']
            y_ri = self.ExpData['n']
            x_ec = self.ExpData['wl_k']
            y_ec = self.ExpData['k']
            fig, ax = plt.subplots()
            ax.plot(x_ri, y_ri, label='n')
            ax.plot(x_ec, y_ec, label='k')
            ax.set(xlabel='wavelength (m)', ylabel='n, k',
                   title='Refractive index and extinction coefficient'
                   f'graph of {self.__name__}')
            ax.grid()
        plt.legend()
        plt.show()

    def __repr__(self):
        return self.__name__

    def __str__(self):
        return self.__name__
