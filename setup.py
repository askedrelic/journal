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

description      = 'A CLI tool to help with keeping a datetime organized journal',
long_description = open('README.markdown').read(),

url              = 'https://github.com/askedrelic/journal',

packages         = find_packages(),
entry_points     = """
[console_scripts]
journal = journal.main:main""",
test_suite       = 'tests',

install_requires = required,

classifiers      = (
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.5',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    # 'Programming Language :: Python :: 3.0',
    # 'Programming Language :: Python :: 3.1',
),
)

