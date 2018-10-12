"""
Copyright (c) 2018, Jairus Martin.

Distributed under the terms of the MIT License.

The full license is in the file LICENSE, distributed with this software.

Created on Jun 19, 2018

@author: jrm
"""
from setuptools import setup, find_packages

setup(
    name='materialize-ui',
    version='0.1.9',
    author='CodeLV',
    author_email='frmdstryr@protonmail.com',
    url='https://github.com/frmdstryr/materialize',
    description='Materailzie web components for enaml-web',
    license="MIT",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=['enaml-web'],
    packages=find_packages(),
    package_data={
        'materialize': ['*.enaml'],
    }
)
