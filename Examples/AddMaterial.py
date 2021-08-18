import PyRI
from PyRI import DataBank
from PyRI.ExpData import SaveData

print(DataBank())


url = "https://refractiveindex.info/data_csv.php?datafile=data/main/Ag/Johnson.yml"
url = 'https://refractiveindex.info/data_csv.php?datafile=data/glass/schott/N-BK7.yml'
url = 'https://refractiveindex.info/data_csv.php?datafile=data/glass/misc/soda-lime/Rubin-clear.yml'
url = 'https://refractiveindex.info/data_csv.php?datafile=data/main/SiO2/Malitson.yml'
url = 'https://refractiveindex.info/data_csv.php?datafile=data/main/Au/Johnson.yml'
url = 'https://refractiveindex.info/data_csv.php?datafile=data/main/Al/Rakic.yml'



SaveData(name='Aluminium', url=url)
print(DataBank())
