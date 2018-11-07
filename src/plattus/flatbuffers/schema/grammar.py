# -*- coding: utf-8 -*-

import pkgutil

from lark import Lark


parser = Lark(
    pkgutil.get_data("plattus.flatbuffers.schema", "flatbuffer.lark").decode("utf8"),
    parser="lalr",
    start="schema",
)
