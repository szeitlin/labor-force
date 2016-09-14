__author__ = 'szeitlin'

#troubleshooting instructions from tutorial to handle multiple categorical columns with sklearn

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import Imputer


class EncodeCategorical(BaseEstimator, TransformerMixin):
    """ Encode a list of columns, or all columns by default

    Note that the stupidity of not just initializing with the
    sklearn dataset Bunch object is inherited, not my idea.

    """

    def __init__(self, columns=None):
        """
        :param columns: (optional) list of str
        """
        self.columns = columns
        self.encoders = None

    def fit(self, data, target=None):
        """
        :param data: pandas dataframe with named columns
        :param target: str column name
        """
        if self.columns is None:
            self.columns = data.columns

        self.encoders = {
            column: LabelEncoder().fit(data[column])
            for column in self.columns
        }

    def transform(self, data):
        """
        apply the encoders to the dataframe

        :return: pandas dataframe with categorical values encoded as numeric
        """
        output=data.copy()
        for column, encoder in self.encoders.items():
            output[column] = encoder.transform(data[column])

        return output


class ImputeCategorical(BaseEstimator, TransformerMixin):
    """
    Guesses how to fill missing values in a list of columns,
    or all columns by default.

    Again, stupid structure here is inherited and this would probably be easier with pandas.
    """
    def __init__(self, columns=None):
        self.columns = columns
        self.imputer = None

    def fit(self, data, target=None):
        """
        :param data: pandas dataframe with named columns
        """
        if self.columns is None:
            self.columns = data.columns

        self.imputer = Imputer(missing_values=0, strategy='most_frequent') #grea way to create bias!
        self.imputer.fit(data[self.columns])

    def transform(self, data):
        """
        apply the imputers to the dataframe

        :return: pandas dataframe with missing values filled by the mode
        """
        output = data.copy()
        output[self.columns] = self.imputer.transform(output[self.columns])

        return output