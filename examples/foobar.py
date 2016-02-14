#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import print_function


__author__ = 'Ertuğrul Keremoğlu'


from plugon import System, Plug


class Application(System):

    def __init__(self, name, *args, **kwargs):

        self.name = name

        super(Application, self).__init__(*args, **kwargs)

        self.register(
            plug = Plug(self.foo, urgency = 2),
        )

        self.register(
            plug = Plug(self.bar, urgency = 3, repeat = 2),
        )

        self.register(
            plug = Plug(self.initial, urgency = 1, repeatable = False),
        )


    def initial(self):
        print("{app_name} is running...".format(
            app_name = self.name,
        ))

    def foo(self):
        print('foo')


    def bar(self):
        print('bar')


if __name__ == '__main__':

    application = Application('FooBar')
    application.run(4)
