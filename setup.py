#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# HFOS - Hackerfleet Operating System
# ===================================
# Copyright (C) 2011-2019 Heiko 'riot' Weinen <riot@c-base.org> and others.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

__author__ = "Heiko 'riot' Weinen"
__license__ = "AGPLv3"

from setuptools import setup, find_packages

setup(
    name="hfos-dev",
    version="0.0.1",
    description="hfos-dev",
    author="Hackerfleet Community",
    author_email="riot@c-base.org",
    url="https://github.com/hackerfleet/hfos-dev",
    license="GNU Affero General Public License v3",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Isomer :: 1',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Utilities'
    ],
    packages=find_packages(),
    long_description="""HFOS - Dev
==========

HFOS module development system

This package a few modules to debug others, as well as the core system.
""",
    dependency_links=[],
    install_requires=[
        'isomer>=1.0.0',
    ],
    entry_points="""[isomer.components]
    recorder=isomer.misc.recorder:Recorder
    playback=isomer.misc.playback:Playback
    navdatasim=isomer.misc.navdatasim:NavdataSim
    vesselsim=isomer.misc.vesselsim:VesselSim
    """,
    test_suite="tests.main.main",
)
