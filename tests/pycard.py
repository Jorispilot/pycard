import io
import unittest

import pycard.pycard as pycard


class TestCase(unittest.TestCase):

    def test_1(self):
        stream = io.StringIO("""\
BEGIN:VCARD
VERSION:3.0
UID:1xek1ndn-d3q0-f287-gq1f-b7raoyb4toxy
N:;aasgd;;;
FN:aasgd
REV:20150619T185609Z
PRODID:-//Inf-IT//CardDavMATE 0.12.0//EN
END:VCARD
""", newline="\r\n")
        pp = pycard.PyCard.from_stream(stream)
        p = next(pp)
        print(p.format())
        self.fail()
