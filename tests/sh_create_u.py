#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shajara.create import GenerateProcessor
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

def test_generate_processor():
    generator = GenerateProcessor(rep)
    t = Tree()
    assert t.current_node().label == ""
    t.process(processor=generator)
    assert t.current_node().label == "a"
    t.select_child("ab")
    assert t.current_node().label == "b"
    t.select_child("be")
    assert t.current_node().label == "e"
    t.up().select_child("bf")
    assert t.current_node().label == "f"
    t.up().up().select_child("ac")
    assert t.current_node().label == "c"
    t.up().select_child("ad")
    assert t.current_node().label == "d"
