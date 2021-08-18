import os

import PyOptik

RootPath     = PyOptik.__path__[0]

ZeroPath     = os.path.dirname(RootPath)

DataPath = os.path.join(RootPath, 'Data')

NPZPath      = os.path.join(DataPath, 'npz')
