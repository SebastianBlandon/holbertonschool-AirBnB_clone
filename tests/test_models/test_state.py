#!/usr/bin/python3
""" Tests for State class """

import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """ Testing Method """

    def test_instances_of_State(self):
        """ Testing instances State """

        Model = State()

        self.assertTrue(hasattr(Model, "name"))

    def test_type_objects_State(self):
        """ Testing type onjects State """

        Model = State()

        self.assertIsInstance(Model, State)

        self.assertIsInstance(Model.name, str)

        self.assertTrue(issubclass(State, BaseModel))


if __name__ == '__main__':
    unittest.main()
