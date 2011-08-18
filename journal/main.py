#!/usr/bin/env python
# -*- coding: utf-8 -*-

#py2.5 compatibility
from __future__ import with_statement

import sys
from os import path, makedirs
import argparse
from datetime import datetime

from journal import __version__

JOURNAL_DEST = ".journal"

def parse_args():
    #parsing
    parser = argparse.ArgumentParser(description='Simple CLI tool to help with keeping a work/personal journal')
    parser.add_argument('-v', '--version',
            action="version",
            version=__version__,
            help="show program's version number and exit")
    parser.add_argument('entry',
            nargs="+",
            help="Text to make an entry in your journal")
    return parser, parser.parse_args()

def check_journal_dest():
    journal_dir = path.expanduser("~/" + JOURNAL_DEST)
    if not path.exists(journal_dir):
        try:
            makedirs(journal_dir)
        except:
            print "journal: error: creating journal storage directory failed"
            sys.exit()

def record_entries(entries):
    """
    args
    entry - list of entries to record
    """
    check_journal_dest()
    current_date = datetime.today()
    date_header = current_date.strftime("%a %I:%M:%S %Y-%m-%d") + "\n"
    with open(build_journal_path(current_date), "a") as date_file:
        entry_output = date_header
        for entry in entries:
            entry_output += "-" + entry + "\n"
        entry_output += "\n"
        date_file.write(entry_output)

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

    record_entries(args.entry)

    #check args
    #if not str.strip(args.entry):
        #parser.print_help()
        #sys.exit()
    #elif args.entry == 'today':
        #entry = show_today()
        #if entry:
            #print entry
        #else:
            #print "journal: error: entry not found on that date"
            #sys.exit()
    #else:
        #record_entry(args.entry)

if __name__ == "__main__":
    main()
