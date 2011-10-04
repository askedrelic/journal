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

The API for viewing and listing previous entries is currently a WIP, but you
should be able to view specific entries for a day by using the flag `--view`. Short
tags work with these dates.

    $ journal --view "yesterday"
    $ journal --view "12 days ago"
    $ journal --view "8/14"

    # Easiest way to view today (t)
    $ journal -vt

    # Easiest way to view yesterday (y)
    $ journal -vy

You can view all entries since a specific previous date, using the flag
`--since`. This is sparse output, dates without entries will be skipped quietly.

    $ journal --since "yesterday"
    $ journal --since "7 days ago"

#Advanced usage

In the simplest for described above, journal entries are stored in ~/.journal.
By providing the `--location|-l path` command line switch entries will be read
from & written to the provided directory.  This functionality is useful for
having journals dealing with separate domains:

    $ journal -l ~/.work "Got all of the monies"
    $ journal -l ~/.home "Spent all the monies"

See below for using a `.journalrc` to define these journals & storage locations.

#Configuration

You can create a `.journalrc` file (or one specified with the `-c` switch) to
define journal directories:

    [journal]
    default: work

    [home]
    location: ~/Dropbox/journals/home

    [work]
    location: ~/Dropbox/journals/work

With journals defined as such, you can use the `--journal|-j name` switch to
choose which journal location to operate on.
