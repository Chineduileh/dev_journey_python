## Modules & Imports — Complete Summary

---

### What a Module Is

A module is simply a Python file. Any `.py` file you create is a module. When your program grows beyond one file, modules are how you organise your code into logical, reusable units. Every time you write `import json` or `from pathlib import Path` you are importing a module.

---

### The Standard Library

Python ships with an enormous collection of built-in modules available on every Python installation with no extra installation needed. The most important ones for your roadmap are `os`, `sys`, `json`, `csv`, `datetime`, `pathlib`, `math`, `random`, `re`, `collections`, `functools`, `typing`, `dataclasses`, `logging`, `unittest`, and `argparse`. Knowing they exist means you reach for them instead of reinventing the wheel.

---

### Import Styles

There are four ways to import and each has its place.

**Basic import** — imports the whole module. Clearest style because the module name always appears before what you're using:
```python
import json
data = json.loads('{"name": "Chinedu"}')
```

**From import** — imports specific names directly. Cleaner when you use something frequently but loses clarity about where the name came from:
```python
from json import loads, dumps
data = loads('{"name": "Chinedu"}')
```

**Import with alias** — renames the module. Used when a module name is long or has a widely accepted community abbreviation like `numpy as np` or `pandas as pd`:
```python
import datetime as dt
```

**Star import** — imports everything from a module. Almost never use this in professional code. It pollutes your namespace and makes it impossible to know where any given name came from:
```python
from json import *   # avoid
```

---

### How Python Finds Modules

When you write `import json`, Python searches in this exact order: the current directory, `PYTHONPATH` environment variable, the standard library, and site-packages where pip installs third-party packages. Never name your files the same as standard library modules — a file called `json.py` in your project folder will shadow Python's built-in `json` and break things silently.

---

### Creating Your Own Modules

Any `.py` file you create is importable as a module by any other file in the same directory. Define functions, classes, and constants in one file and import them into another. Keep related functionality together — string utilities in one file, math utilities in another, file utilities in another.

---

### `__name__` and `if __name__ == "__main__"`

Every Python module has a built-in `__name__` variable. When you run a file directly with `python main.py`, `__name__` is set to `"__main__"`. When a file is imported by another file, `__name__` is set to the module's name. This distinction lets you write code that only runs when the file is executed directly — never when it's imported:

```python
def my_function():
    pass

if __name__ == "__main__":
    my_function()   # only runs when this file is run directly
```

You will write this at the bottom of almost every Python script you create. It is the standard entry point pattern.

---

### Packages

A package is a folder containing multiple modules. It must contain a file called `__init__.py` to tell Python to treat the folder as a package. Without `__init__.py` Python does not recognise the folder as something you can import from.

`__init__.py` serves two purposes. First it marks the folder as a package. Second it controls what gets exposed when someone imports your package — by putting imports inside it you decide what's accessible directly from the package name without knowing which submodule something lives in:

```python
# student_utils/__init__.py
from .grades import assign_grade
from .stats import average
from .formatter import format_student
```

Now `from student_utils import assign_grade` works directly instead of `from student_utils.grades import assign_grade`.

---

### Relative vs Absolute Imports

Absolute imports use the full path from the project root and are always unambiguous — preferred in professional code:
```python
from student_utils.grades import assign_grade
```

Relative imports use dots to navigate relative to the current file's location. The single dot means "in this same package." Used inside packages to reference sibling modules:
```python
from .grades import assign_grade      # sibling module
from ..other_package import something  # up one level
```

---

### Third-Party Packages and pip

Everything beyond the standard library is installed with pip:
```bash
pip install requests
pip install fastapi
pip install pandas
```

Packages install into your environment's site-packages folder. Always use a virtual environment so package versions don't conflict between projects.

---

### `requirements.txt`

The standard way to record a project's dependencies so anyone can reproduce your environment:
```bash
pip freeze > requirements.txt        # capture all installed packages
pip install -r requirements.txt      # install everything from the file
```

Always commit `requirements.txt` to your repo. Never commit your virtual environment folder.

---

### `__pycache__`

Python automatically compiles your modules into bytecode and stores the result in a `__pycache__` folder as `.pyc` files. This makes subsequent runs faster — Python loads the compiled version instead of recompiling from scratch if the source hasn't changed. Never manually edit anything inside it. It is already in your Python `.gitignore` so it will never be committed to GitHub.

---

### The `collections` Module

A standard library module with data structures worth knowing early.

`Counter` counts occurrences of items in any iterable and has a `most_common()` method for finding the most frequent items. `defaultdict` is a dictionary that never raises `KeyError` — it returns a default value for missing keys, which is useful for grouping and accumulating data. `namedtuple` creates tuple subclasses with named fields — giving you the immutability of a tuple with the readability of named attributes.

---

### The `logging` Module

In production code `print()` is replaced with `logging`. It gives you severity levels — `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` — so you can filter output by importance. It adds timestamps automatically, can write to files, and produces consistent structured output. You set the level once and everything below that level is silently suppressed — so debug noise disappears in production without changing any code.

---

### Golden Rules of Modules and Imports

Never name your files the same as standard library modules. Always use `if __name__ == "__main__"` as your script entry point. Prefer absolute imports over relative imports for clarity. Always use a virtual environment — never install packages globally for a specific project. Always commit `requirements.txt` and always add your virtual environment folder to `.gitignore`. Keep modules focused — one file should have one clear responsibility.