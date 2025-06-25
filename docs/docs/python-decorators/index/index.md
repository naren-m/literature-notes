---
layout: "default"
title: "Python Decorators"
word_count: 64
created: "2025-06-25T14:36:45.470864"
modified: "2025-06-25T14:36:45.470864"
backlinks:
  - title: "Design Patterns"
    url: "cse/design_patterns/design_patterns/"
breadcrumbs:
  - title: "Home"
    url: "/"
  - title: "Docs"
    url: "/topics/docs//"
  - title: "Python Decorators"
    url: "/topics/docs/python-decorators//"
---
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

