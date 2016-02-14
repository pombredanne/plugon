#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'Ertuğrul Keremoğlu'


from distutils.core import setup


setup(

    name = 'Plugon',
    version = '1.0',
    description = 'Lightweight and simple loop engine.',

    author = 'Ertuğrul Keremoğlu',
    author_email = 'ertugkeremoglu@gmail.com',
    url = 'https://github.com/ertugrulkeremoglu/',

    classifiers = [
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ],

    packages = [
        'plugon',
    ],

)
