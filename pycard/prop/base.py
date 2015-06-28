"""Abstract base classe for vCard Properties.

"""
import warnings
from abc import abstractmethod, ABCMeta
from collections.abc import Sequence

from ..param import from_string as param_from_string
from ..tools.base import CRLF
from ..tools.lexer import escape_value, split_list


__all__ = ["Prop", "StringProp", "TupleProp"]


props = dict()


class PropRegisterType(ABCMeta, type):
    """Customized metaclass for Properties.

    New properties are added to the props dict to allows for directory
    access to these object.

    """
    def __init__(cls, name, bases, nmspc):
        super().__init__(name, bases, nmspc)
        if cls.name is not None:
            props[cls.name] = cls


class Prop(object, metaclass=PropRegisterType):
    """Base class for Vcard properties.

    A property has a unique name, a list of 0 or more properties, and
    a value.

    URL: http://www.imc.org/pdi/vcard-21.txt

    """
    def __and__(p1, p2):
        """Compare types."""
        if isinstance(p2, Prop):
            return p1.name == p2.name
        elif isinstance(p2, Sequence ):
            return p1.name == p2[1]
        else:
            raise TypeError("Cannot compare with object.")

    def __eq__(p1, p2):
        return (p1 & p2 and
                p1.groups == p2.groups and
                p1.params == p2.params and
                p1.value == p2.value)

    def __init__(self, value=None, params=None, groups=None):
        groups = list() if groups is None else groups
        params = list() if params is None else params
        self.groups = groups
        self._check_params(params)
        self.params = params
        self.value = value

    authorized_params = ["ENCODING"]

    @classmethod
    def _check_params(cls, params):
        for param in params:
            if param.name not in cls.authorized_params:
                raise ValueError("unauthorized param: {!s}".format(param))

    def format(self):
        """Format property as vCard specification."""
        groups = [g + "." for g in self.groups]
        params = [";" + p.format() for p in self.params]
        groups_name_params = "".join(groups) + self.name + "".join(params)
        return groups_name_params + ":" + self.format_value() + CRLF

    @abstractmethod
    def format_value(self):
        pass

    @classmethod
    def from_tuple(cls, tpl):
        groups, name, params, value = tpl
        params = [param_from_string(p) for p in params]
        value = cls.from_tuple_value(value)
        return cls(value, params, groups)

    @classmethod
    @abstractmethod
    def from_tuple_value(cls, value):
        pass

    name = None

    @property
    def value(self):
        return self._value
    @value.setter
    @abstractmethod
    def value(self, value):
        pass


class ListProp(Prop):

    @Prop.value.setter
    def value(self, value):
        self._value = list(value)

    def __init__(self, value=None, params=None, groups=None):
        value = list if value is None else value
        super().__init__(value, params, groups)

    def format_value(self):
        value = [escape_value(p) for p in self.value]
        return self.sep.join(value)

    @classmethod
    def from_tuple_value(cls, value):
        return split_list(value, cls.sep)

    sep = None


class StringProp(Prop):

    def __init__(self, value="", params=None, groups=None):
        super().__init__(value, params, groups)

    def format_value(self):
        return escape_value(self.value)

    @classmethod
    def from_tuple_value(cls, value):
        return value

    @Prop.value.setter
    def value(self, value):
        self._value = str(value)


class TupleProp(Prop):

    @Prop.value.setter
    def value(self, value):
        self._value = tuple(value)

    def __init__(self, value=None, params=None, groups=None):
        value = list if value is None else value
        super().__init__(value, params, groups)

    def format_value(self):
        value = [escape_value(p) for p in self.value]
        return self.sep.join(value)

    @classmethod
    def from_tuple_value(cls, value):
        return split_list(value, cls.sep)

    sep = None
