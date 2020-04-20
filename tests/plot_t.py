#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shajara.plot import graphviz_processor
from shajara import Tree, Node

t = Tree(Node(label="a"))
b = Node(label="b")
c = Node(label="c")
d = Node(label="d")
t.get_root().append_child("ab", b).append_child("ac", c).append_child("ad", d)
e = Node(label="e")
f = Node(label="f")
b.append_child("be", e).append_child("bf", f)

#t.process()# testing the default

graph = t.process(processor=graphviz_processor)

f = open("graphviz.dot", "w")
f.write(graph)
f.close()
