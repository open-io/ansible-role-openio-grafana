import json
import urllib2
from base64 import b64encode
from traceback import format_exc


class PutRequest(urllib2.Request):

    def __init__(self, *args, **kwargs):
        return urllib2.Request.__init__(self, *args, **kwargs)

    def get_method(self, *args, **kwargs):
        return 'PUT'


class FilterModule(object):
    def filters(self):
        return {
            'set_default_dashboard': self.set_default_dashboard,
        }

    def set_default_dashboard(self, ip, user, password, proto, port):
        try:
            BASE_URL = "%s://%s:%s" % (proto, ip, port)
            AUTH = "Basic %s" % b64encode("%s:%s" % (user, password))

            req = urllib2.Request("%s/api/search" % BASE_URL)
            req.add_header("Authorization", AUTH)

            data = json.load(urllib2.urlopen(req))

            dashboards = [d['id'] for d in data if d['title'] == 'Overview']
            if len(dashboards) < 1:
                raise Exception("Overview dashboard not found")

            data = json.dumps(dict(homeDashboardId=dashboards[0], theme="", timezone=""))

            req = PutRequest("%s/api/user/preferences" % BASE_URL, data=data)
            req.add_header("Authorization", AUTH)
            req.add_header("Content-Type", 'application/json')
            res = json.loads(urllib2.urlopen(req).read())
            return res["message"]
        except Exception as e:
            return "Could not update preferences, %s" % format_exc(e)
