#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shajara.search.trie import trie_adder, trie_searcher
from shajara import Tree

strings = ["to", "ten", "inn", "in", "tea", "A"]
root_keys = ["t", "i", "A"]
t = Tree()
search = ["tell", "tea", "inner"]
founds = ["te", "tea", "inn"]
in_dic = [False, True, True]

def test_trie_adder():
    for string in strings:
        trie_adder.set_parameters(string)
        t.process(processor=trie_adder)
    assert list(t.root.children.keys()) == root_keys
    assert not t.root.value
    assert t.root.children["t"].children["o"].value

def test_trie_searcher():
    for i in range(len(search)):
        string = search[i]
        trie_searcher.set_parameters(string)
        found, node = t.process(processor=trie_searcher)
        assert found == founds[i]
        assert node.value == in_dic[i]
