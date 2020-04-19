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

    def root_init(self, root):
        self.__fill_node(root, self.rep)
