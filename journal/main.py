#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
from os import path, makedirs
from datetime import datetime

from journal import __version__

JOURNAL_DEST = ".journal"

def parse_args():
    #parsing
    parser = argparse.ArgumentParser(
            description='Simple CLI tool to help with keeping a work/personal journal',
            version=__version__)
    parser.add_argument('entry',
            action="store",
            help="Text to make an entry in your journal")
    return parser, parser.parse_args()

def check_journal_dest():
    journal_dir = path.expanduser("~/" + JOURNAL_DEST)
    if not path.exists(journal_dir):
        makedirs(journal_dir)

def record_entry(entry):
    check_journal_dest()
    current_date = datetime.today()
    update_date = current_date.strftime("%a %I:%M:%S %Y-%m-%d")
    entry = update_date + "\n-" + entry + "\n\n"
    with open(build_journal_path(current_date), "a") as date_file:
        date_file.write(entry)

def build_journal_path(date):
    date_filename = path.expanduser("".join(
        [ "~/", JOURNAL_DEST, '/', date.strftime("%Y.%m.%d"), ".txt"]
        ))
    return date_filename

def show_today():
    current_date = datetime.today()
    return show_entry(current_date)

def show_entry(date):
    """
    args
    date - datetime object
    returns entry text or None if entry doesn't exist
    """
    try:
        with open(build_journal_path(date), "r") as entry_file:
            return entry_file.read()
    except IOError:
        return None

def main():
    #parse args
    parser, args = parse_args()

    if not str.strip(args.entry):
        parser.print_help()
        sys.exit()
    elif args.entry == 'today':
        entry = show_today()
        if entry:
            print entry
        else:
            print "journal: error: entry not found on that date"
            sys.exit()
    else:
        record_entry(args.entry)

if __name__ == "__main__":
    main()
