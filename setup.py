# -*- coding: utf-8 -*-

import os

from setuptools import setup
from setuptools import find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name='starzel.bob_hooks',
    version='0.1.dev0',
    description='Hooks for mr.bob',
    long_description=read('README.rst') +
                     read('HISTORY.rst') +
                     read('LICENSE'),
    classifiers=[
        "Programming Language :: Python",
    ],
    author='Patrick Gerken',
    author_email='gerken@starzel.de',
    url='https://github.com/starzel/starzel.bob_hooks',
    license='BSD',
    packages=find_packages(),
    install_requires=[
        'mr.bob',
        'setuptools',
    ],
    extras_require={
        'test': [
            'nose',
            'nose-selecttests',
            'coverage',
            'unittest2',
            'flake8',
        ],
        'development': [
            'zest.releaser',
            'check-manifest',
        ],
    },
    entry_points="""
    """,
    include_package_data=True,
    zip_safe=False,
)
