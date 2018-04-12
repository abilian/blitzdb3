from __future__ import absolute_import, print_function, unicode_literals

from .base import BaseField


class EnumField(BaseField):

    def __init__(self, enums, native_enum=False, *args, **kwargs):
        self.enums = enums
        self.native_enum = native_enum
        super(EnumField, self).__init__(*args, **kwargs)
