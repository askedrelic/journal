from setuptools import setup, find_packages                                                                                                                                                      
import journal

setup(
name         = 'journal',
version      = journal.__version__,
author       = journal.__author__,
author_email = 'askedrelic@gmail.com',

description      = 'Simple CLI tool to assist in keeping a journal for work or personal reasons',
long_description = open('README.markdown').read(),

url              = 'https://github.com/askedrelic/journal',

packages         = find_packages(),
test_suite       = 'tests',
entry_points     = """
[console_scripts]
journal = journal.main:main"""
)

