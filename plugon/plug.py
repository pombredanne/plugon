#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'Ertuğrul Keremoğlu'


class Plug():

    def __init__(self, function, args = (), kwargs = {}, *initial_args, **initial_kwargs):

        self.name = function.__name__

        self.function = function
        self.args = args
        self.kwargs = kwargs

        self.urgency = int(initial_kwargs.get('urgency', 10))
        self.repeatable = bool(initial_kwargs.get('repeatable', True))
        self.repeat = initial_kwargs.get('repeat', None)
        self.disabled = bool(initial_kwargs.get('disabled', False))


    def run(self):

        if (self.disabled is False) and (self.repeat != 0):

            self.function(*self.args, **self.kwargs)

            if self.repeat is not None:
                self.repeat -= 1

            if self.repeatable is False:
                self.disabled = True
