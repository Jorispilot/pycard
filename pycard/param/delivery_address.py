from .base import Param


__all__ = ["DomesticParam", "InternationalParam", "PostalParam",
           "ParcelParam", "HomeParam", "WorkParam"]


DomesticParam = Param("DOM")
InternationalParam = Param("INTL")
PostalParam = Param("POSTAL")
ParcelParam = Param("PARCEL")
HomeParam = Param("HOME")
WorkParam = Param("WORK")
