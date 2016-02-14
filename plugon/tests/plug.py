#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'Ertuğrul Keremoğlu'


import unittest
from plugon.plug import Plug


def example_function(*args, **kwargs):
    pass


class TestPlug(unittest.TestCase):

    def test_plug_name(self):

        example_function_plug = Plug(example_function)

        self.assertEqual(example_function_plug.name, example_function.__name__)


    def test_plug_default_variables(self):

        example_function_plug = Plug(example_function)

        self.assertEqual(example_function_plug.name, example_function.__name__)
        self.assertEqual(example_function_plug.urgency, 10)
        self.assertEqual(example_function_plug.repeatable, True)


    def test_plug_changed_variables(self):
        
        example_function_plug = Plug(example_function)
        example_function_plug.urgency = 1
        example_function_plug.repeatable = False

        self.assertEqual(example_function_plug.urgency, 1)
        self.assertEqual(example_function_plug.repeatable, False)


    def test_plug_initial_variables(self):

        example_function_plug = Plug(
                example_function,
                urgency = 5,
                repeatable = False,
                disabled = True
        )

        self.assertEqual(example_function_plug.urgency, 5)
        self.assertEqual(example_function_plug.repeatable, False)
        self.assertEqual(example_function_plug.disabled, True)


if __name__ == '__main__':
    unittest.main()
