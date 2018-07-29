# 
#  Author: Rongyang Sun <sun-rongyang@outlook.com>
#  Creation Date: 2018-07-09 20:59
#  
#  Description: alpskit project. Unit test for data module.
# 
import unittest
import alpskit.data as data

import os

import numpy as np


class TestMeasuDataFuncs(unittest.TestCase):
  def setUp(self):
    self.measu_data1 = data.MeasuData(x = np.array([1,2]),
                                      y = np.array([3,4]),
                                      props = {'key1': 'val1'})
    self.measu_data1_jss = ('{\n  "MeasuData": [\n    '
                            '{\n      "x": [\n        1, \n        2\n      ]\n    }, \n    '
                            '{\n      "y": [\n        3, \n        4\n      ]\n    }, \n    '
                            '{\n      "props": {\n        "key1": "val1"\n      }\n    }\n  ]\n}')

  def test_measu_data_to_jss(self):
    measu_data1 = self.measu_data1
    measu_data1_jss_gt = self.measu_data1_jss
    measu_data1_jss = data.measu_data_to_jss(measu_data1)
    self.assertEqual(measu_data1_jss, measu_data1_jss_gt)

  def test_jss_to_measu_data(self):
    measu_data1_gt = self.measu_data1
    measu_data1_jss = self.measu_data1_jss
    measu_data1 = data.jss_to_measu_data(measu_data1_jss)
    np.testing.assert_array_equal(measu_data1.x, measu_data1_gt.x)
    np.testing.assert_array_equal(measu_data1.y, measu_data1_gt.y)
    self.assertEqual(measu_data1_gt.props, measu_data1.props)


class TestPropsFuncs(unittest.TestCase):
  def setUp(self):
    self.case1 = './key1=1_key2=0.3_key3=1e-5_key4=str_suffix'
    os.mkdir(self.case1)

  def test_get_props(self):
    props_dict = data.get_props(self.case1)
    self.assertEqual(props_dict,
                     {'key1':   1,
                      'key2':   0.3,
                      'key3':   1e-5,
                      'key4':   'str',
                      '#0': 'suffix'})
  
  def tearDown(self):
    os.rmdir(self.case1)

if __name__ == '__main__':
  unittest.main()
