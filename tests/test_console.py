#!/usr/bin/python3
"""
Unittest - For test console AirBnB 
"""
import unittest
import os
import json
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel

class TestConsole(unittest.TestCase):
    """ Class designed for test """

    @classmethod
    def setUpClass(self):
        """Setting of test"""
        self.typing = console.HBNBCommand()
"""
    @classmethod
    def tearDownClass(self):
        """ Remove file.json temp """
        try:
            os.remove("file.json")
        except:
            pass
"""

   """Check for docstring existance"""
    def test_docstrings_in_console(self):
                self.assertTrue(len(console.__doc__) >= 1)test_console.py"""
        self.assertTrue(len(self.__doc__) 


    """Test command interpreter outputs"""

if __name__ == "__main__":
    unittest.main()
