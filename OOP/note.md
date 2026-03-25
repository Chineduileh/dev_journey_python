## OOP — Complete Summary

---

### What OOP Is

OOP bundles related data and the functions that operate on it into a single unit called a **class**. A class is a blueprint. Every object created from that blueprint is an **instance** — independent, with its own data.

---

### Classes and Instances

A class defines the structure. An instance is the actual object built from it. Two instances built from the same class are completely independent — changing one doesn't affect the other.

---

### `__init__` — The Constructor

Runs automatically every time you create a new instance. This is where you define what data each instance will carry. Every attribute set here with `self` belongs exclusively to that instance.

---

### `self`

`self` is the instance itself — whichever specific object is calling the method. Python passes it automatically as the first argument to every instance method. You never pass it manually but you must always include it in method definitions. `self.name = name` means "store this value on this specific instance."

---

### Instance Attributes vs Class Attributes

Instance attributes are defined with `self` inside `__init__` — each instance has its own separate copy. Class attributes are defined directly on the class outside any method — shared across all instances. A class attribute is useful for things like counters or constants that belong to the class concept, not any specific object.

---

### Instance Methods

Functions defined inside a class that always receive `self` as the first parameter. Through `self` they have full access to the instance's data and can call other methods on the same instance.

---

### Dunder Methods

Special methods Python calls automatically in specific situations. The double underscore marks them as part of Python's protocol system:

`__init__` runs on object creation. `__str__` defines what `print(object)` shows — the human-readable representation. `__repr__` defines the unambiguous debug representation shown in the shell. `__len__` makes `len(object)` work. `__eq__` defines what `==` means between two instances. `__lt__` enables sorting with `sorted()`. `__contains__` makes the `in` operator work on your object.

---

### `@classmethod` and `@staticmethod`

A `@classmethod` receives the class itself as `cls` instead of an instance. It's used for alternative constructors — different ways to create instances from different data sources without overloading `__init__`.

A `@staticmethod` receives neither `self` nor `cls`. It's a plain utility function that lives inside the class purely for organisational reasons. It has no access to the class or any instance.

---

### Inheritance

A child class inherits all attributes and methods of its parent and can extend or override them. The child gets everything the parent has for free — it only needs to define what's different or additional about itself.

---

### `super()`

Gives you access to the parent class from inside the child. Most commonly used to call the parent's `__init__` from the child's `__init__` — delegating the shared setup upward and then adding child-specific attributes after.

---

### Method Overriding

When a child class defines a method with the same name as the parent, the child's version runs instead. The parent's version is not lost — you can still access it via `super()` if needed.

---

### `isinstance()` and `issubclass()`

`isinstance(object, Class)` checks if an object is an instance of a class or any of its parents. `issubclass(Child, Parent)` checks if one class inherits from another. Both are useful when you have mixed collections of objects and need to handle them differently.

---

### Encapsulation

Controlling what's accessible from outside the class. Public attributes have no underscore and are accessible everywhere. Protected attributes use a single underscore `_` as a convention meaning "internal — handle carefully." Private attributes use double underscore `__` and Python mangles the name to make external access harder. Encapsulation protects your object's internal state from being modified in ways you didn't intend.

---

### `@property`

Lets you access a method like an attribute. A getter controls how a value is read. A setter controls how a value is written — letting you add validation before the value is stored. This gives you control over your data while keeping clean attribute-style access rather than ugly `get_x()` and `set_x()` calls.

---

### Composition vs Inheritance

Inheritance is an "is-a" relationship — a Student is a Person. Composition is a "has-a" relationship — a Student has a Course. When the relationship is "has-a", prefer composition — it stays more flexible and avoids deeply nested, brittle inheritance hierarchies.

---

### `@dataclass`

A decorator that auto-generates `__init__`, `__repr__`, and `__eq__` from class-level type annotations — eliminating boilerplate for data-holding classes. You still add custom methods normally. Standard in modern Python for any class whose primary purpose is holding data.

---

### The Golden Rules of OOP

Write classes when you have data and behaviour that naturally belong together. Prefer composition over inheritance when the relationship is "has-a" not "is-a". Keep `__init__` simple — it should set attributes, not do complex work. Use `@property` instead of public attributes whenever validation matters. Never expose internal state directly when a method can protect it. Name classes with CapitalCase, methods and attributes with lowercase_underscore.