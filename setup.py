#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os
import re


ROOT = os.path.dirname(__file__)
with open(os.path.join(ROOT, 'cutter', '__init__.py')) as fd:
    __version__ = re.search("__version__ = '([^']+)'", fd.read()).group(1)

setup(
    name="cutter",
    version=__version__,
    description="Python list cutter tool",
    author="Florian Mounier",
    author_email="paradoxxx.zero@gmail.com",
    packages=find_packages(),
    platforms="Any",
    provides=['cutter'],
    tests_require=["pytest"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"])
