from setuptools import setup, find_packages
import sys, os

version = '0.1dev'

setup(name='pyzcasp',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Santiago Videla',
      author_email='santiago.videla@gmail.com',
      url='',
      license='gpl3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "ply",
          "zope.component",
          "zope.interface"
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )