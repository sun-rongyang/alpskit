# 
#  Author: Rongyang Sun <sun-rongyang@outlook.com>
#  Creation Date: 2018-07-09 20:59
#  
#  Description: alpskit project. Unit test for data module.
# 
import unittest
import alpskit.data as data

import numpy as np


class TestDataSetFuncs(unittest.TestCase):
  def setUp(self):
    self.data_set1 = data.pyalps.DataSet(x = np.array([1,2]),
                                         y = np.array([3,4]),
                                         props = {'key1': 'val1'})
    self.data_set1_js = ('{\n  "DataSet": [\n    '
                         '{\n      "x": [\n        1, \n        2\n      ]\n    }, \n    '
                         '{\n      "y": [\n        3, \n        4\n      ]\n    }, \n    '
                         '{\n      "props": {\n        "key1": "val1"\n      }\n    }\n  ]\n}')

  def test_data_set_to_jss(self):
    data_set1 = self.data_set1
    data_set1_js_gt = self.data_set1_js
    data_set1_js = data.data_set_to_jss(data_set1)
    self.assertEqual(data_set1_js, data_set1_js_gt)

  def test_jss_to_data_set(self):
    data_set1_gt = self.data_set1
    data_set1_js = self.data_set1_js
    data_set1 = data.jss_to_data_set(data_set1_js)
    np.testing.assert_array_equal(data_set1.x, data_set1_gt.x)
    np.testing.assert_array_equal(data_set1.y, data_set1_gt.y)
    self.assertEqual(data_set1_gt.props, data_set1.props)



if __name__ == '__main__':
  unittest.main()
