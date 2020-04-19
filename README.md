# Shajara

<img align="left" src="assets/shajara-logo.svg" width="100" height="100">
**Shajara** means "Tree" in Arabic.
It is a project for manipulating trees.
There is a tree, there is a node and there is node processor.

[![Project](https://img.shields.io/badge/Project-Shajara-0BDA51.svg?style=plastic)](https://kariminf.github.io/shajara/)
[![License](https://img.shields.io/badge/License-MIT-0BDA51.svg?style=plastic)](https://opensource.org/licenses/MIT)
[![PyPI](https://img.shields.io/pypi/v/shajara.svg?style=plastic)](https://pypi.python.org/pypi/shajara)
[![Downloads](https://img.shields.io/pypi/dm/shajara.svg?style=plastic)](https://pypi.org/project/shajara/)
[![Python version](https://img.shields.io/pypi/pyversions/shajara.svg?style=plastic)](https://pypi.org/project/shajara/)
[![Documentation Status](https://readthedocs.org/projects/shajara/badge/?version=latest)](https://shajara.readthedocs.io/en/latest/?badge=latest)
[![Travis](https://img.shields.io/travis/kariminf/shajara.svg?style=plastic)](https://travis-ci.org/kariminf/shajara)
[![Codecov](https://img.shields.io/codecov/c/github/kariminf/shajara.svg?style=plastic)](https://codecov.io/gh/kariminf/shajara)
[![CodeFactor](https://www.codefactor.io/repository/github/kariminf/shajara/badge/master)](https://www.codefactor.io/repository/github/kariminf/shajara/overview/master)
[![codebeat badge](https://codebeat.co/badges/9ea7f2f7-58cb-4df9-b4b7-33d33aee07aa)](https://codebeat.co/projects/github-com-kariminf-shajara-master)
[![Code Climate](https://img.shields.io/codeclimate/maintainability-percentage/kariminf/shajara.svg?style=plastic)](https://codeclimate.com/github/kariminf/shajara/)
<br clear="left"/>

## Description

A tree has one node which represents its root.
Each node has a label, a value and many children.
The arc from the parent to the child is labeled.


## Create a tree

### Using shajara API

```python
from shajara import Tree, Node

#create a tree with a root labeled "a"
t = Tree(label="a")
# add childrend "b", "c" and "d" to "a"
t.add_child("ab", Node(label="b")).add_child("ac", Node(label="c")).add_child("ad", Node(label="d"))
# go to child "b" and add to it children "e" and "f"
t.select_child("ab").add_child("be", Node(label="e")).add_child("bf", Node(label="f"))
# go up to "a", go to child "d" and add to it children "g" and "h"
t.up().select_child("ad").add_child("dg", Node(label="g")).add_child("dh", Node(label="h"))
```

![](assets/readme/shajara_api.png)

### Using a dict representation

```python
from shajara.create import GenerateProcessor
from shajara.plot import graphviz_processor
from shajara import Tree

# the tree representation : the arcs must be labeled
rep = {
    "label": "a",
    "children": {
        "ab": {
            "label": "b",
            "children": {
                "be": {"label": "e"},
                "bf": {"label": "f"}
            }
        },
        "ac": {"label": "c"},
        "ad": {"label": "d"}
    }
}

# Create a generator to this representation
generator = GenerateProcessor(rep)
#create an ampty tree (acrually the root exists without a label or a value)
t = Tree()
#fill the tree using the generator
t.process(processor=generator)
```

![](assets/readme/generate_api.png)

## Visualize a tree

DOT description of a tree for Graphviz can be generated using **GraphvizProcessor**

```python
from shajara.plot import graphviz_processor

# create the tree t using one of the methods above
...
#process the tree using graphviz_processor, which returns a DOT description (string)
graph = t.process(processor=graphviz_processor)

# save the description in a file with extension .dot
f = open("graphviz.dot", "w")
f.write(graph)
f.close()

```

## Binary search trees (not balanced)

### Create unbalanced binary search trees

```python
from shajara.search import BSearchTree

values = [5, 9, 2, 11, 3, 7, 2]
labels = ["five", "nine", "two", "eleven", "three", "seven", "two_again"]

#create a blank binary tree
t = BSearchTree()

#add the elements using search_add
for i in range(len(values)):
    t.search_add(values[i], label=labels[i], add=True)

```

![](assets/readme/bsearch_api.png)

### Search a value

```python
from shajara.search import binary_searcher

# after creating t
# these are the values we want to search
search = [4, 5, 8, 10, 12]

for i in search:
    #setting the search value to our search pprocessor
    binary_searcher.set_parameters(value=i)
    # processing the tree using this processor will return a bool (found or not), a node (if found: the node with the value; else the node with the nearest value) and a relationship ("=", ">", "<")
    found, node, rel = t.process(processor=binary_searcher)
    if found :
        print (str(i) + " is " + node.label)
    else:
        pos = "before "
        if (rel =="<"):
            pos = "after "
        print (str(i) + " not found. It must be " + pos + str(node.value))

```
The result :
![](assets/readme/bsearch_api_res.png)


## License

MIT License

Copyright (c) 2020 Abdelkrime Aries
