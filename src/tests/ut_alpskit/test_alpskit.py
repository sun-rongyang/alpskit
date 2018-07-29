# 
#  Author: Rongyang Sun <sun-rongyang@outlook.com>
#  Creation Date: 2018-07-10 07:20
#  
#  Description: alpskit project. Unit test for functions and classes which
#               are imported directly to alpskit package.
# 
import unittest
import alpskit


class TestStringTools(unittest.TestCase):
  #  TODO: write the test # 
  def test_gen_basename(self):
    pass

  def test_get_basename(self):
    str1 = '../basename.suffix'
    self.assertEqual(alpskit.get_basename(str1),
                     'basename')
    str2 = './for/bar.baz.bax'
    self.assertEqual(alpskit.get_basename(str2, suffixs=2),
                     'bar')

  def test_get_folder(self):
    str1 = '../foo/bar/basename.suffix'
    folder = alpskit.get_folder(str1)
    self.assertEqual(folder, '../foo/bar')
    str2 = 'foo/bar.baz'
    self.assertEqual(alpskit.get_folder(str2),
                     'foo')
    str3 = 'foo.bar'
    self.assertEqual(alpskit.get_folder(str3), '.')

  def test_getlabel(self):
    measu_data1 = alpskit.MeasuData(props={'key1': 'val1', 'key2': 'val2'})
    keys = ['key1', 'key2']
    self.assertEqual(alpskit.getlabel(measu_data1, keys),
                     'key1=val1 key2=val2 ')

  #  TODO: write this test # 
  def test_get_fig_name(self):
    pass

  def test_basename2dict(self):
    basename1 = 'key1=1_key2=0.3_key3=1e-5_key4=str'
    dict1 = alpskit.basename2dict(basename1)
    self.assertEqual(dict1,
                     {'key1': 1,
                      'key2': 0.3,
                      'key3': 1e-5,
                      'key4': 'str'})
    basename2 = basename1 + '_suffix'
    dict2 = alpskit.basename2dict(basename2)
    self.assertEqual(dict2,
                     {'key1':   1,
                      'key2':   0.3,
                      'key3':   1e-5,
                      'key4':   'str',
                      'suffix': 'suffix'})

  def test_basename2jss(self):
    basename = 'key1=1_key2=0.3_key3=1e-5_key4=str'
    jss = alpskit.basename2jss(basename, 'props')
    self.assertEqual(jss,
        '{\n  "props": {\n    "key3": 1e-05, \n    "key2": 0.3, \n    "key1": 1, \n    "key4": "str"\n  }\n}')
