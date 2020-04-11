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

from trees.plot import graphviz_processor
from trees import Tree, Node

t = Tree(label="a")
t.add_child("ab", Node(label="b")).add_child("ac", Node(label="c")).add_child("ad", Node(label="d"))
t.select_child("ab").add_child("be", Node(label="e")).add_child("bf", Node(label="f"))
t.up().select_child("ad").add_child("dg", Node(label="g")).add_child("dh", Node(label="h"))

graph = t.process(processor=graphviz_processor)

f = open("graphviz_trees.dot", "w")
f.write(graph)
f.close()
