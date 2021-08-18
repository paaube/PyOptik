from PyOptical import DataBank, ExpData
from PyOptical.ExpData import SaveData

print(DataBank())

dat = ExpData('BK7')

dat.GetRI([5e-7])
