from setuptools import find_packages
from setuptools import setup

setup(
	name='jc_ActionsJH',
	version='1.0.0',
	description='This package contains a simple library for adding action/activity times and collecting their average times.',
	author='Jeffrey Hamlin',
	author_email='jeff.m.hamlin@gmail.com',
	url='https://github.com/jham20x6/turbo-octo-broccoli.git',
	packages=find_packages(exclude=['*.test*'])
)	
