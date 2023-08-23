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

