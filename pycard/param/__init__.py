"""Parameters for vCard properties.

The params dict contains all known params. They are objects with name
and value attributes (value may be None), plus some optional method
related to what they represents.

"""
from ..tools.lexer import split_param
from .base import params
from .delivery_address import *
from .encodings import QuotedPrintableParam


def from_list(lst):
    name = lst[0]
    param = params[name]
    return param
    # value = lst[1] if len(lst) > 1 else None
    # return Param(name, value)


def from_string(string):
    lst = split_param(string)
    return from_list(lst)
