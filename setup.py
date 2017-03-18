from setuptools import setup

install_requires = [
    'nose',
    'tox',
]

setup(
    name = "demo",
    version = "0.0.1",
    description = ("A demonstration of the problem"),
    install_requires = install_requires
)
