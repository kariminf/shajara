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

from trees import NodeProcessor, Node

class DecisionProcessor(NodeProcessor):

    def __init__(self, X, Y, stop_fun, split_fun):
        self.X = X
        self.Y = Y
        self.stop_fun = stop_fun
        self.split_fun = split_fun

    def root_init(self, root):
        setattr(root, "X", self.X)
        setattr(root, "Y", self.Y)

    def root_final(self, root):
        pass

    def child_pre_process(self, node, key):
        return False

    def child_post_process(self, node, child_key):
        return False

    def pre_process(self, node):
        test, test_res, attr = self.stop_fun(node.X, node.Y)
        if test:
            for val in attr:
                setattr(node, val, attr[val])
            return []
        sets = self.split_fun(node.X, node.Y, test_res)
        for key in sets:
            the_set = sets[key]
            child = Node(value=the_set.value, label=the_set.label)
            setattr(child, "X", the_set.X)
            setattr(child, "Y", the_set.Y)
            node.children[key] = child
        return node.children.keys()

    def post_process(self, node):
        pass

    def result(self):
        pass
