#!/usr/bin/env python2

import json
import sys
from shutil import copyfile


if len(sys.argv) != 2:
    print "Usage: %s [path to dashboard]" % sys.argv[0]
    sys.exit(1)

try:
    copyfile(sys.argv[1], sys.argv[1] + ".old")
    with open(sys.argv[1], 'r+') as f:
        data = json.load(f)
        for k in ('id', 'version', 'uid'):
            if k in data:
                del data[k]
        if 'templating' in data and 'list' in data['templating']:
            del data['templating']['list'][0]['current']
        f.seek(0)
        f.write(json.dumps(data))
        f.truncate()
        print "File %s has been sanitized. Backup saved to %s" % (sys.argv[1], sys.argv[1] + ".old")
except Exception as e:
    raise e
