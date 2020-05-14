"""
Serializers take a Python object and return a string representation of it.
BlitzDB currently supports several differen JSON serializers,
as well as a cPickle serializer.
"""

import json
import pickle as cPickle

import six

from .utils import JsonEncoder


class JsonSerializer:
    @classmethod
    def serialize(cls, data):
        if isinstance(data, bytes):
            return json.dumps(
                data.decode("utf-8"), cls=JsonEncoder, ensure_ascii=False
            ).encode("utf-8")

        else:
            return json.dumps(data, cls=JsonEncoder, ensure_ascii=False).encode("utf-8")

    @classmethod
    def deserialize(cls, data):
        return json.loads(data.decode("utf-8"))


class PickleSerializer:
    @classmethod
    def serialize(cls, data):
        return cPickle.dumps(data, cPickle.HIGHEST_PROTOCOL)

    @classmethod
    def deserialize(cls, data):
        return cPickle.loads(data)


try:
    import cjson

    class CJsonSerializer:
        @classmethod
        def serialize(cls, data):
            return cjson.encode(data)

        @classmethod
        def deserialize(cls, data):
            return cjson.decode(data)


except ImportError:
    pass
