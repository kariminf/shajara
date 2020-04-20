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

res = """digraph Tree {
node [shape=box] ;
N1[label="a"];
N2[label="b"];
N1 -> N2 [label="ab"];
N3[label="e"];
N2 -> N3 [label="be"];
N4[label="f"];
N2 -> N4 [label="bf"];
N5[label="c"];
N1 -> N5 [label="ac"];
N6[label="d"];
N1 -> N6 [label="ad"];
}"""

def test_graphviz_processor():
    graph = t.process(processor=graphviz_processor)
    assert graph == res
