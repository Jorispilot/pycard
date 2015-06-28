import io
import unittest

from pycard.tools.lexer import logical_lines, split_line


class LogicalLineTestCase(unittest.TestCase):

    def test_1(self):
        stream = io.StringIO("""\
BEGIN:VCARD
VERSION:2.1
X-DL;Design Work Group:List Item 1;List Item 2;List Item 3
BEGIN:VCARD
UID:List Item 1
N:John Smith
""", newline="\r\n")
        result = [
            "BEGIN:VCARD\r\n",
            "VERSION:2.1\r\n",
            "X-DL;Design Work Group:List Item 1;List Item 2;List Item 3\r\n",
            "BEGIN:VCARD\r\n",
            "UID:List Item 1\r\n",
            "N:John Smith\r\n",
        ]
        self.assertSequenceEqual(result, list(logical_lines(stream)))

    def test_2(self):
        stream = io.StringIO("""\
SOUND;WAVE;BASE64:
    UklGRhAsAABXQVZFZm10IBAAAAABAAEAESsAABErAAABAAgAZGF0YesrAACAg4eC
    eXR4e3uAhoiIiYmKjIiDfnx5eX6CgoKEhYWDenV5fH6BhISGiIiDfHZ2eXt/hIiK
    jY2IhH12d3Vyc3uDiIiFf3l7fn18eXl+houFf319fnyAgHl5eoCIiISChIeAfnt2
TEL:+1-213-555-5555
END:VCARD
""", newline="\r\n")
        result = [
            "SOUND;WAVE;BASE64:UklGRhAsAABXQVZFZm10IBAAAAABAAEAESsAABErAAABAAgAZGF0YesrAACAg4eCeXR4e3uAhoiIiYmKjIiDfnx5eX6CgoKEhYWDenV5fH6BhISGiIiDfHZ2eXt/hIiKjY2IhH12d3Vyc3uDiIiFf3l7fn18eXl+houFf319fnyAgHl5eoCIiISChIeAfnt2\r\n",
            "TEL:+1-213-555-5555\r\n",
            "END:VCARD\r\n",
        ]
        self.assertSequenceEqual(result, list(logical_lines(stream)))

    def test_3(self):
        stream = io.StringIO("""\
SOUND;WAVE;BASE64:
    UklGRhAsAABXQVZFZm10IBAAAAABAAEAESsAABErAAABAAgAZGF0YesrAACAg4eC
    eXR4e3uAhoiIiYmKjIiDfnx5eX6CgoKEhYWDenV5fH6BhISGiIiDfHZ2eXt/hIiK
    jY2IhH12d3Vyc3uDiIiFf3l7fn18eXl+houFf319fnyAgHl5eoCIiISChIeAfnt2
""", newline="\r\n")
        result = [
            "SOUND;WAVE;BASE64:UklGRhAsAABXQVZFZm10IBAAAAABAAEAESsAABErAAABAAgAZGF0YesrAACAg4eCeXR4e3uAhoiIiYmKjIiDfnx5eX6CgoKEhYWDenV5fH6BhISGiIiDfHZ2eXt/hIiKjY2IhH12d3Vyc3uDiIiFf3l7fn18eXl+houFf319fnyAgHl5eoCIiISChIeAfnt2\r\n",
        ]
        self.assertSequenceEqual(result, list(logical_lines(stream)))


class SplitLineTestCase(unittest.TestCase):

    def test_1(self):
        line = "BEGIN:VCARD\r\n"
        result = ([], "BEGIN", [], "VCARD")
        self.assertSequenceEqual(result, split_line(line))

    def test_2(self):
        line = "X-DL;Design Work Group:List Item 1;List Item 2;List Item 3\r\n"
        result = ([], "X-DL", ["Design Work Group"], "List Item 1;List Item 2;List Item 3")
        self.assertSequenceEqual(result, split_line(line))

    def test_3(self):
        line = "A.TEL;HOME:+1-213-555-1234"
        result = (["A"], "TEL", ["HOME"], "+1-213-555-1234")
        self.assertSequenceEqual(result, split_line(line))

        
