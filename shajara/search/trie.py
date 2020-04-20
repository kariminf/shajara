#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import NodeProcessor, Node, Tree

class TrieSearchProcessor(NodeProcessor):

    def _pre_process(self, node):
        self._current_node = node
        if not self._search_string:
            return []
        char = self._search_string[0]
        self._search_string = self._search_string[1:]
        return [char]

    def _child_pre_process(self, node, child_key):
        if child_key in node.children:
            self._found_string += child_key
        return child_key not in node.children

    def init(self, tree):
        self._current_node = tree.root
        return self._current_node is None

    def result(self):
        return self._found_string, self._current_node

    def set_parameters(self, string):
        self._search_string = string
        self._found_string = ""

trie_searcher = TrieSearchProcessor()

class TrieAddProcessor(TrieSearchProcessor):

    def _post_process(self, node):
        if not self._search_string:
            self._current_node.value = True
            self._current_node.label = "True"

    def _child_pre_process(self, node, child_key):
        if child_key not in node.children:
            node.children[child_key] = Node(value=False, label="False")
        return False

    def init(self, tree):
        if tree.root is None:
            tree.root = Node(value=False, label="False")
        self._current_node = tree.root
        return False

    def set_parameters(self, string):
        self._search_string = string
        self._found_string = ""

trie_adder = TrieAddProcessor()


class AutocompleteProcessor(TrieSearchProcessor):
    pass
