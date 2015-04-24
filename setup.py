#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="openstack_cors",
    version="1.0.0",
    install_requires = [
        "webob",
    ],
    packages = find_packages(),
    )
