# Copyright (c) 2014, Santiago Videla
#
# This file is part of pyzcasp.
#
# caspo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# caspo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with caspo.  If not, see <http://www.gnu.org/licenses/>.
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import sys, os

version = '1.0.1'

long_desc = """
This package provides a framework to build on top of Answer Set Programming tools using the Zope Component Architecture.
For more details on available features and usage, visit the `GitHub repository`_.

.. _`github repository`: http://github.com/svidela/pyzcasp

"""
setup(name='pyzcasp',
      version=version,
      description="Python + Zope Component Architecture framework for Answer Set Programming",
      long_description=long_desc + open('CHANGES').read(),
      classifiers=[
          "Intended Audience :: Science/Research",
          "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 2.7",
          "Topic :: Scientific/Engineering :: Artificial Intelligence"
      ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Santiago Videla',
      author_email='santiago.videla@gmail.com',
      url='http://github.com/svidela/pyzcasp',
      license='GPLv3+',
      packages=find_packages(exclude=['ez_setup', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "pyparsing>=1.5.7,<2.0.0", #latest pyparsing version for Python 2.x
          "zope.component",
          "zope.interface"
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
