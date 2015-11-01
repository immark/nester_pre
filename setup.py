#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import nester_pre

setup(
    name = 'nester_pre',
    version = nester_pre.__version__,

    description = 'nester_pre let you print nestered data. i.e. nested list',
    long_description = open('README.rst').read(),

    author ='Mark Ma',
    author_email = 'maanyng@yahoo.com.tw',
    url = 'https://github.com/immark/nester_pre',

    license='MIT',
    platforms = 'any',
    classifiers = [
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    packages = find_packages(),

)
