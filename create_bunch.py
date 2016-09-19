__author__ = 'szeitlin'

import json
import pandas as pd
from sklearn.datasets.base import Bunch
import os

def load_files(root='data'):
    """
    Helper method for create_bunch

    Loads the meta, train and test data from a root folder

    :param root: parent folder with the following files:
           meta.json
           training_df.csv
           testing_df.csv
           readme (optional)
    :return: meta (json), train and test (pandas dataframes)

    """
    with open(os.path.join(root, 'meta.json'), 'r') as f:
        meta = json.load(f)

    train = pd.read_csv(os.path.join(root, 'training_df.csv'), index_col=0)
    test = pd.read_csv(os.path.join(root, 'testing_df.csv'), index_col=0)

    return meta, train, test

def create_bunch(meta, train, test, target='income'):
    """
        2) Removes the target from the categorical features

        Preconditions: current version assumes the target column is the last one
        :param meta: json
        :param train: pandas dataframe
        :param test: pandas dataframe
        # :param names: list of str (column names) todo: add this

        :returns: an sklearn Bunch object

    """
    features = meta['feature_names']

    #remove the target column - todo: fix this in make_meta method
    meta['categorical_features'].pop(target)

    #following the tutorial, I hate doing it this way - todo: refactor this to use target name
    return Bunch(
        train_data = train.iloc[:, :-1], #all but the last column
        train_target = train.iloc[:, -1], #only the last column
        test_data = test.iloc[:, :-1],
        test_target = test.iloc[:, -1],
        target_names = meta['target_names'],
        feature_names = meta['feature_names'],
        categorical_features = meta['categorical_features'],
        #DESCR = readme, #assuming this is optional?
    )

if '__name__'=='__main__':
    meta, train, test = load_files('data')
    mybunch = create_bunch(meta, train, test)
