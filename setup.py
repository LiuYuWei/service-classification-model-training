"""This file is for setup information and version control used."""
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme_text = f.read()

with open('LICENSE') as f:
    license_text = f.read()

setup(
    project_name='service-ml-model-training-evaluation',
    project_version='0.0.4',
    description='In this project, we want to build the platform to train the classification model.',
    long_description=readme_text,
    author='Simon Liu',
    url='https://github.com/LiuYuWei/service-ml-model-training-evaluation',
    license=license_text,
    packages=find_packages(exclude=('tests'))
)
