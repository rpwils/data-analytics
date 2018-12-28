#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
description: setup script for the tidals package
created: 2018-10-01
author: Ed Nykaza
license: BSD-2-Clause
Parts of this file were taken from
https://packaging.python.org/tutorials/packaging-projects/
"""

# %% REQUIRED LIBRARIES
import setuptools
import os
import glob
import shutil


# %% START OF SETUP
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tidals",
    version="0.0.1",
    author="Ed Nykaza",
    author_email="ed@tidepool.org",
    description="Tidepool Data Analysis Tools",
    long_description="Tidepool Data Analysis Data Pipeline functions used to load and clean data ",
    long_description_content_type="text/markdown",
    url="https://github.com/rpwils/data-analytics/blob/master/tidepool-analysis-tools",
    packages=setuptools.find_packages(),
    download_url="https://github.com/rpwils/data-analytics/archive/v0.0.1.tar.gz",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD-2-Clause',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
          'numpy>=1.14.1',
          'pandas>=0.23.1',
      ],
)


# %% CLEAN UP
# remove the excess files if package is installed with pip from github
# TODO: make tidals its own repository under tidepool_org
# once tidals becomes its own github repository, then this step will no longer be necessary
# TODO: publish tidals as a PyPi pacakge

files = glob.glob(os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "*")))

hidFiles = glob.glob(os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", ".*")))

allFiles = files + hidFiles

# if loaded from github with pip in environmental.yml, then when it will
# create a source file (src) and clone the entire data-analytics repo
for i in allFiles:
    # make sure you are in the src/tidals/ directory
    if "src" in i.split(sep=os.sep)[-3]:
        # delete all BUT files in tidals package
        if "tidepool-analysis-tools" not in i:
            if os.path.isdir(i):
                shutil.rmtree(i)
            else:
                os.remove(i)
