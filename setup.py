import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plattus",
    version="0.0.1",
    author="Stéphane Boisson",
    author_email="sboisson@gmail.com",
    description="A pythonic FlatBuffers library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sboisson/plattus",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Pre-processors",
        "Topic :: Software Development :: Code Generators",
    ],
)
