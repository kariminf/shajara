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

from .. import NodeProcessor, Node, Tree

class BSearchProcessor(NodeProcessor):

    def _pre_process(self, node):
        self.node = node
        if node.value < self.value :
            self.rel = "<"
        elif node.value > self.value :
            self.rel = ">"
        else:
            self.found = True

        exit = self.found or not self.rel in node.children

        if self.add:
            if self.found:
                node.label = self.label
            elif not self.rel in node.children:
                if self.rel == ">" and "<" in node.children:
                    lt_child = node.children["<"]
                    del node.children["<"]
                    node.children[">"] = Node(self.value, self.label)
                    node.children["<"] = lt_child
                else:
                    node.children[self.rel] = Node(self.value, self.label)

        if exit :
            return []

        return [self.rel]

    def root_init(self, root):
        self.node = root
        self.found = False

    def result(self):
        return self.found, self.node, self.rel

    def set_parameters(self, value, label="", add=False):
        self.value = value
        self.add = add
        self.label = label
        self.rel = "="

binary_searcher = BSearchProcessor()

class BSearchTree(Tree):

    def __init__(self, value=None, label=None, search_processor=binary_searcher):
        self.root = Node(value, label)
        self.search_processor = search_processor
        self.create_stack = [self.root]
        self.empty = True

    def search_add(self, value, label="", add=False):
        if add and self.empty:
            self.root.value = value
            self.root.label = label
            self.empty = False
            return True, self.root
        self.search_processor.set_parameters(value=value, label=label, add=add)
        return self.process(processor=self.search_processor)

    def add_child(self, label, node):
        return self
