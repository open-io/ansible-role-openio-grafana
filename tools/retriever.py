#!/usr/bin/env python3

import requests
import sys
import json
from os import path


class DashboardRetriever(object):

    def __init__(self, host, user, password, dst):
        self.BASE_URL = "http://%s:%s@%s" % (user, password, host)
        self.DST = dst

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
            name = dash['title'].lower().replace(' ', '_')
            data = self.sanitize(self.get_dashboard(dash['uid']))
            self.save(name, data)
            print("Imported dashboard \"%s\" (%d/%d)" %
                  (name, index + 1, len(dashboards)))

    def sanitize(self, data):
        """ Sanitize a dashboard """
        for k in ('id', 'version', 'uid'):
            if k in data:
                del data[k]
        if 'templating' in data and 'list' in data['templating']:
            del data['templating']['list'][0]['current']
        return data

    def save(self, name, data):
        """ Save a Grafana dashboard """
        with open(path.join(self.DST, "%s.json" % name), 'w') as f:
            f.write(json.dumps(data))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("Usage: %s HOST:PORT USER PASSWORD DESTINATION" % sys.argv[0])

    DashboardRetriever(*sys.argv[1:]).run()
