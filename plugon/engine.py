#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'Ertuğrul Keremoğlu'


from plugon.plug import Plug


class System():

    def __init__(self):
        self.plugs = list()


    def register(self, plug):

        if isinstance(plug, Plug):
            self.plugs.append(plug)

        else:
            raise TypeError('Object must be an instance of Plug')

        return plug


    def order_plugs_by_urgency(self):

        i = 0

        while i < len(self.plugs) - 1:

            j = 0
            i += 1

            while j < len(self.plugs) - 1:

                if self.plugs[j].urgency > self.plugs[j + 1].urgency:

                    temp = self.plugs[j + 1]
                    self.plugs[j + 1] = self.plugs[j]
                    self.plugs[j] = temp

                j += 1


    def run(self, loop_count = None):

        self.order_plugs_by_urgency()

        if loop_count is None:

            while True:

                for plug in self.plugs:
                    plug.run()

        else:

            for _ in range(loop_count):

                for plug in self.plugs:
                    plug.run()
