from distutils.core import setup
from setuptools import find_packages

with open("README.md") as fh:
    long_description = fh.read()

VERSION = "3.0a3"

setup(
    name='blitzdb3',
    version=VERSION,
    author='Stefane Fermigier - Abilian',
    author_email='sf@abilian.com',
    description='A document-oriented database written purely in Python (Python 3 fork).',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url='https://github.com/abilian/blitzdb3',
    packages=find_packages(),
    install_requires=['six'],
    zip_safe=False,
)
