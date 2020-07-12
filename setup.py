# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='stock_screener_fastapi_model',
    version='0.0.1',
    description='Demo Model for Testing FastAPI',
    long_description=readme,
    author='Amruth VVKP',
    author_email='amruthvvkp@gmail.com',
    url='https://github.com/amruthvvkp/stock_screener_fastapi',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

