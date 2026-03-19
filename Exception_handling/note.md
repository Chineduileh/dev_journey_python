# Error Handling in Python — Complete Summary

---

## 1. Why Error Handling Exists

Every program will eventually encounter unexpected input, missing files, network failures, or invalid operations. Without error handling, any of these crashes your entire program with an ugly traceback and zero explanation to the user.

Error handling lets you **anticipate** what can go wrong, **catch** it when it does, and **respond** intelligently instead of crashing.

---

## 2. The Python Exception Hierarchy

Errors in Python are objects — instances of exception classes that inherit from `BaseException`. The ones you'll deal with daily all inherit from `Exception`:

```
BaseException
└── Exception
    ├── ValueError        — right type, wrong value e.g int("hello")
    ├── TypeError         — wrong type entirely e.g 1 + "hello"
    ├── KeyError          — dictionary key doesn't exist
    ├── IndexError        — list index out of range
    ├── AttributeError    — attribute doesn't exist
    ├── NameError         — variable doesn't exist
    ├── FileNotFoundError — file doesn't exist
    ├── ZeroDivisionError — dividing by zero
    ├── ImportError       — module can't be found
    └── RuntimeError      — general runtime error
```

---

## 3. The `try / except` Block

The fundamental structure of error handling:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero.")
```

- Python attempts everything inside `try`
- The moment an error occurs, it stops and jumps to the matching `except` block
- If no error occurs, the `except` block is skipped entirely

---

## 4. Catching Multiple Exceptions

Handle different errors differently:

```python
try:
    result = a / b
except ZeroDivisionError:
    print("Cannot divide by zero.")
except TypeError:
    print("Both values must be numbers.")
```

Catch multiple exceptions in one block when you'd handle them the same way:

```python
except (ValueError, TypeError):
    print("Invalid input provided.")
```

---

## 5. Accessing the Exception Object

Use `as e` to capture the exception and read its message:

```python
try:
    number = int("hello")
except ValueError as e:
    print(f"Something went wrong: {e}")
    # Something went wrong: invalid literal for int() with base 10: 'hello'
```

---

## 6. The `else` Clause

Runs **only if** the `try` block succeeded — no exception was raised:

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    return result  # only reaches here if no exception occurred
```

Keeps your `try` block minimal — only the risky operation lives there.

---

## 7. The `finally` Clause

Runs **always** — whether an exception occurred or not. Used for cleanup:

```python
try:
    file = open(filename, "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Operation complete.")  # always runs
```

Use `finally` for: closing files, closing database connections, releasing resources.

---

## 8. The Full Structure

```python
try:
    # risky code here — keep this minimal
except SpecificError as e:
    # handle specific error
except AnotherError as e:
    # handle another error
else:
    # runs only if no exception occurred
finally:
    # runs always — cleanup goes here
```

**Most common combinations:**
- `try / except` — basic handling
- `try / except / finally` — when cleanup is needed
- `try / except / else` — when you want to separate success logic clearly

---

## 9. Raising Exceptions

You can raise exceptions yourself when something violates a rule you've defined:

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age
```

- `raise` stops execution immediately
- The exception propagates up to whoever called the function
- The message string is **optional** but always recommended in professional code

### Raising the same exception with different messages

You can raise the same exception type multiple times with different messages:

```python
def create_user(name: str, age: int):
    if not name:
        raise ValueError("Name cannot be empty.")
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age > 150:
        raise ValueError("Age is not realistic.")
```

One `except ValueError` block catches all three — the message tells you which one fired.

### When to raise vs when to catch

| Scenario | Who Raises It | Do You Catch It |
|---|---|---|
| Built-in error from bad code | Python automatically | Yes, if you want to handle it |
| Built-in error from your own rule | You raise it manually | Yes, whoever calls the function |
| Custom exception | You raise it manually | Yes, whoever calls the function |

---

## 10. Creating Custom Exceptions

For professional code, define your own exception types that communicate exactly what went wrong:

```python
class EmptyFileError(Exception):
    def __init__(self, filename):
        self.filename = filename
        super().__init__(f"File '{filename}' is empty.")
```

Then raise and catch it like any other exception:

```python
raise EmptyFileError(filename)

except EmptyFileError as e:
    print(e)
```

### When to use custom exceptions vs built-in

| Situation | Approach |
|---|---|
| Same error type, same response | One `except` block, use message for logging |
| Same error type, different responses | Custom exceptions inheriting from base type |
| Error specific to your application | Custom exception |
| Generic value or type problem | Built-in `ValueError` or `TypeError` |

### Custom exceptions inheriting from built-ins

Custom exceptions can inherit from built-in ones — making them catchable both specifically and generally:

```python
class EmptyNameError(ValueError):
    pass

class InvalidAgeError(ValueError):
    pass

# Catch specifically
except EmptyNameError:
    # handle empty name

# Or catch all ValueErrors including your custom ones
except ValueError:
    # catches EmptyNameError, InvalidAgeError, and any other ValueError
```

---

## 11. Exception Chaining

Preserve the original error context when raising a new exception:

```python
try:
    data = int("hello")
except ValueError as e:
    raise RuntimeError("Failed to process data.") from e
```

`from e` preserves the original `ValueError` in the traceback so you can see both what went wrong at the low level and what it means at the high level.

---

## 12. The `with` Statement — Context Managers

Python's clean solution for resource management — automatically handles setup and teardown:

```python
with open("file.txt", "r") as f:
    content = f.read()
# file is automatically closed here — even if an error occurred
```

Equivalent to `try/finally` but cleaner. Any object implementing `__enter__` and `__exit__` works with `with` — files, database connections, network sockets, locks.

---

## 13. Professional Error Handling Principles

**Keep `try` blocks small** — only wrap the specific line that can fail:
```python
# Bad — too broad
try:
    lots_of_code()
    more_code()
    risky_operation()
except Exception:
    pass

# Good — minimal and specific
try:
    risky_operation()
except SpecificError:
    handle_it()
```

**Never use bare `except`** — catches everything including `KeyboardInterrupt` and `SystemExit`:
```python
# Bad
except:
    pass

# Good
except ValueError:
    handle_it()
```

**Never silently swallow exceptions** — at minimum log what went wrong:
```python
# Bad — error disappears silently
except ValueError:
    pass

# Good — at least acknowledge it
except ValueError as e:
    print(f"Warning: {e}")
```

**Handle exceptions at the right level** — catch where you can do something useful. If a function can't meaningfully handle an error, let it propagate up to a level that can.

---

## 14. Golden Rules of Error Handling

- Always catch **specific** exceptions — never bare `except`
- Keep `try` blocks **minimal** — only the risky line
- Always provide a **message** when raising exceptions in professional code
- Use `else` to separate **success logic** from the `try` block
- Use `finally` for **cleanup** — it always runs
- Use `with` for **resource management** — files, connections, sockets
- Use **custom exceptions** when built-in types aren't specific enough
- Never **swallow** an exception silently — always respond or log