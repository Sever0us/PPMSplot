#!/usr/bin/env python

from setuptools import setup

setup(name='PPMSplot',
      version='1.0',
      description='Plot PPMS dat files',
      author='Matt Griffiths',
      author_email='griff@me3d.com.au',
      install_requires=['matplotlib'],
      lisence='MIT',
      packages=['PPMSplot'],
	  entry_points = {
	  	'console_scripts': [
                  'PPMSplot=PPMSplot.__main__:main',
                  'PPMSconfig=PPMSplot.generate_config.__main__:main'
            ]
	  }
)
