"""
pip3 install pytest-html
py, pytest, pytest-html

Command: py.test filename --html=report.html
"""

import unittest
from F4_test_class1 import TestClass1
from F5_test_class2 import TestClass2

# Get all tests from TestClass1 and TestClass2
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestClass1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestClass2)

# Create a test suite combining TestClass1 and TestClass2
smokeTests = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTests)