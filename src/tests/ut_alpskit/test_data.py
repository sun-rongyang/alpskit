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


class TestGetDataFiles(unittest.TestCase):
  def setUp(self):
    def touch(fname, times=None):
      with open(fname, 'a'):
        os.utime(fname, times)
     
    self.case1 = './case1'
    self.chkp1 = self.case1 + '/case1.out.chkp'
    self.h51 = self.case1 + '/case1.out.h5'
    os.makedirs(self.chkp1)
    touch(self.h51)
    self.case2 = './case2'
    self.chkp21 = self.case2 + '/case2.out1.chkp'
    self.chkp22 = self.case2 + '/case2.out2.chkp'
    [os.mkdir(dir_) for dir_ in [self.case2,
                                 self.chkp21,
                                 self.chkp22]]

  def test_get_chkp_dirs(self):
    chkps = data.get_chkp_dirs(self.case1)
    self.assertEqual(chkps, [self.chkp1])
    chkps = data.get_chkp_dirs(self.case2)
    self.assertEqual(chkps, [self.chkp21, self.chkp22])

  def test_get_h5_files(self):
    h5 = data.get_h5_files(self.case1)
    self.assertEqual(h5, [self.h51])

  def tearDown(self):
    os.remove(self.h51)
    os.removedirs(self.chkp1)
    [os.removedirs(dir_) for dir_ in [self.chkp21, self.chkp22]]


if __name__ == '__main__':
  unittest.main()
