__author__ = 'szeitlin'

#troubleshooting instructions from tutorial to handle multiple categorical columns with sklearn

#from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import LabelEncoder, Imputer


def multi_column_encoding(df, colnames):
    """
    My version - just apply sklearn.preprocessing.LabelEncoder
    fit and transform to multiple columns

    :param df: pandas dataframe
    :param colnames: list of str (names of categorical columns)
    :return: transformed df
    """
    encoders = {column: LabelEncoder().fit(df[column])
                for column in colnames
                }
    output = df.copy()
    for column, encoder in encoders.items():
        output[column] = encoder.transform(df[column])
    return output

def multi_column_imputing(df, colnames, strategy='most_frequent'):
    """
    My version - just apply sklearn.preprocessing.Imputer
    fit and transform to multiple columns

    :param df: pandas dataframe
    :param columns: list of str (names of columns with missing values)
    :return: filled df
    """
    imputer = Imputer(missing_values=0, strategy=strategy)
    imputer.fit(df[colnames]) #if it can already take a dataframe, why do you need to even do this-?
    output = df.copy()
    output[colnames] = imputer.transform(output[colnames])
    return output
