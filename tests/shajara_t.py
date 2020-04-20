#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shajara.plot import graphviz_processor
from shajara import Tree, Node

t = Tree(Node(label="a"))
t.add_child("ab", Node(label="b")).add_child("ac", Node(label="c")).add_child("ad", Node(label="d"))
t.select_child("ab").add_child("be", Node(label="e")).add_child("bf", Node(label="f"))
t.up().select_child("ad").add_child("dg", Node(label="g")).add_child("dh", Node(label="h"))

graph = t.process(processor=graphviz_processor)

f = open("shajara.dot", "w")
f.write(graph)
f.close()
