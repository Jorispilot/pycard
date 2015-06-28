import re

from .base import *


__all__ = ["escape_value", "logical_lines", "split_line", "split_list", "split_param"]


def escape_value(value):
    return value.replace(",","\,").replace(";","\;").replace(":","\:")


def logical_lines(stream):
    """Split the text stream agument to a sequence of logical (unfolded)
    lines.

    """
    lastline = next(stream)
    for line in stream:
        if re.match(ws, line):
            ## Continuation line.
            lastline = lastline.rstrip(CRLF) + line.lstrip(SPACE + HTAB)
        else:
            ## New logical line.
            yield lastline
            lastline = line
    yield lastline


def split_line(line):
    """Split a logical line into the tuple:
    
        name, [param0, param1, ...], value

    """
    ## To avoid matching escaped separators, use: "(?!\\\\):"
    ## but there must me need to use it.
    groups_name_params, value_crlf = re.split(":", line, 1)
    groups_name_params = re.split(";", groups_name_params)
    groups_name, params = groups_name_params[0], groups_name_params[1:]
    groups_name = re.split("\.", groups_name)
    groups, name = groups_name[:-1], groups_name[-1]
    value = value_crlf.rstrip(CRLF)
    return groups, name, params, value


def split_list(value, sep=","):
    value = re.split("(?<!\\\\)" + re.escape(sep), value)
    return [val.replace("\\" + sep, sep) for val in value]


def split_param(param):
    return tuple(param.split("=", 1))
