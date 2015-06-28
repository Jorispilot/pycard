import re
from .base import *


def physical_lines(line, length=75, indent=" "):
    """Fold lines to the specified length.

    """
    line, nextline = line[:length], line[length:]
    lines = [line + CRLF]
    length -= len(indent)
    while nextline:
        line, nextline = nextline[:length], line[length:]
        lines.append(indent + line + CRLF)
    return lines
