import os
from setuptools import setup, find_packages

from timeseries_service.version import VERSION


def read_requirements(file_name):
    cwd = os.path.abspath(
            os.path.dirname(__file__)
    )
    requirements = []
    with open(os.path.join(cwd, file_name), encoding="utf-8") as file:
        requirements = [requirement.strip() for requirement in file.readlines()]

    return requirements


setup(
    name="timeseries_service",
    version=VERSION,
    packages=find_packages(exclude=[
        "*.tests", "*.tests.*", "tests.*", "tests"
    ]),
    install_requires=read_requirements("requirements.txt"),
    include_package_data=True,
    author="MB",
    tests_require=read_requirements("requirements-dev.txt")
)
