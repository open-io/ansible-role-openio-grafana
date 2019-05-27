#!/usr/bin/env python3

import requests
import sys
import json
from os import path, makedirs


class DashboardRetriever(object):

    def __init__(self, host, user, password, dst, strict=False):
        self.BASE_URL = "http://%s:%s@%s" % (user, password, host)
        self.DST = dst
        self.strict = strict

    @property
    def list_dashboards(self):
        """ List grafana dashboards """
        return requests.get("%s/api/search" % self.BASE_URL).json()

    def get_dashboard(self, uid):
        """ Get a dashboard from Grafana, specified by its UUID """
        return requests.get(
            "%s/api/dashboards/uid/%s" % (self.BASE_URL, uid)).json()

    def run(self):
        """ Retrieve dashboards from Grafana, and sanitizes them """
        dashboards = self.list_dashboards
        for index, dash in enumerate(dashboards):
            if dash['type'] == 'dash-db':
                self.import_one(index, dash, len(dashboards))

    def import_one(self, index, dash, total):
        name = dash['title'].lower().replace(' ', '_')
        data, errors = self.sanitize(self.get_dashboard(dash['uid']))
        saved = self.save(name, data, folder=dash.get('folderTitle', None))
        print("Imported dashboard \"%s\" (%d/%d)" %
              (saved, index + 1, total))
        for e in errors:
            print(e % name)
            if self.strict:
                sys.exit("ERROR: Strict validation mode is on, \
aborting due to warning")

    def sanitize(self, data):
        """ Sanitize a dashboard """
        errors = list()
        if 'dashboard' not in data:
            raise Exception('Invalid dashboard format')
        data = data['dashboard']
        for k in ('id', 'version', 'uid'):
            if k in data:
                del data[k]
        if 'time' in data:
            data['time'] = {"from": "now-15m", "to": "now"}
        try:
            del data['templating']['list'][0]['current']
        except Exception:
            pass
        if 'editable' in data and data['editable']:
            errors.append('WARN: [%s] dashboard has been left editable')
        return data, errors

    def save(self, name, data, folder=None):
        """ Save a Grafana dashboard """
        dest = self.DST
        if folder:
            dest = path.join(self.DST, folder)
            if not path.exists(dest):
                makedirs(dest)
        with open(path.join(dest, "%s.json" % name), 'w') as f:
            f.write(json.dumps(data, indent=2))
        return path.join(folder or str(), "%s.json" % name)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("Usage: %s HOST:PORT USER \
PASSWORD DESTINATION [STRICT]" % sys.argv[0])

    DashboardRetriever(*sys.argv[1:]).run()
