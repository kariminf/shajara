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
#from trees import Tree, Node
from shajara.search import BSearchTree, binary_searcher

# values = [1, 2, 3, 4, 5, 6, 3]
# labels = ["one", "two", "three", "four", "five", "six", "three"]

values = [5, 9, 2, 11, 3, 7, 2]
labels = ["five", "nine", "two", "eleven", "three", "seven", "two_again"]

search = [4, 5, 8, 10, 12]

t = BSearchTree()

for i in range(len(values)):
    t.search_add(values[i], label=labels[i], add=True)

graph = t.process(processor=graphviz_processor)

f = open("graphviz_btree.dot", "w")
f.write(graph)
f.close()

for i in search:
    binary_searcher.set_parameters(value=i)
    found, node, rel = t.process(processor=binary_searcher)
    if found :
        print (str(i) + " is " + node.label)
    else:
        pos = "before "
        if (rel =="<"):
            pos = "after "
        print (str(i) + " not found. It must be " + pos + str(node.value))
