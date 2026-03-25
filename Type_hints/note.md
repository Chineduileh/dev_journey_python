## Type Hints — Complete Summary

---

### What Type Hints Are

Type hints are annotations that tell you and your tools what types a variable, parameter, or return value should be. Python does not enforce them at runtime — your code runs whether the types are correct or not. They exist for three reasons: they make code self-documenting, they allow tools to catch bugs before runtime, and they are required by FastAPI which uses them to validate request data, generate documentation, and serialise responses.

---

### Basic Annotations

Variables, function parameters, and return types:

```python
name: str = "Chinedu"
age: int = 25
score: float = 85.5
is_active: bool = True

def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old."

def log_message(message: str) -> None:
    print(message)
```

`-> None` means the function returns nothing. Always include it rather than omitting the return annotation — it makes intent explicit.

---

### Collection Types

For lists, dicts, tuples, and sets you annotate the type of their contents. In Python 3.9+ you can use the built-in types directly without importing from `typing`:

```python
# Lists
def average(scores: list[float]) -> float:
    return sum(scores) / len(scores)

# Dicts
def count_words(text: str) -> dict[str, int]:
    ...

# Tuples — specific type at each position
def get_dimensions() -> tuple[int, int]:
    return 1920, 1080

# Sets
def unique_subjects(students: list[dict]) -> set[str]:
    ...
```

For older codebases using Python 3.8 or below you'll see `List`, `Dict`, `Tuple`, `Set` imported from `typing` — same concept, older syntax.

---

### `Optional` — Values That Can Be None

`Optional[X]` means the value is either X or None. One of the most used type hints in real code because functions frequently return None when something isn't found:

```python
from typing import Optional

def find_student(name: str, students: list[dict]) -> Optional[dict]:
    for student in students:
        if student['name'] == name:
            return student
    return None
```

---

### `Union` — Multiple Possible Types

`Union[X, Y]` means the value can be either type X or type Y. In Python 3.10+ you can use the cleaner `|` operator instead:

```python
# Old style
from typing import Union
def process_id(user_id: Union[int, str]) -> str:
    return str(user_id)

# Python 3.10+ style
def process_id(user_id: int | str) -> str:
    return str(user_id)

# Optional is just Union with None
def find(name: str) -> dict | None:
    ...
```

---

### `Any` — Opting Out of Type Checking

Tells the type checker this value can be anything. Use sparingly — it defeats the purpose of type hints. The main legitimate use case is `**kwargs` where values genuinely can be any type:

```python
from typing import Any

def process(**kwargs: Any) -> None:
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

---

### `Callable` — Type Hinting Functions

When a function accepts another function as an argument. The first list is argument types, the second value is the return type:

```python
from typing import Callable

def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)
```

---

### `TypeVar` — Generic Types

When a function works with any type but the input and output types must match:

```python
from typing import TypeVar, List

T = TypeVar('T')

def first_item(items: List[T]) -> T:
    return items[0]
```

If you pass a `List[str]` the return type is `str`. If you pass a `List[int]` the return type is `int`. The type checker understands this relationship.

---

### `Literal` — Restricting to Specific Values

Restricts a parameter to a specific set of allowed values. The type checker flags anything outside that set as an error:

```python
from typing import Literal

def set_direction(direction: Literal["north", "south", "east", "west"]) -> None:
    print(f"Moving {direction}")
```

---

### `TypedDict` — Type Hints for Dictionaries

Defines exactly what keys a dictionary should have and what types their values should be. A halfway point between a plain dict and a full class:

```python
from typing import TypedDict

class Student(TypedDict):
    name: str
    subject: str
    score: int

def process_student(student: Student) -> str:
    return f"{student['name']} scored {student['score']}"
```

---

### `ClassVar` — Class Attributes

Marks a class attribute so the type checker knows it is shared across all instances rather than belonging to a specific instance:

```python
from typing import ClassVar

class Student:
    school: ClassVar[str] = "University of Lagos"
    count: ClassVar[int] = 0
```

---

### `@dataclass` and Type Hints

Dataclasses rely entirely on type hints to generate `__init__`. Every field must be annotated — the annotation is not optional:

```python
from dataclasses import dataclass, field

@dataclass
class Student:
    name: str
    age: int
    scores: list[float] = field(default_factory=list)
    active: bool = True
```

---

### Forward References

When a method returns an instance of its own class, the class isn't fully defined yet. Use a string as the annotation or add `from __future__ import annotations` at the top of the file:

```python
from __future__ import annotations

class Node:
    def __init__(self, value: int, next: Node = None):
        self.value = value
        self.next = next
```

---

### Runtime Type Checking

Type hints don't enforce types at runtime. When you genuinely need enforcement — in public APIs or with user input — use `isinstance`:

```python
def add(a: int | float, b: int | float) -> float:
    if not isinstance(a, (int, float)):
        raise TypeError(f"Expected int or float, got {type(a).__name__}")
    return float(a + b)
```

---

### `mypy` — Static Type Checker

The standard tool for checking type hints without running your code. Reads your annotations and reports type errors — wrong argument types, return type mismatches, incompatible assignments. In professional codebases `mypy` runs as part of CI/CD and code that fails type checking doesn't get merged:

```bash
pip install mypy
mypy main.py
```

Pylance in VS Code does the same thing live as you type.

---

### Golden Rules of Type Hints

Always annotate function parameters and return types — never leave them bare. Use `-> None` explicitly when a function returns nothing. Prefer `X | None` over `Optional[X]` in Python 3.10+. Use `Literal` instead of plain `str` when only specific string values are valid. Use `TypedDict` when a dictionary has a fixed known structure. Use `Any` only as a last resort. Never use type hints as a substitute for runtime validation when input comes from users or external sources.