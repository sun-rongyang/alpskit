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
