#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Copyright 2020 Abdelkrime Aries <kariminfo0@gmail.com>
#
#  ---- AUTHORS ----
#  2020	Abdelkrime Aries <kariminfo0@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shajara.plot import graphviz_processor
from shajara import Tree, Node

t = Tree(label="a")
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
