from itertools import chain

from .param import params
from .prop import BeginProp, EndProp, UnknownProp
from .prop import from_string as property_from_string
from .tools.lexer import logical_lines


__all__ = ["PyCard"]


class PyCard(object):
    """Object-oriented interface to a vCard

    “A vCard is a collection of one or more properties.”

                           ---vCard, The Electronic Business Card, Version 2.1,
                                      http://www.imc.org/pdi/vcard-21.txt, §.2.

    The instance properties are stored in the the .props list.

    """
    def __init__(self, props=None):
        self._props = list()
        ## Argument preparation.
        props = list() if props is None else props.copy()
        ## Adds vCard properties
        while props:
            self.props.append( props.pop(0) )

    def format(self):
        return "".join( prop.format() for prop in self.props )

    def check(self):
        """Check badly formed vCards"""
        if len(props) == 0:
            raise Exception("Empty vCard")
        if props[0].name != BeginProp.name:
            raise Exception("vCard does not start with BEGIN:VCARD")
        if props[-1].name != EndProp.name:
            raise Exception("vCard does not end with END:VCARD")

    @classmethod
    def from_stream(cls, stream):
        """Yields vCards objects from a text stream.

        """
        current_obj = None
        for line in logical_lines(stream):
            prop = property_from_string(line)
            if  prop.name == BeginProp.name:
                if current_obj is not None:
                    raise Exception("new vCard without ending the precedent one.")
                current_obj = cls()
            current_obj.props.append(prop)
            if  prop.name == EndProp.name:
                if current_obj is None:
                    pass
                yield current_obj
                current_obj = None

    @property
    def props(self):
        """property list"""
        return self._props
