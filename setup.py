#!/usr/bin/env python3
#
# pydictor setup
#
# date: Mar 1 2021
# Maintainer: glozanoa <glozanoa@uni.pe>


from setuptools import setup, find_packages
#from ama.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()


setup(
    name='pydictor',
    version=VERSION,
    description='A powerful and useful hacker dictionary builder for a brute-force attack',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    maintainer='glozanoa',
    maintainer_email='glozanoa@uni.pe',
    url='https://github.com/fpolit/pydictor',
    license='GPL3',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts':[
            'pydictor = pydictor.pydictor:main',
        ],
    }
)
