#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shajara.search.trie import trie_adder, trie_searcher
from shajara.plot import graphviz_processor
from shajara import Tree

strings = ["to", "ten", "inn", "in", "tea", "A"]

t = Tree()
for string in strings:
    trie_adder.set_parameters(string)
    t.process(processor=trie_adder)

graph = t.process(processor=graphviz_processor)


f = open("trie_creater.dot", "w")
f.write(graph)
f.close()

search = ["tell", "tea", "inner"]
for string in search:
    trie_searcher.set_parameters(string)
    found, node = t.process(processor=trie_searcher)
    is_word = ""
    if not node.value:
        is_word = " (not in dictionary)"
    print("searching: " + string + ", found: " + found + is_word)
