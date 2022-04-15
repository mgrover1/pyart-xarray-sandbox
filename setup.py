#!/usr/bin/env python3

"""The setup script."""

from setuptools import find_packages, setup

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

with open('README.md') as f:
    long_description = f.read()


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Topic :: Scientific/Engineering',
]

setup(
    name='xradar',
    description='A lightweight interface for working with the Weather Research and Forecasting (WRF) model output in Xarray.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.7',
    maintainer='ARM Development Team',
    maintainer_email='mgrover@anl.gov',
    classifiers=CLASSIFIERS,
    url='https://xradar.readthedocs.io',
    project_urls={
        'Documentation': 'https://xradar.readthedocs.io',
        'Source': 'https://github.com/mgrover1/pyart-xarray-sandbox',
        'Tracker': 'https://github.com/mgrover1/pyart-xarray-sandbox/issues',
        'Discussions/Support': 'https://github.com/mgrover1/pyart-xarray-sandbox/discussions',
    },
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    install_requires=install_requires,
    license='Apache 2.0',
    zip_safe=False,
    entry_points={},
    keywords='pyart, xarray',
    use_scm_version={'version_scheme': 'post-release', 'local_scheme': 'dirty-tag'},
)