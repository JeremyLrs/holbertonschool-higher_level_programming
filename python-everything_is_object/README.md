# Understanding Python's Identity, Types, Mutability, and Memory Model

## Introduction

Python looks simple on the surface, but beneath that friendly syntax is
a surprisingly intricate memory model. When I started digging into
concepts such as object identity, mutability, references, and how
arguments are passed to functions, I discovered that understanding these
"under-the-hood" mechanics is essential for writing predictable,
efficient programs.

## ID and Type

Every object in Python has an identity and a type.

``` python
a = 10
b = 10
c = 999
d = 999

print(id(a))
print(id(b))
print(id(c))
print(id(d))
```

``` python
print(type(a))
print(type([]))
```

## Mutable Objects

Mutable objects can be changed in place. Examples include lists,
dictionaries, sets, and bytearrays.

``` python
lst = [1, 2, 3]
print(id(lst))
lst.append(4)
print(id(lst))
```

## Immutable Objects

Immutable objects cannot be changed once created. Examples include
numbers, strings, tuples, frozensets, and bytes.

``` python
x = "hello"
print(id(x))
x = x + " world"
print(id(x))
```

Tuples can still contain mutable objects:

``` python
t = ([1, 2], 3)
t[0].append(4)
print(t)
```

## Why Mutability Matters

Immutable objects allow Python to reuse memory safely, while mutable
objects require unique storage to avoid global side effects.

Memory diagrams:

    x = 5
    y = x

    a = [1, 2]
    b = a

## Assignment vs Reference

Assignment copies references, not objects.

``` python
a = [1, 2, 3]
b = a
a.append(4)
print(b)
```

## Immutable Object Storage

Immutable objects may be reused in memory.

``` python
x = 300
y = 300
print(id(x), id(y))
```

## Argument Passing

Python uses call-by-assignment.

``` python
def add_one(n):
    n += 1
    return n

x = 10
add_one(x)
print(x)
```

``` python
def add_item(lst):
    lst.append(99)

a = [1, 2]
add_item(a)
print(a)
```

## Integer Pre-Allocation

Python pre-allocates integers from -5 to 256 using:

-   NSMALLNEGINTS = 5\
-   NSMALLPOSINTS = 257

``` python
a = 100
b = 100
print(id(a) == id(b))
```

## Aliases

Aliases refer to the same object.

``` python
A = [1, 2, 3]
B = A
A.append(4)
print(B)
```

## Special Case: Tuples and Frozensets

Both are immutable containers that may hold mutable items.

## Conclusion

Understanding Python's object model identity, references, mutability,
and memory allocation clarifies how Python code behaves and prevents
subtle bugs.
