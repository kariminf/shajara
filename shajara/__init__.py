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

from collections import OrderedDict

version = "0.1"
release = "0.1.0"

class NodeProcessor(object):

    def _pre_process(self, node):
        pass

    def _post_process(self, node):
        pass

    def _child_pre_process(self, node, child_key):
        return False

    def _child_post_process(self, node, child_key):
        return False

    def root_init(self, root):
        pass

    def root_final(self, root):
        pass
    
    def result(self):
        pass

    def process(self, node):
        children_keys = self._pre_process(node)
        for child_key in children_keys:
            if self._child_pre_process(node, child_key):
                next
            if self.process(node.children[child_key]):
                next
            if self._child_post_process(node, child_key):
                break
        self._post_process(node)

def_processor = NodeProcessor()

class Node(object):
    def __init__(self, value=0, label=""):
        self.label = label
        self.value = value
        self.children = OrderedDict()

    def append_child(self, label, node):
        self.children[label] = node
        return self


class Tree(object):
    """Generic tree representation

    Parameters
    ----------
    value : type
        the value of the root node
    label : type
        the label of the root node

    Attributes
    ----------
    root : Node
        The root node
    node_stack : array
        the stack for browsing nodes

    """

    def __init__(self, value=0, label=""):
        self.root = Node(value, label)
        self.node_stack = [self.root]

    def get_root(self):
        """Returns the root of the tree

        Parameters
        ----------


        Returns
        -------
        Node
            The root of the tree if it exists or None

        """
        return self.root

    def process(self, processor=def_processor):
        """Short summary.

        Parameters
        ----------
        processor : NodeProcessor
            the processor used to manipulate the tree starting from its root

        Returns
        -------
        type
            The result of processing, it can be None, a node, a string, etc.

        """
        processor.root_init(self.root)
        processor.process(self.root)
        processor.root_final(self.root)
        return processor.result()

    def add_child(self, label, node):
        """Adds a child to the current node.
        To browse the nodes use select_child and up

        Parameters
        ----------
        label : str or int
            The label of the arc
        node : Node
            The node to add as a child

        Returns
        -------
        Tree
            this object

        """
        current = self.node_stack[-1]
        current.append_child(label, node)
        return self

    def select_child(self, label):
        """Select a child node of the current one, using its label.
        Used to browsing the tree down.

        Parameters
        ----------
        label : str or int
            the label of the label of the arc

        Returns
        -------
        Tree
            this object

        """
        current = self.node_stack[-1]
        current = current.children[label]
        if current:
            self.node_stack.append(current)
        return self

    def up(self):
        """Select the parent of the current node.
        Used to browsing the tree up.

        Parameters
        ----------


        Returns
        -------
        type
            this object

        """
        if len(self.node_stack) > 1:
            self.node_stack.pop()
        return self

    def current_node(self):
        """Returns the current node

        Parameters
        ----------


        Returns
        -------
        Node
            The current node

        """
        return node_stack[-1]
