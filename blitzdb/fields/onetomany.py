from .base import BaseField


class OneToManyField(BaseField):

    """"""

    def __init__(self, related, key, backref=None, unique=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.related = related
        self.key = key
        self.unique = unique
        self.backref = backref
