#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shajara import Tree, Node
from shajara.search.binary import binary_adder, binary_searcher, binary_opti_searcher

values = [5, 9, 2, 11, 3, 7, 2]
labels = ["five", "nine", "two", "eleven", "three", "seven", "two_again"]

search = [4, 5, 8, 10, 12]
find = [3, 5, 7, 11, 11]
rels = ["<", "=", "<", ">", "<"]

t = Tree()

def test_binary_adder():
    for i in range(len(values)):
        binary_adder.set_parameters(Node(value=values[i], label=labels[i]))
        t.process(processor=binary_adder)
    assert t.root.value == 5
    assert t.root.children[">"].value == 2
    assert t.root.children[">"].label == "two_again"
    assert t.root.children["<"].value == 9

def test_binary_searcher():
    for i in range(len(search)):
        v = search[i]
        binary_searcher.set_parameters(value=v)
        rel, node = t.process(processor=binary_searcher)
        assert rel == rels[i]
        assert node.value == find[i]

def test_binary_opti_searcher():
    binary_opti_searcher.set_parameters(search="min")
    min_node = t.process(processor=binary_opti_searcher)
    assert min_node.value == 2
    binary_opti_searcher.set_parameters(search="max")
    max_node = t.process(processor=binary_opti_searcher)
    assert max_node.value == 11
