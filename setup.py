#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'Ertuğrul Keremoğlu'


from distutils.core import setup


setup(

    name = 'Plugon',
    version = '1.0',
    keywords = 'loop engine',
    description = 'Lightweight and simple loop engine.',
    long_description = 'Plugon is a lightweight and simple loop engine which is made for building efficient and clean architecture for applications such as servers, clients, bots, etc.',
    license = 'MIT',

    author = 'Ertuğrul Keremoğlu',
    author_email = 'ertugkeremoglu@gmail.com',
    url = 'https://github.com/ertugrulkeremoglu/plugon/',

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
    ],

    packages = [
        'plugon',
    ],

)
