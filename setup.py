#!/usr/bin/env python

from sys import version_info as version
from setuptools import setup, find_packages


exclude = ["docs", "tests"]

if version.major < 3 or (version.major == 3 and version.minor < 4):
    exclude += ["rafty.server"]
    entry_points = {}
else:
    entry_points = {"console_scripts": ["raftyd=rafty.server.main:run"]}

setup(
    name="rafty",
    version="1.0",
    description="Implementation of the Raft algorithm for distributed consensus",
    author="Sagnik Chatterjee",
    author_email="sagnik.chatterjee51@gmail.com",
    url="https://github.com/sagnik-chatterjee/rafty",
    license="MIT",
    keywords="distributed consensus raft",
    classifiers=[
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Distributed Systems :: Consens Algorithms",
        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # "Programming Language :: Python :: 2",
        # "Programming Language :: Python :: 2.7",
        # "Programming Language :: Python :: 3",
        # "Programming Language :: Python :: 3.3",
        # "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.9",
    ],
    # packages = ['rafty.client'],
    packages=find_packages(exclude=exclude),
    install_requires=["msgpack-python"],
    entry_points=entry_points,
)
