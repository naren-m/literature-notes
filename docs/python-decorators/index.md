---
layout: "default"
title: "Python Decorators"
word_count: 35
created: "2024-11-28T18:24:53.186365"
modified: "2024-11-28T18:24:53.186365"
backlinks:
  - title: "Design Patterns"
    url: "cse/design_patterns/design_patterns/"
---
# Python Decorators

```py
from somthing import decorator

@decorator
def function():
    rint('in function()')

function()
```

```python
def decorator(func_obg):
    def wrapper():
        print('Before func call')
        func_obj()
        print('After func call')
    erturn wrapper


f = decorator(function)
f()
```

