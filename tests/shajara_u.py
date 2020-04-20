#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shajara import Tree, Node


def test_node():
    n = Node(value=1, label="n1")
    assert n.value == 1
    assert n.label == "n1"
    n.append_child("c1", Node(label="n2"))
    n.append_child("c2", Node(label="n3"))
    n.append_child("c3", Node(label="n4"))
    order = ["n2", "n3", "n4"]
    order_arcs = ["c1", "c2", "c3"]
    # verify the order
    i = 0
    for arc in n.children:
        assert arc == order_arcs[i]
        assert n.children[arc].label == order[i]
        i += 1

#TODO test Tree
