#Journal

Journal is a Python command line tool to help with keeping a journal for work,
personal, or any reason really!  Inspired by Peter Lyons'
[article](http://peterlyons.com/leveling_up.html) on career development, my own
experiences, and too much free time.

Requires

* Python (Tested on Python 2.5, 2.6, 2.7)

Related:

* [Blog post about Journal](http://asktherelic.com/2011/08/16/journaling/)

#Installation

    pip install journal

The `journal` command should now be available on your command line.

#Usage

It's as simple as:

    $ journal "Task foo completed"

and a `~/.journal/[CURRENT DATE].txt` file will be created using the current
date, with a timestamp and your entry. Just continue to enter your tasks
through the days and weeks and build a record of your work.
