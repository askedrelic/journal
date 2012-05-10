from setuptools import setup, find_packages
import sys
import journal

required = []

if sys.version_info[:2] < (2,6):
    required.append('argparse')

setup(
	name             = 'journal',
	version          = journal.__version__,
	description      = 'A CLI tool to help with keeping a work/personal journal',
	long_description = open('README.markdown').read() + '\n\n' + open('HISTORY.markdown').read(),

	author           = journal.__author__,
	author_email     = 'askedrelic@gmail.com',
	url              = 'https://github.com/askedrelic/journal',
    license          = open("LICENSE.txt").read(),

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
	),
)

