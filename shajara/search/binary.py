#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import NodeProcessor, Node, Tree

class BSearchProcessor(NodeProcessor):

    def _pre_process(self, node):
        self._current_node = node
        if node.value < self._search_value :
            self._rel = "<"
        elif node.value > self._search_value :
            self._rel = ">"

        if self._rel not in node.children:
            return []

        return [self._rel]

    def init(self, tree):
        self._current_node = tree.root
        return self._current_node is None

    def result(self):
        return self._rel, self._current_node

    def set_parameters(self, value):
        self._search_value = value
        self._rel = "="

binary_searcher = BSearchProcessor()

class BAddProcessor(BSearchProcessor):

    def _pre_process(self, node):
        path = super()._pre_process(node)

        if not path:
            if self._rel == "=":
                node.label = self._add_node.label
            else:
                if self._rel == ">" and "<" in node.children:
                    lt_child = node.children["<"]
                    del node.children["<"]
                    node.children[">"] = self._add_node
                    node.children["<"] = lt_child
                else:
                    node.children[self._rel] = self._add_node

        return path

    def init(self, tree):
        self._current_node = tree.root
        if tree.root is None:
            tree.root = self._add_node
            return True
        return False

    def set_parameters(self, node):
        self._search_value = node.value
        self._add_node = node
        self._rel = "="

binary_adder = BAddProcessor()


class BOptiSearchProcessor(NodeProcessor):

    def _pre_process(self, node):
        self._current_node = node

        if self._rel not in node.children:
            return []

        return [self._rel]

    def init(self, tree):
        self._current_node = tree.root
        return self._current_node is None

    def result(self):
        return self._current_node

    def set_parameters(self, search="min"):
        self._rel = "<"
        if search == "min":
            self._rel = ">"

binary_opti_searcher = BOptiSearchProcessor()
