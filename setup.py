#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="_",
    version='0',
    description="Various utils",
    author="Florian Mounier",
    author_email="paradoxxx.zero@gmail.com",
    packages=find_packages(),
    platforms="Any",
    provides=['_'],
    tests_require=["pytest"],
    use_2to3=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"])
