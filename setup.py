#!/usr/bin/env python

from setuptools import setup

setup(name='PPMSplot',
      version='1.0',
      description='Plot PPMS dat files',
      author='Matt Griffiths',
      author_email='griff@me3d.com.au',
      packages=['PPMSplot'],
	  entry_points = {
	  	'console_scripts': ['PPMSplot=PPMSplot.__main__:main'],
	  }
)
