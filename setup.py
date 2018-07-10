# 
#  Author: Rongyang Sun <sun-rongyang@outlook.com>
#  Creation Date: 2018-07-07 09:16
#  
#  Description: alpskit project. Setup configuration file.
# 
from setuptools.command.install import install
from setuptools import setup


setup(
  name = 'alpskit',
  version = '0.0.1',
  description = 'Python toolkit for ALPS library.',
  author = 'Rongyang Sun',
  packages = ['alpskit'],
  package_dir = {'': 'src'},
  test_suite = 'tests',
  zip_safe = False,
)
