# coding: utf-8
# Copyright (C) 2015 Mark Ma
# Author: Mark Ma <maanyng@yahoo.com.tw>
# License: MIT
# For license information, see LICENSE.TXT

"""
  The nester_pre is an open source Python library for nested data processing. 
  It provided a function to print item of list, whether list is nested or not.
"""


# Copyright notice
__copyright__ = "MIT"

# Maintainer
__maintainer__ = "Mark Ma"
__maintainer_email__ = "maanyng@yahoo.com.tw"
__author__ = __maintainer__
__author_email__ = __maintainer_email__


try:
    #from .file import a_function, b_function
    from .nester_pre import print_lol
    from .nester_pre_version import __version__

except ImportError as e:
    print('Could not import module.: '+ str(e))
