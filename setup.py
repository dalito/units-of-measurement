from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(here + "/README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

install_requires = ["lark-parser", "rdflib"]

test_requires = ["pytest"]

setup(
    name="units-of-measurement",
    description="URLs and ID mappings for UCUM codes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.0.1",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=install_requires,
    setup_requires=["pytest-runner"],
    tests_require=test_requires,
    test_suite="pytest",
    packages=find_packages(exclude="tests"),
    entry_points={"console_scripts": ["uom=units_of_measurement.cli:main"]},
    package_data={"units_of_measurement": ["resources/*.csv"]}
)
