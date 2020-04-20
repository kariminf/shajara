#!/usr/bin/env python
# -*- coding: utf-8 -*-


from . import NodeProcessor

class GraphvizProcessor(NodeProcessor):
    """Generates DOT representation of a tree"""

    def __fill_node(self, node):
        self.nbr += 1
        nid = 'N' + str(self.nbr)
        self.graph += nid + '[label="' + node.label + '"];\n'
        return nid

    def _pre_process(self, node):
        if len(self.father_id) == 0:
            self.father_id.append(self.__fill_node(node))
        return node.children.keys()

    def _child_pre_process(self, node, key):
        nid = self.__fill_node(node.children[key])
        self.graph += self.father_id[-1] + ' -> ' + nid + ' [label="' + key + '"];\n'
        self.father_id.append(nid)
        return False

    def _child_post_process(self, node, child_key):
        self.father_id.pop()
        return False

    def init(self, tree):
        self.nbr = 0
        self.graph = "digraph Tree {\nnode [shape=box] ;\n"
        self.father_id = []
        return False

    def final(self, tree):
        self.graph += "}"

    def result(self):
        return self.graph

graphviz_processor = GraphvizProcessor()
