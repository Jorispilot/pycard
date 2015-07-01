from .base import Param


__all__ = [
	"URLParam",
]


class ValueParam(Param):

    def __init__(self, valu):
        super().__init__("VALUE", value)


URLParam   = TypeParam("URL")
