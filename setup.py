"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='csvdb',
    version='0.0.0',
    description='Manipulate a CSV file with ORM.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/andymememe/CSVDB',
    author='Andymememe',
    author_email='andymememe@gmail.com',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Topic
        'Intended Audience :: Developers',
        'Topic :: Database :: Front-Ends',

        # License
        'OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',

        # Support Python Version
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='development, csv, database',
    packages=find_packages(),
    python_requires='>=3.5, <4',
    project_urls={
        'Bug Reports': 'https://github.com/andymememe/CSVDB/issues',
        'Source': 'https://github.com/andymememe/CSVDB',
    },
)