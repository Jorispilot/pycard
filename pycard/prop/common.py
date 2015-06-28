from ..param.base import Param
from .base import ListProp, StringProp, props


__all__ = ["BeginProp", "CategoriesProp", "EndProp", "UnknownProp"]


class BeginProp(StringProp):

    def __init__(self, value="VCARD", params=None, groups=None):
        super().__init__(value, params, groups)

    @property
    def authorized_params(self):
        return []

    name = "BEGIN"


class CategoriesProp(ListProp):

    name = "CATEGORIES"

    sep = ","


class EndProp(StringProp):

    def __init__(self, value="VCARD", params=None, groups=None):
        super().__init__(value, params, groups)

    name = "END"


class UnknownProp(StringProp):
    """A generic Vcard property for non-handled properties.

    Any parameters are authorized.

    """
    def __init__(self, name, value=None, params=None, groups=None):
        self.name = name
        super().__init__(value, params, groups)

    authorized_params = None

    @classmethod
    def _check_params(cls, params):
        ## Allow any parameters, expecially unknown ones.
        pass

    @classmethod
    def from_tuple(cls, tpl):
        groups, name, params, value = tpl
        params = [param_from_string(p) for p in params]
        value = cls.from_tuple_value(value)
        return cls(name, value, params, groups)
