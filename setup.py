from setuptools import setup, find_packages
import sys
import journal

required = []

if sys.version_info[:2] < (2,6):
    required.append('argparse')

setup(
name         = 'journal',
version      = journal.__version__,
author       = journal.__author__,
author_email = 'askedrelic@gmail.com',

description      = 'Simple CLI tool to help with keeping a work/personal journal',
long_description = open('README.markdown').read(),

url              = 'https://github.com/askedrelic/journal',

packages         = find_packages(),
entry_points     = """
[console_scripts]
journal = journal.main:main""",
test_suite       = 'tests',

install_requires = required,
)

