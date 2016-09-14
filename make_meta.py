__author__ = 'szeitlin'

import json

def make_meta(training_data, target='income'):
    """
    Create meta.json for use in creating sklearn Bunch objects

    :param training_data: pandas dataframe
    :return: currently saves to a file named meta.json in folder named 'data'
    """
    meta = {'target_names': list(training_data[target].unique()),
           'feature_names': list(training_data.columns),
           'categorical_features': {
                column: list(training_data[column])
                for column in training_data.columns
                if training_data[column].dtype == 'object'
        },
    }

    with open('data/meta.json', 'w') as f:
        json.dump(meta, f, indent=2)