#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from datetime import datetime
from os import path

def parse_args():
    #parsing
    parser = argparse.ArgumentParser(description='Journal some stuff', version='0.1')
    parser.add_argument('message', action="store", help="message")

    args = parser.parse_args()
    return args

def record_message(message):
    message_type = ".journal"

    current_date = datetime.today()
    update_date = current_date.strftime("%a %I:%M:%S %Y-%m-%d")
    message = update_date + "\n-" + message + "\n\n"
    date_filename = path.expanduser("".join([
            "~/",
            message_type,
            '/',
            current_date.strftime("%Y.%m.%d"),
            ".txt"]))
    with open(date_filename, "a") as date_file:
        date_file.write(message)

def main():
    #parse args
    args = parse_args()
    #print args.message
    record_message(args.message)

if __name__ == "__main__":
    main()
