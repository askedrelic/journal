#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
journal
Copyright (c) 2011 Matt Behrens <askedrelic@gmail.com>
http://asktherelic.com

A CLI tool to help with keeping a datetime organized journal

Licensing included in LICENSE.txt
"""

#py2.5 compatibility
from __future__ import with_statement

import sys
from os import path, makedirs
import argparse
import string
import datetime
import ConfigParser

from journal import __version__, parse

DEFAULT_JOURNAL = "~/.journal"
DEFAULT_JOURNAL_RC = "~/.journalrc"

def parse_args():
    #parsing
    description = 'A CLI tool to help with keeping a datetime organized journal'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--version', action="version", version=__version__)
    parser.add_argument('-c', '--config',
            action="store",
            dest="config_file",
            nargs="?",
            help="")
    parser.add_argument('-j', '--journal',
            action="store",
            dest="journal",
            nargs="?",
            help="")
    parser.add_argument('-l', '--location',
            action="store",
            dest="location",
            nargs="?",
            help="")

    date_group = parser.add_mutually_exclusive_group()
    date_group.add_argument('-s', '--since',
            action="store",
            dest="since",
            nargs="?",
            help="show all journal entries since a date [SINCE]")
    date_group.add_argument('-v', '--view',
            action="store",
            dest="view",
            nargs="?",
            help="view all journal entries on a specific date [VIEW]")

    parser.add_argument('entry',
            nargs="*",
            help="Text to make an entry in your journal")
    return parser, parser.parse_args()

def parse_config(args):
    """
    Parse existing config for journal location
    Otherwise, return default location

    Returns journal location
    """
    # Use config file if provided
    if args.config_file:
        config_file = args.config_file
    else:
        config_file = DEFAULT_JOURNAL_RC

    config_path = path.expanduser(config_file)
    if not path.exists(config_path):
        # Complain if they provided non-existant config
        if config_file != DEFAULT_JOURNAL_RC:
            print "journal: error: config file '" + config_file + "' not found"
            sys.exit()
        else:
            # If no config file, use default journal location
            return DEFAULT_JOURNAL

    config = ConfigParser.SafeConfigParser({
        'journal':{'default':'__journal'},
        '__journal':{'location':DEFAULT_JOURNAL}
    })
    config.read(config_path)

    journal_location = config.get(config.get('journal', 'default'), 'location');
    if args.journal:
        journal_location = config.get(args.journal, 'location');
    return journal_location

def check_journal_dest(location):
    journal_dir = path.expanduser(location)
    if not path.exists(journal_dir):
        try:
            makedirs(journal_dir)
        except:
            print "journal: error: creating journal storage directory failed"
            sys.exit()

def record_entries(journal_location, entries):
    """
    args
    entry - list of entries to record
    """
    check_journal_dest(journal_location)
    current_date = datetime.datetime.today()
    date_header = current_date.strftime("%a %I:%M:%S %Y-%m-%d") + "\n"
    with open(build_journal_path(journal_location, current_date), "a") as date_file:
        entry_output = date_header
        for entry in entries:
            entry_output += "-" + entry + "\n"
        entry_output += "\n"
        date_file.write(entry_output)

def build_journal_path(journal_location, date):
    date_filename = path.expanduser("".join(
        [ journal_location, '/', date.strftime("%Y.%m.%d"), ".txt"]
        ))
    return date_filename

def get_entry(journal_location, date):
    """
    args
    date - date object
    returns entry text or None if entry doesn't exist
    """
    if not isinstance(date, datetime.date):
        return None
    try:
        with open(build_journal_path(journal_location, date), "r") as entry_file:
            return entry_file.read()
    except IOError:
        return None

def daterange(start_date, end_date):
    #loop over days + 1 for inclusive behavior
    for n in xrange((end_date - start_date).days + 1):
        yield start_date + datetime.timedelta(n)

def get_entries_since(journal_location, date):
    today = datetime.date.today()
    for single_date in daterange(date, today):
        entry = get_entry(journal_location, single_date)
        if entry:
            print entry

def main():
    #parse args
    parser, args = parse_args()
    journal_location = parse_config(args)
    date_parse = parse.Parse()

    #check args
    if args.location:
        journal_location = args.location
    check_journal_dest(journal_location)

    #TODO: better handle program exit flow through exceptions?
    #handle_args
    if args.view:
        date = date_parse.day(args.view)
        if not date:
            print "journal: error: unknown date format"
            sys.exit()

        entry = get_entry(journal_location, date)
        if entry:
            print entry
        else:
            print "journal: error: entry not found on date %s" % date
            sys.exit()
    elif args.since:
        date = date_parse.day(args.since)
        if not date:
            print "journal: error: unknown date format"
            sys.exit()
        get_entries_since(journal_location, date)
    else:
        # Cleanup/check for empty entry list
        entries = filter(string.strip, args.entry)
        if entries:
            record_entries(journal_location, entries)
        else:
            print "journal: error: missing entry"
            sys.exit()

if __name__ == "__main__":
    main()
