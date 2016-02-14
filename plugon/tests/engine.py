#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'Ertuğrul Keremoğlu'


import unittest

from plugon.plug import Plug
from plugon.engine import System


def example_function(*args, **kwargs):
    pass


class TestSystem(unittest.TestCase):

    def test_register_plug(self):

        system = System()
        registered_plug = system.register(
                plug = Plug(example_function, ['1', '2', '3'], sample = 'data'),
        )

        self.assertIsInstance(registered_plug, Plug)

        with self.assertRaises(TypeError):
            system.register(dict())


    def test_order_plugs_by_urgency(self):

        system = System()

        third_plug = system.register(
            plug = Plug(example_function, 'third', 'plug', urgency = 3),
        )

        first_plug = system.register(
            plug = Plug(example_function, 'first', 'plug', urgency = 1),
        )

        second_plug = system.register(
            plug = Plug(example_function, 'second', 'plug', urgency = 2),
        )

        system.order_plugs_by_urgency()

        self.assertEqual(system.plugs[0].urgency, first_plug.urgency)
        self.assertEqual(system.plugs[1].urgency, second_plug.urgency)
        self.assertEqual(system.plugs[2].urgency, third_plug.urgency)


if __name__ == '__main__':
    unittest.main()
