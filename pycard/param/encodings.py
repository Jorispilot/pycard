import base64
import quopri

from .base import Param


__all__ = ["Base64Param", "QuotedPrintableParam"]


class EncodingParam(Param):

    def __init__(self, value, decoder, encoder):
        super().__init__("ENCODING", value)
        self._decoder = decoder
        self._encoder = encoder

    def decode(self, text):
        return self._decoder(text)

    def encode(self, text):
        return self._encoder(text)


Base64Param = EncodingParam(
    "BASE64",
    base64.standard_b64decode,
    base64.standard_b64encode)


QuotedPrintableParam = EncodingParam(
    "QUOTED-PRINTABLE",
    quopri.decodestring,
    quopri.encodestring)
