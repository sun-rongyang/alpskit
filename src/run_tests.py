# 
#  Author: Rongyang Sun <sun-rongyang@outlook.com>
#  Creation Date: 2018-07-09 21:16
#  
#  Description: alpskit project. Python script to run unit tests.
# 
import unittest


loader = unittest.TestLoader()
start_dir = './tests/ut_alpskit'
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner()
runner.run(suite)
