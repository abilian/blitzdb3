from __future__ import absolute_import, print_function, unicode_literals

from .base import BaseField


class OneToManyField(BaseField):

    """
    """

    def __init__(self, related, key, backref=None, unique=False, *args, **kwargs):
        super(OneToManyField, self).__init__(*args, **kwargs)
        self.related = related
        self.key = key
        self.unique = unique
        self.backref = backref
