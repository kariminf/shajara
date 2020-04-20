#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import NodeProcessor, Node

class GenerateProcessor(NodeProcessor):
    """Generates a tree given a representation using dictionaries

    Parameters
    ----------
    rep : dict
        A dictionary representing the tree

    Attributes
    ----------
    rep

    """

    def __init__(self, rep):
        self.rep = rep

    def __fill_node(self, node, rep):
        for val in rep:
            setattr(node, val, rep[val])

    def _pre_process(self, node):
        if not node.children:
            return []
        return node.children.keys()

    def _child_pre_process(self, node, key):
        child = Node()
        self.__fill_node(child, node.children[key])
        node.children[key] = child
        return False

    def _child_post_process(self, node, child_key):
        return False

    def init(self, tree):
        if not tree.root:
            tree.root = Node()
            self.__fill_node(tree.root, self.rep)
            tree._node_stack.append(tree.root)
        return False
