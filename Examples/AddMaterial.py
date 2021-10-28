from PyOptik import DataBank
from PyOptik.ExpData import SaveData

print(DataBank())

url = 'https://refractiveindex.info/data_csv.php?datafile=data/main/Al/Rakic.yml'

SaveData(name='Aluminium', url=url)

print(DataBank())
