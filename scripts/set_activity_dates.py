#!/usr/bin/env python3
"""
Update the dates of the _days/day-%d.md according to the Excel file in CALENDAR_XLSX.
(See the source for where this script looks for that file.)
This file should have fields 'Date' and 'Instructional Day'.

Author: Oliver Steele
Date: 2017-01-14
License: MIT
"""

import os
import re
from copy import deepcopy
from datetime import date

import pandas as pd
import yaml

CALENDAR_XLSX = '~/Downloads/SoftDes Spring 2017 Calendar.xlsx'
INSTRUCTIONAL_DAY_LABEL = 'Instructional Day'
DAY_FILE_FMT = './_days/day-{}.md'
DRY_RUN = False

publication_date = date.today()  # days after this date are published

df = pd.read_excel(os.path.expanduser(CALENDAR_XLSX))

# select rows whose Instructional Days are numbers (represented as strings)
instr_day_df = df[df[INSTRUCTIONAL_DAY_LABEL].astype(str).str.match(r'\d+')].set_index(INSTRUCTIONAL_DAY_LABEL)
instr_day_df = instr_day_df[pd.notnull(instr_day_df.Date)]

for day_no, activity_date in instr_day_df['Date'].dt.date.iteritems():
    fname = DAY_FILE_FMT.format(day_no)
    if not os.path.exists(fname):
        print('file does not exist:', fname)
        continue

    with open(fname) as f:
        m = re.match(r'^---\n(.+?\n)---\n(.*)', f.read(), re.DOTALL)
        fm_s, content = m.groups()
        fm0 = yaml.load(fm_s)

    fm1 = deepcopy(fm0)
    fm1['activity_date'] = activity_date
    fm1['published'] = publication_date >= activity_date

    if fm0 == fm1:
        print('unchanged:', fname)
        continue

    if not DRY_RUN:
        with open(fname, 'w') as f:
            f.write('---\n')
            yaml.dump(fm1, f, default_flow_style=False)
            f.write('---\n')
            f.write(content)

    print('updated', fname)
