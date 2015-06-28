"""vCard properties.

A vCard property is identified by its name, has a list of zero or more
parameters, and has a value. These elements are typeset as follows:

    NAME[;PARAMERERS]:VALUE

This package offers OOP acces to vCard properties that can be loaded
and dumped from files. There is a generic object called
UnknownProperty than can handle any property, plus sub-classes for
specific properties.

Note: Not all defined properties are coded at the time.

The props dict defined in this package references all objects by their
correponding vCard NAME.

"""
from ..tools.lexer import split_line
from .base import props
from .common import *
from .delivery_address import *
from .name import *


def from_string(string):
    tpl = split_line(string)
    return from_tuple(tpl)


def from_tuple(tpl):
    name = tpl[1]
    Prop = props.get(name, UnknownProp)
    return Prop.from_tuple(tpl)
