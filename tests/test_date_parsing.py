#!/usr/bin/env python
# -*- coding: utf-8 -*-

#py25, py26 compat
try:
    import unittest2 as unittest
except ImportError:
    import unittest

import datetime

from journal import main, parse


class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = parse.Parse()
        self.today = datetime.date.today()

    def test_parsing_days(self):
        date_today = datetime.date(self.today.year, self.today.month, self.today.day)
        date_yesterday = datetime.date(self.today.year, self.today.month, self.today.day-1)

        dates = map(self.parser.day, 'today t yesterday y'.split())
        answers = [date_today, date_today, date_yesterday, date_yesterday]

        self.assertListEqual(dates, answers)

    def test_parsing_n_days(self):
        # days ago case
        dates = []
        answers = []
        for n in xrange(1,12,2):
            dates.append("%s days ago" % n)
            answers.append(datetime.date(self.today.year, self.today.month, self.today.day) - datetime.timedelta(days=n))

        #'a day ago' case
        dates.append("a day ago")
        answers.append(datetime.date(self.today.year, self.today.month, self.today.day) - datetime.timedelta(days=1))

        dates = map(self.parser.day, dates)

        self.assertListEqual(dates, answers)

    def test_parsing_dates(self):
        dates = ['2/6/1977', '02/06/77', '1977-06-02', 'June 2, 1977', 'Jun 2, 1977', '2 June', 'Jun 2']
        dates += ['July 22, 1986', '7/22/86', 'July 22 1986', '07 22 1986', '07/22/1986', '7/22/86']
        dates = map(self.parser.day, dates)

        answers = [
                datetime.date(1977, 2, 6),
                datetime.date(1977, 2, 6),
                datetime.date(1977, 6, 2),
                datetime.date(1977, 6, 2),
                datetime.date(1977, 6, 2),
                datetime.date(self.today.year, 6, 2),
                datetime.date(self.today.year, 6, 2),
                ]
        answers += [
                datetime.date(1986, 7, 22),
                datetime.date(1986, 7, 22),
                datetime.date(1986, 7, 22),
                datetime.date(1986, 7, 22),
                datetime.date(1986, 7, 22),
                datetime.date(1986, 7, 22),
                ]

        self.assertListEqual(dates, answers)

if __name__ == '__main__':
    unittest.main()
