from setuptools import setup, find_packages

setup(
	name='jc_ActionsJH',
	version='1.0.0',
	description='This package contains a simple library for adding action/activity times and outputing their average times.',
	author='Jeffrey Hamlin',
	author_email='jeff.m.hamlin@gmail.com',
	url='https://github.com/jham20x6/turbo-octo-broccoli.git',
	license='MIT',
	install_requires=["simplejson>=3.16.0"]
	packages=find_packages(exclude=['*.test*'])
)	
