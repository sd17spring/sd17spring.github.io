"""
Update file dates to match the git modification times.

Author: Oliver Steele
Date: 2017-01-21
License: MIT
"""

# TODO:
# [ ] switch date format
# [ ] don't warn about files that have been removed from the repo
# [ ] read _config include, exclude

import os
import re
import subprocess
from copy import deepcopy

import arrow
import yaml

DRY_RUN = False
WARN_ON_NOT_EXISTS = False

os.chdir(os.path.join(os.path.dirname(__file__), '..'))
p = subprocess.run("git log --pretty=medium --date=iso8601 --stat=1024 --stat".split(),
                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
lines = p.stdout.decode().split('\n')

file_modtimes = {}
for line in lines:
    if line.startswith('Date:'):
        date = line.split(':', 1)[1].strip()
        date = arrow.get(date, 'YYYY-MM-DD HH:mm:ss Z')
    m = re.match(r' (\S.*?)\s+\| \d+', line)
    if m:
        filename = m.group(1)
        # filename = re.replace()
        filename = re.sub(r'{.+? => (.+?)}', r'\1', filename)
        filename = re.sub(r'.+? => (.+)', r'\1', filename)
        file_modtimes[filename] = file_modtimes.get(filename, date)

for fname, date in file_modtimes.items():
    if not re.match(r'.*\.(md|html)', fname):
        continue

    if re.match(r'(_layout|_includes|[^_].+\/)\/', fname):
        continue

    if not os.path.exists(fname):
        if WARN_ON_NOT_EXISTS:
            print('file does not exist:', fname)
        continue

    with open(fname) as f:
        m = re.match(r'^---\n(.+?\n)---\n(.*)', f.read(), re.DOTALL)
        if not m:
            print('no frontmatter:', fname)
            continue
        fm_s, content = m.groups()
        fm0 = yaml.load(fm_s)

    if 'date' not in fm0:
        print('no date in frontmatter:', fname)
        continue

    fm1 = deepcopy(fm0)
    # fm1['date'] = date.strftime('%Y-%m-%d')
    fm1['date'] = date.format('YYYY-MM-DD HH:mm:ss Z')
    # fm1['date'] = date.isoformat()

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
