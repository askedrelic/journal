#Journal

Journal is a Python command line tool to help with keeping a date and time
organized journal for work, personal, or any reason really!

Inspired by Peter Lyons' [article](http://peterlyons.com/leveling_up.html) on career development, my own experiences, and too much free time.

Related:

* [My blog post explaining Journal](http://asktherelic.com/2011/08/16/journaling/)

##Installation

Journal is on pypi at [http://pypi.python.org/pypi/journal/](http://pypi.python.org/pypi/journal/)

To install, from a command line:

	$ pip install journal

or

    $ easy_install journal

depending on how much Python work you do.

Journal only requires Python, (tested on Python 2.5, 2.6, 2.7).

The `journal` command should now be available on your command line.

##Usage

It's as simple as:

    $ journal "Task foo completed"

and a `~/.journal/[DATE].txt` file will be created using the current date with a timestamp and your entry appended to that file. Keep entering your tasks you complete during the day and then you can quickly view your work at the end of the day. Or review what you did yesterday, just before your morning scrum meeting! Or review what you did last week, when you come back on Monday! Build a simple record of your work and gain better understanding of your work.

The API for viewing and listing previous entries is currently a WIP, but you
should be able to view specific entries for a day by using the flag `--view|-v`.

Short tags work with these dates.

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

##Advanced usage

By default, journal entries are stored in `~/.journal`. By providing the `--location|-l path` command line switch entries will be read from & written to the provided directory. This functionality is useful for having journals dealing with separate domains:

    $ journal -l ~/.work "Got all of the monies"
    $ journal -l ~/.home "Spent all the monies"

See below for using a `.journalrc` to define these journals & storage locations.

###Configuration

You can create a `.journalrc` file (or one specified with the `-c` switch) to define default journal directories:

    [journal]
    default: work

    [home]
    location: ~/Dropbox/journals/home

    [work]
    location: ~/Dropbox/journals/work

With multiple journals defined, you can use the `--journal|-j name` switch to choose which journal to write to.
