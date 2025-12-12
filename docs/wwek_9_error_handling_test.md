# Error Handling & Testing with pytest

## 1. Why Error Handling Matters
Error handling makes programs more robust by:
- Preventing crashes
- Providing clear feedback when something goes wrong
- Allowing recovery from unexpected conditions
- Making debugging easier

Python uses **exceptions** to signal errors. You handle them with ```try/except```.

### Examples of Python exceptions
```python
ZeroDivisionError
ValueError
TypeError
FileNotFoundError
KeyError
```
___

## 2. Basic ```try/except``` Structure

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

```

## 3. Catching Multiple Errors
```python
try:
    value = int("abc")
except (ValueError, TypeError):
    print("Invalid input!")

```
## 4. ```else``` and ```finally```
```python
try:
    f = open("data.txt")
except FileNotFoundError:
    print("File missing.")
else:
    print("Successfully opened!")
finally:
    print("Done.")

```
## 5. Raising Your Own Exceptions
```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount

```

## 6. Creating Custom Exception Classes
```python
class InvalidAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")

```

# Unit Testing with pytest
## 1. What Is a Unit Test?

A **unit test** is a small, isolated test that checks whether a **single unit of code** (usually a function or method) works correctly on its own.

- The “unit” is the smallest testable part of a program.

- Unit tests ensure that this part behaves as expected for different inputs and situations.

- They run automatically and quickly, and help catch bugs early.

Key characteristics of a unit test

- Tests **one thing only** (one function, one behavior).

- Isolates the code being tested — no databases, networks, or other dependencies.

- Uses assertions to verify the output.

- Should be fast, repeatable, and predictable.

```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

```
This unit test checks that the ```add``` function returns the correct result.

## 1. What is pytest?
A lightweight testing framework that supports:
- Simple test functions
- Fixtures
- Assertions
- Test discovery

### 1. Installation and execution:
```bash
    #installation
    pip install pytest
    #execution
    pytest
```
### 2. Basic pytest Test
```python
# test_math.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

```
### 3. Testing Exceptions with pytest
```python
import pytest

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("No zero division")
    return a / b

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


```

