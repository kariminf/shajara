#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shajara.create import GenerateProcessor
from shajara.plot import graphviz_processor
from shajara import Tree

rep = {
    "label": "a",
    "children": {
        "ab": {
            "label": "b",
            "children": {
                "be": {"label": "e"},
                "bf": {"label": "f"}
            }
        },
        "ac": {"label": "c"},
        "ad": {"label": "d"}
    }
}

generator = GenerateProcessor(rep)
t = Tree()
t.process(processor=generator)
graph = t.process(processor=graphviz_processor)


f = open("graphviz_generate.dot", "w")
f.write(graph)
f.close()
