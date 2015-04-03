#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages

setup(name         = "passwdk",
      description  = "Simple console password manager using json as backend",
      url          = "https://github.com/lkrotowski/passwdk",
      version      = "0.2.0",
      packages     = find_packages("src"),
      package_dir  = {"": "src"},
      entry_points = {"console_scripts": ["passwdk=passwdk.main:main"]},
      author       = "Łukasz Krotowski",
      author_email = "lukasz.krotowski@gmail.com",
      license      = "GPLv3",
      classifiers  = ["Development Status :: 3 - Alpha",
                      "Environment :: Console",
                      "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                      "Operating System :: POSIX :: Linux",
                      "Topic :: Utilities"])
