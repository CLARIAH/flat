#! /usr/bin/env python3
# -*- coding: utf8 -*-

from __future__ import print_function

import os
import sys
from setuptools import setup


try:
   os.chdir(os.path.dirname(sys.argv[0]))
except:
   pass


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Flat",
    version = "0.2",
    author = "Maarten van Gompel",
    author_email = "proycon@anaproy.nl",
    description = ("Flat is a web-based linguistic annotation environment based around the FoLiA format (http://proycon.github.io/folia), a rich XML-based format for linguistic annotation. Flat allows users to view annotated FoLiA documents and enrich these documents with new annotations, a wide variety of linguistic annotation types is supported through the FoLiA paradigm."),
    license = "GPL",
    keywords = "flat linguistic annotation nlp computationa_linguistics folia annotator web",
    url = "https://github.com/proycon/flat",
    packages=['flat','flat.modes','flat.modes.structureeditor','flat.modes.viewer','flat.modes.editor','flat.users'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Text Processing :: Linguistic",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Operating System :: POSIX",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    package_data = {'flat':['templates'], 'flat.modes.structureeditor':['templates'],  'flat.modes.viewer':['templates'], 'flat.modes.editor':['templates'] },
    install_requires=['lxml >= 2.2','pynlpl >= 0.7.0','foliadocserve >= 0.2','Django >= 1.5']
)