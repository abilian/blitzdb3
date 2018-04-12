from __future__ import absolute_import, print_function, unicode_literals

import datetime
import json


class JsonEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        elif isinstance(obj, datetime.datetime):
            return obj.ctime()
        return json.JSONEncoder.default(self, obj)
