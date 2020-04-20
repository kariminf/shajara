#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shajara.plot import graphviz_processor
from shajara import Tree, Node
from shajara.search.binary import binary_adder, binary_searcher, binary_opti_searcher

# values = [1, 2, 3, 4, 5, 6, 3]
# labels = ["one", "two", "three", "four", "five", "six", "three"]

values = [5, 9, 2, 11, 3, 7, 2]
labels = ["five", "nine", "two", "eleven", "three", "seven", "two_again"]

search = [4, 5, 8, 10, 12]

t = Tree()

for i in range(len(values)):
    binary_adder.set_parameters(Node(value=values[i], label=labels[i]))
    t.process(processor=binary_adder)
    #t.search_add(values[i], label=labels[i], add=True)

graph = t.process(processor=graphviz_processor)

f = open("graphviz_btree.dot", "w")
f.write(graph)
f.close()

for i in search:
    binary_searcher.set_parameters(value=i)
    rel, node = t.process(processor=binary_searcher)
    if rel == "=" :
        print (str(i) + " is " + node.label)
    elif rel =="<" :
        print (str(i) + " not found. It must be after " + str(node.value))
    else:
        print (str(i) + " not found. It must be before " + str(node.value))

binary_opti_searcher.set_parameters(search="min")
min_node = t.process(processor=binary_opti_searcher)
print("The minimum is " + str(min_node.value))
binary_opti_searcher.set_parameters(search="max")
max_node = t.process(processor=binary_opti_searcher)
print("The maximum is " + str(max_node.value))
