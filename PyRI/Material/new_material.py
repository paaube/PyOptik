import json
import os
import pandas as pd
import numpy as np


def LoadOnline(url):
    df = pd.read_csv(url)
    df = df.to_numpy()

    if ['wl', 'k'] in df:
        index = int(np.where(df == 'wl')[0])
        df = np.concatenate((df[:index], df[index+1:]), axis=1)

        data = {'wl_n': df[:, 0].astype(float),
                'n': df[:, 1].astype(float),
                'wl_k': df[:, 2].astype(float),
                'k': df[:, 3].astype(float)}

    else:
        data = {'wl_n': df[:, 0].astype(float),
                'n': df[:, 1].astype(float)}

    return data


def SaveData(url, filename, unit=1e-6):
    dict_data = LoadOnline(url)
    directory = os.path.join('../Data/npz', filename)

    if 'k' not in dict_data:
        np.savez(directory,
                 wl_n=dict_data['wl_n'] * unit,
                 n=dict_data['n'])
    else:
        np.savez(directory,
                 wl_n=dict_data['wl_n'] * unit,
                 n=dict_data['n'],
                 wl_k=dict_data['wl_k'] * unit,
                 k=dict_data['k']
                 )

    with open(os.path.join('../Data', 'Meta.json'), 'r+') as f:
        META = json.load(f)
        META['remote'][filename] = url
        META['local'][filename] = filename + '.npz'
        f.seek(0)
        json.dump(META, f, indent=4)
