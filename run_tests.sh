#!/bin/bash
#
# Author: Rongyang Sun <sun-rongyang@outlook.com>
# Creation Date: 2018-07-09 21:10
# 
# Description: alpskit project. Bash script to run unit tests.
#
ROOTPATH="$(pwd)"
SRCPATH="${ROOTPATH}/src"
UT_PYTHON_SCRIPT="run_tests.py"


cd ${SRCPATH}
alpspython ${UT_PYTHON_SCRIPT}
cd ${ROOTPATH}
