from functools import partial

from ..params.encodings import EncodingParam
from ..params.values import URLParam
from .base import StringProp


__all__ = ["PhotoProp"]


class PhotoProp(StringProp):

    authorized_params = ["ENCODING", "TYPE", "VALUE"]

    name = "PHOTO"

    def export(self, path):
        """Export value to a file.

        """
        pass

    def import(self, path):
        """Import a file to the value.

        """
        if URLParam in self.params:
            ## Do not import.
            return
        ## Check and get encodings.
        encoders = {p for p in self.params if isinstance(p, EncodingParam)}
        if   len(encoders) == 0:
            raise ValueError("No encoding found.")
        elif len(encoders) > 1:
            raise ValueError("More than one encoding, ambigous.")
        encoder = next(encoders)
        ## Check path.
        if not path.exists():
            raise FileNotFoundError( str(path) )
        ## TODO: Check file extension.
        ## Do import.
        with path.open("rb") as file:
            self.value = encoder.encode(file.read())
