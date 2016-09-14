__author__ = 'szeitlin'

import pandas as pd
import unittest

from create_bunch import load_files, create_bunch

class TestLoadFiles(unittest.TestCase):

    def setUp(self):
        self.meta, self.train, self.test = load_files()

    def test_load_meta(self):
        self.assertTrue(isinstance(self.meta, dict))

    def test_load_train_test(self):
        self.assertTrue(isinstance(self.train, pd.DataFrame))
        self.assertTrue(isinstance(self.test, pd.DataFrame))

class TestCreateBunch(unittest.TestCase):

    def test_bunch_attribute_types(self):
        meta, train, test = load_files('data')
        mybunch = create_bunch(meta, train, test)
        self.assertTrue(isinstance(mybunch.data, pd.DataFrame))
        self.assertTrue(isinstance(mybunch.data_test, pd.DataFrame))
        self.assertTrue(isinstance(mybunch.target, pd.DataFrame))
        self.assertTrue(isinstance(mybunch.target_test, pd.DataFrame))
        self.assertTrue(isinstance(mybunch.target_names, list))
        self.assertTrue(isinstance(mybunch.feature_names, list))
        self.assertTrue(isinstance(mybunch.categorical_features, list))

if '__name__'=='__main__':
    unittest.main()
