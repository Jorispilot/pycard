from collections import namedtuple

from ..param.delivery_address import *
#from ..tools.tools import *
from ..tools.lexer import escape_value
from .base import TupleProp


__all__ = ["DeliveryAddress"]


PostalAddress = namedtuple("PostalAddress", ["post_office_address",
                                             "extended_address", "street",
                                             "locality", "region",
                                             "postal_code", "country"])


class DeliveryAddress(TupleProp):

    def __init__(self, value=None, params=None, groups=None):
        """The first argument must be a tuple consisting of seven elements:

          (post_office_address, extended_address, street, locality, region, 
           postal_code, country)

        An empty string serves to indicate an empty element.

        """
        value = PostalAddress(*value)
        super().__init__(value, params, groups)

    authorized_params = ( TupleProp.authorized_params + 
                          ["TYPE"] +
                          [DomesticParam.name,
                           InternationalParam.name,
                           PostalParam.name, ParcelParam.name,
                           HomeParam.name, WorkParam.name] )

    name = "ADR"

    sep = ";"
