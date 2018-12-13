# -*- coding: utf-8 -*-

# Learn more: https://github.com/yayakona

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='usedir',
    version='0.1.0',
    description='usedir package for Python-Guide.org',
    long_description=readme,
    author='yayakona',
    author_email='yayakona_pkmn@yahoo.co.jp',
    url='https://github.com/yayakona',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

