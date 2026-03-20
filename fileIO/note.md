## File I/O — Complete Summary

---

### 1. What File I/O Is

File I/O means **Input/Output** — reading data from files and writing data to files. Almost every real program does this. Configuration files, logs, CSVs, JSON data — all of it lives on a filesystem and needs to be read or written.

---

### 2. Opening Files — The `open()` Function

Everything starts with `open()`. The second argument is the **mode**:

| Mode | Meaning | Creates if missing? | Overwrites? |
|---|---|---|---|
| `"r"` | Read | No — raises `FileNotFoundError` | No |
| `"w"` | Write | Yes | Yes — destroys existing content |
| `"a"` | Append | Yes | No — adds to end |
| `"x"` | Create | Fails if file exists | N/A |
| `"r+"` | Read and Write | No | No |
| `"rb"` | Read binary | No | No |
| `"wb"` | Write binary | Yes | Yes |

Binary modes are for non-text files — images, PDFs, audio.

---

### 3. Always Use `with` — Context Managers

The only professional way to open files:

```python
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

- Automatically closes the file when the block ends — even if an exception occurs
- Without it, a crash mid-read leaves the file open — consuming resources and potentially corrupting data
- Always specify `encoding="utf-8"` to avoid platform-specific bugs

---

### 4. Reading Files — Four Ways

**`.read()`** — entire file as one string. Good for small files:
```python
content = f.read()
```

**`.readline()`** — one line at a time. Each call advances the pointer:
```python
first_line = f.readline()
second_line = f.readline()
```

**`.readlines()`** — all lines as a list. Each line includes `\n`:
```python
lines = f.readlines()
# Strip newlines with: [line.strip() for line in lines]
```

**Iterating directly** — best for large files, reads one line at a time without loading everything into memory:
```python
for line in f:
    print(line.strip())
```

---

### 5. Writing Files

**`.write()`** — writes a string. No automatic newline — include `\n` yourself:
```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, world.\n")
```

**`.writelines()`** — writes a list of strings. Still no automatic newlines:
```python
lines = ["line one\n", "line two\n"]
with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)
```

**Append mode** — adds to end without destroying existing content:
```python
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("New log entry.\n")
```

---

### 6. `pathlib` — Modern Path Handling

The professional standard for working with file paths. Cross-platform — no worrying about `\` vs `/`:

```python
from pathlib import Path

path = Path("files/data.txt")

path.exists()          # True or False
path.is_file()         # True
path.is_dir()          # False
path.name              # "data.txt"
path.stem              # "data"
path.suffix            # ".txt"
path.parent            # Path("files")

# Build paths safely
base = Path("project")
data = base / "data" / "file.txt"   # project/data/file.txt

# Create directories
Path("new_folder").mkdir(exist_ok=True)
Path("a/b/c").mkdir(parents=True, exist_ok=True)

# List files
for file in Path(".").glob("*.py"):
    print(file)

# Read and write directly
path.read_text()
path.write_text("Hello.\n")
```

**Key lesson from exercises** — use `path.exists()` to check before opening rather than relying purely on catching `FileNotFoundError`.

---

### 7. CSV Files

**Reading with `DictReader`** — each row becomes a dictionary using the header row as keys:
```python
import csv

with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    students = list(reader)   # convert inside the with block — reader dies when file closes
```

**Important** — CSV reads everything as strings. Convert numeric fields manually:
```python
for student in students:
    student['score'] = int(student['score'])
```

**Writing with `DictWriter`** — pass fieldnames and use `writeheader()` then `writerows()`:
```python
with open("output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "subject", "score"])
    writer.writeheader()
    writer.writerows(students)
```

`newline=""` is required to prevent extra blank lines on Windows.

---

### 8. JSON Files

Four functions — the `s` indicates string, no `s` indicates file:

| Function | Direction | Works With |
|---|---|---|
| `json.loads()` | JSON string → Python dict | String variable |
| `json.dumps()` | Python dict → JSON string | String variable |
| `json.load()` | JSON file → Python dict | File object |
| `json.dump()` | Python dict → JSON file | File object |

```python
import json

# Reading
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Writing
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)   # indent=4 for readable formatting
```

**Key lesson from exercises** — opening a file in `"w"` mode immediately clears it even before writing. If your program crashes before `json.dump` runs, you're left with an empty file that causes `JSONDecodeError` on the next read.

---

### 9. File Pointer & Seeking

Python tracks your position in the file as you read:

```python
with open("file.txt", "r") as f:
    first = f.read()    # reads everything — pointer at end
    second = f.read()   # returns "" — pointer still at end

    f.seek(0)           # reset to beginning
    third = f.read()    # reads everything again
```

---

### 10. Encoding

Always specify explicitly — the system default varies by platform:

```python
open("file.txt", "r", encoding="utf-8")   # always explicit
```

UTF-8 handles virtually all characters including non-English ones.

---

### Golden Rules of File I/O

- **Always use `with`** — never open files without it
- **Always specify `encoding="utf-8"`** — on every text file
- **Use `pathlib` for paths** — never concatenate path strings manually
- **Use `path.exists()` proactively** — check before opening
- **Convert CSV values** — everything comes back as a string
- **Convert inside the `with` block** — `DictReader` is tied to the open file
- **Use `json.load/dump` for files** — not `loads/dumps`
- **Iterate line by line for large files** — never `.read()` a potentially huge file

---
