#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Copyright 2020 Abdelkrime Aries <kariminfo0@gmail.com>
#
#  ---- AUTHORS ----
# 2020	Abdelkrime Aries <kariminfo0@gmail.com>
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

from trees import NodeProcessor

class GraphvizProcessor(NodeProcessor):

    def root_init(self):
        self.nbr = 0
        self.graph = "digraph Tree {\nnode [shape=box] ;\n"
        self.father_id = []

    def root_final(self):
        self.graph += "}"

    def _fill_node(self, node):
        self.nbr += 1
        nid = 'N' + str(self.nbr)
        self.graph += nid + '[label="' + node.label + '"];\n'
        return nid

    def child_pre_process(self, node, key):
        nid = self._fill_node(node.children[key])
        self.graph += self.father_id[-1] + ' -> ' + nid + ' [label="' + key + '"];\n'
        self.father_id.append(nid)
        return False

    def child_post_process(self, node, child_key):
        self.father_id.pop()
        return False

    def pre_process(self, node):
        if len(self.father_id) == 0:
            self.father_id.append(self._fill_node(node))
        return node.children.keys()

    def post_process(self, node):
        #self.father_id.pop()
        pass

    def result(self):
        return self.graph

graphviz_processor = GraphvizProcessor()
