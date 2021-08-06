import json
import os
import pandas as pd
import numpy as np


def load_online(url):
    """Loads the data from RefractiveIndex.INFO and returns it as a
    dictionary.

    Arguments:
    url -- link to the csv file from RefractiveIndex.INFO
    """
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


def save_data(url, name, unit=1e-6):
    """Loads the data from RefractiveIndex.INFO and saves it in a json file.

    Arguments:
    url -- link to the csv file from RefractiveIndex.INFO
    name -- name of the material used as the index in the json file
    """
    dict_data = load_online(url)
    directory = os.path.join('PyRI/Data/npz', name)

    if 'k' not in dict_data:
        np.savez(directory,
                 wl_n=dict_data['wl_n'] * unit,
                 n=dict_data['n'])
    else:
        np.savez(directory,
                 wl_n=dict_data['wl_n'] * unit,
                 n=dict_data['n'],
                 wl_k=dict_data['wl_k'] * unit,
                 k=dict_data['k'])

    with open('PyRI/Data/meta_expdata.json', 'r+') as f:
        meta_expdata = json.load(f)
        meta_expdata['remote_data'][name] = url
        meta_expdata['local_data'][name] = name + '.npz'
        f.seek(0)
        json.dump(meta_expdata, f, indent=4)


def remove_data(name):
    """Removes the experimental data stored locally for a given material.

    Arguments:
    name -- name of the material to remove
    """
    with open('PyRI/Data/meta_expdata.json', 'r+') as f:
        meta_expdata = json.load(f)
        assert name in meta_expdata['local_data'], \
            "The material you are trying to remove is not in the local data."
        del meta_expdata['remote_data'][name]
        del meta_expdata['local_data'][name]
    os.remove(os.path.join('PyRI/Data/npz', name + '.npz'))
    with open('PyRI/Data/meta_expdata.json', 'w') as f:
        json.dump(meta_expdata, f)