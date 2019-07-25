from __future__ import absolute_import, print_function, unicode_literals

from .base import BaseField


class CharField(BaseField):
    def __init__(self, length=None, *args, **kwargs):
        self.length = length
        super(CharField, self).__init__(*args, **kwargs)
