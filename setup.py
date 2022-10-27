#!/usr/bin/python
"""
Instalation setup of CarStats
"""
import os
from setuptools import setup, find_packages


def read(fname):
    """set up path"""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


with open("requirements.txt") as f:
    reqs = f.read().splitlines()

setup(
    name="CarStats",
    version="0.0.1",
    author="Artur Nowak",
    keywords="Carstats, car statistic",
    long_description=read("README.md"),
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=reqs,
    python_requires=">=3.8, <3.9",
    classifiers=[
        "Development Status :: 1 - Pre-alpha",
        "Environment :: Console",
        "Intended Audience :: Cars Lovers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: UNIX :: Linux",
        "Programming Language :: Python :: 3",
    ],
)
