#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

import setuptools


__version__, = re.findall(
    '__version__ = "(.*)"', open("src/plattus/__init__.py").read()
)

with open("README.md", "r") as fh:
    long_description = fh.read()

INSTALL_REQUIRES = ["lark-parser"]
EXTRAS_REQUIRE = {
    "docs": [],
    "tests": ["coverage", "hypothesis", "pytest", "six", "pytest-benchmark"],
}
EXTRAS_REQUIRE["dev"] = (
    EXTRAS_REQUIRE["tests"] + EXTRAS_REQUIRE["docs"] + ["pre-commit"]
)


setuptools.setup(
    name="plattus",
    version=__version__,
    author="Stéphane Boisson",
    author_email="sboisson@gmail.com",
    description="A pythonic FlatBuffers library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["flatbuffers"],
    url="https://github.com/sboisson/plattus",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Pre-processors",
        "Topic :: Software Development :: Code Generators",
    ],
    install_requires=INSTALL_REQUIRES,
    setup_requires=["pytest-runner"],
    tests_require=EXTRAS_REQUIRE["tests"],
    extras_require=EXTRAS_REQUIRE,
    zip_safe=False,
    package_data={"": ["*.lark"]},
)
