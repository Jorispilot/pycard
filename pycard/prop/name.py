from collections import namedtuple

from ..tools.tools import *
from .base import StringProp, TupleProp


__all__ = ["FormattedName", "Name"]


NameParts = namedtuple("NameParts", ["familly_name", "given_name",
                                     "additional_names",
                                     "name_prefix",
                                     "name_suffix"])


class FormattedName(StringProp):

    name = "FN"


class Name(TupleProp):

    def __init__(self, value=None, params=None, groups=None):
        """The first argument must be a tuple consisting of five elements:

           (familly_name, given_name, additional_names, name_prefix,
            name_suffix)

        An empty string serves to indicate an empty element.

        """
        value = NameParts(*value)
        super().__init__(value, params, groups)

    name = "N"

    sep = ";"
