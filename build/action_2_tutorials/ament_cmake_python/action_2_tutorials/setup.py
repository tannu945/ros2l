from setuptools import find_packages
from setuptools import setup

setup(
    name='action_2_tutorials',
    version='0.0.0',
    packages=find_packages(
        include=('action_2_tutorials', 'action_2_tutorials.*')),
)
