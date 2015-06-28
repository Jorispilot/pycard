import re

__all__ = ["SPACE", "HTAB", "CRLF", "ws"]


## Definitions from: http://www.imc.org/pdi/vcard-21.txt
SPACE = " "
HTAB  = "\t"
CRLF  = "\r\n"
ws = re.compile("["+ SPACE + HTAB +"]+", re.ASCII + re.IGNORECASE)
