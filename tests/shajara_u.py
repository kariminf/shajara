#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Copyright 2020 Abdelkrime Aries <kariminfo0@gmail.com>
#
#  ---- AUTHORS ----
#  2020	Abdelkrime Aries <kariminfo0@gmail.com>
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

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shajara import Tree, Node


def test_node():
    n = Node(value=1, label="n1")
    assert n.value == 1
    assert n.label == "n1"
    n.append_child("c1", Node(label="n2"))
    n.append_child("c2", Node(label="n3"))
    n.append_child("c3", Node(label="n4"))
    order = ["n2", "n3", "n4"]
    order_arcs = ["c1", "c2", "c3"]
    # verify the order
    i = 0
    for arc in n.children:
        assert arc == order_arcs[i]
        assert n.children[arc].label == order[i]
        i += 1

#TODO test Tree
