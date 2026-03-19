FUNCTIONS

---

1. What a Function Is

A function is a reusable block of code that you define once and call as many times as you need. The core purpose is to avoid repetition and organise logic into named, meaningful units.

```python
def greet(name):
    print(f"Hello, {name}.")
```

---

2. Parameters vs Arguments

- Parameter — the variable name in the function definition
- Argument — the actual value passed when calling the function

```python
def add(a, b):    # a and b are parameters
    return a + b

add(3, 5)         # 3 and 5 are arguments
```

---

3. The `return` Statement

- A function always returns something
- Without `return`, it returns `None` by default
- `return` hands a value back to the caller and stops the function immediately
- `print` displays output but returns `None` — the value is thrown away

```python
def multiply(a, b):
    return a * b          # returns the value

def bad_multiply(a, b):
    print(a * b)          # displays but returns None
```

---
4. Default Arguments

Parameters can have fallback values used when the caller doesn't provide them. Default arguments must always come after non-default arguments:

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}."

greet("Chinedu")            # Hello, Chinedu.
greet("Chinedu", "Hey")     # Hey, Chinedu.
```

---

5. Keyword Arguments

Arguments can be passed by name instead of position, allowing you to skip defaults selectively:

```python
def create_profile(name, role="Student", country="Nigeria"):
    print(name, role, country)

create_profile("Chinedu", country="Ghana")
# Chinedu Student Ghana
```

---
6. `*args` — Variable Positional Arguments

Collects any number of positional arguments into a **tuple** inside the function:

```python
def add_all(*numbers):
    return sum(numbers)

add_all(1, 2, 3, 4, 5)   # 15
```

- The `*` does the packing — the name `args` is convention, not required
- You can combine with regular parameters: regular args first, `*args` after

---

7. `**kwargs` — Variable Keyword Arguments

Collects any number of keyword arguments into a **dictionary** inside the function:

```python
def display_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

display_profile(name="Chinedu", role="Developer")
```

- The `**` does the packing — `kwargs` is convention, not required
- Combined order is always: `regular → *args → **kwargs`

---

8. Scope — The LEGB Rule

Python searches for variable names in this exact order:

- L — Local** — variables defined inside the current function
- E — Enclosing** — variables in the outer function when functions are nested
- G — Global** — variables defined at the top level of the script
- B — Built-in** — Python's own names: `print`, `len`, `range`, `sum` etc.

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)    # local
    inner()
    print(x)        # enclosing

outer()
print(x)            # global
```

---

9. Avoiding `global` — Three Clean Approaches

| Situation | Approach |
|---|---|
| One or two functions | Pass and return |
| Multiple functions on a list or dict | Mutable object — modify in place |
| Complex program with shared state | Class with `self` |

---

10. Functions as First-Class Objects

Functions are objects in Python. You can:
- Assign them to variables
- Pass them as arguments to other functions
- Return them from functions

```python
def apply(func, value):
    return func(value)

apply(str.upper, "hello")   # HELLO
```

This is what makes `sorted(users, key=some_function)` possible.

---

11. Lambda Functions

A small, anonymous, single-expression function written inline:

```python
# These are identical
def square(x): return x ** 2
square = lambda x: x ** 2
```

Most useful as inline arguments to functions like `sorted()`:

```python
sorted(products, key=lambda p: p["price"], reverse=True)
```

- Lambda parameter = each individual item from the collection
- Can only contain a single expression — no loops, no multiple lines

---

12. Docstrings

Written immediately after the function definition. Part of the function object itself — not a comment:

```python
def calculate_tax(amount: float, rate: float = 0.075) -> float:
    """
    Calculate tax on a given amount.

    Args:
        amount: The base amount before tax.
        rate: Tax rate as a decimal. Defaults to 7.5%.

    Returns:
        The calculated tax amount.
    """
    return amount * rate
```

Every function you write professionally should have one.

---

13. Type Hints

Annotate what types a function expects and returns:

```python
from typing import Any, Optional, List

def find_user(user_id: int, users: List[dict]) -> Optional[dict]:
```

- `parameter: type` for inputs
- `-> type` for return value
- `Optional[X]` means X or None
- `Any` means any type — used for mixed-type collections like `**kwargs`
- Python doesn't enforce them at runtime but they are professional standard and required by FastAPI

The Golden Rules of Functions

- If you've written the same logic twice — it should be a function
- If a function does more than one thing — split it
- Always `return` — never rely on `print` for values you need to use
- Every function gets a docstring and type hints in professional code
- Default arguments after non-default, `*args` before `**kwargs` — always

