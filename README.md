# Clean Code in Python
**Clean code** is a set of rules and principles that helps to keep our code readable, maintainable, and extendable.
## How to write Clean variables in Python:

 1. We should use **nouns** for variable names.
 2. We should use **meaningful** variable names.
```python
#this is bad
a = 52
#this is good
age = 52
```
 3. **Same vocabulary** for the same type of variable is needed.
```python
# This is bad
client_first_name = 'Bob'
customer_last_name = 'Smith'

# This is good
client_first_name = 'Bob'
client_last_name = 'Smith'
```

 4. Names should be **descriptive/intention-revealing.** Other developers should be able to figure out what a variable stores just by reading its name.
 5. We should always use **pronounceable** names.
 6. **Searchable** names are always preferred.
## How to write Clean Functions in Python:

 1. A function should be **small**  because it is easier to know what the function does.
 2. We should **not use different words** for the same concept.
 ```python
# This is bad
def get_name(): pass
def fetch_age(): pass

# This is good
def get_name(): pass
def get_age(): pass
```

 3. We should **avoid duplication** because it creates redundancy and if we make a change to one piece of code, we need to remember to make the same change to another piece of code. If we forget to do so, we will introduce bugs into our code.
 4. Names should be **descriptive**. It is better to write long names rather than write vague names. A long descriptive name is better than a long descriptive comment.
 5. Functions should only perform a **single task**.
 ```python
# This is bad
def fetch_and_display_personnel(): 
	pass
	
# This is good
def fetch_personnel():
	pass

def display_personnel():
	pass
```

 6. A function **should not have more than 3 arguments** since it is a sign that the function is performing multiple tasks. It is also difficult to test a function with more than 3 different combinations of variables.

	**Suggestion:** If a function has more than 3 arguments, you can consider turning it into a class.
	

 7. We should **not use flags** in functions. Flags are variables (usually booleans) passed to functions, which the function uses to determine its behavior. They are considered bad designs because functions should only perform one task. The easiest way to avoid flags is to split your function into smaller functions.
```python
# This is bad
def transform(text, uppercase):
    if uppercase:
        return text.upper()
    else:
        return text.lower()

uppercase_text = transform(text, True)
lowercase_text = transform(text, False)


# This is good
def uppercase(text):
    return text.upper()

def lowercase(text):
    return text.lower()

uppercase_text = uppercase(text)
lowercase_text = lowercase(text)
```
8. Function names should be **verbs**

9. A function produces a side effect if it does anything other than take a value in and return another value or values. For example, a side effect could be writing to a file or modifying a global variable.
 ## How to write Clean Comments in Python: 
 1. Comments should not contradict the code.
 2. Comments should be written in complete sentences.
 4. Noise comments should be avoided. comments that do not add any value to the code are noise comments. Such as: 
 ```python
 numbers = [1, 2, 3, 4, 5]

 # This is a list of numbers.
 ```
 6. We should not leave a commented-out code. All the debug code or debug messages should be removed before pushing to a version control system.

 ## Naming conventions in Python:

 1. **class** names should be **CamelCase** (MyClass).

 2. **variable** names should be **snake_case** and **all lowercase** (first_name).

 3. **function** names should be **snake_case** and **all lowercase** (quick_sort()).

4. **constants** should be **snake_case** and **all uppercase** (PI = 3.14159).

5. **modules** should have short, **snake_case** names (numpy).

## Line formatting in Python:

1. indent using **4 spaces** (spaces are preferred over tabs).

2. **lines** should not be longer than **79 characters**.

3. **avoid multiple statements** on the **same line**.

4. **top-level function** and **class definitions** are surrounded with **two blank lines**.

5. **method definitions** inside a class are surrounded by a **single blank line**.

6. **imports** should be on **separate lines**.

## Few other important points
1. Use modules rather than repeating the same code.
2. Use virtual environment where it is possible.
3. There are a lot of unique ways to implement a specific task in Python. These are concise methods that help in shortening the code and make it look elegant. Such as: List Comprehensions, Swapping Variables, Slicing. Try to use these.

##### There are four most popular principles: DRY, KISS, SoC, and SOLID to write clean code. All of these are covered in the description above. I am giving a brief introduction of these four priciples below:
1. **DRY** (Don't repeat yourself)
Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.
2. **KISS** (Keep it simple, stupid)
Most systems work best if they are kept simple, rather than made complicated.
3. **SoC** (Separation of concerns)
SoC is a design principle for separating a computer program into distinct sections such that each section addresses a separate concern. A concern is a set of information that affects the code of a computer program.
A good example of SoC is MVC (Model - View - Controller).
4. **SOLID**
It consists of the following five concepts:
The Single-responsibility principle: "A class should have one, and only one, reason to change."
The Open–closed principle: "Entities should be open for extension, but closed for modification."
The Liskov substitution principle: "Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it."
The Interface segregation principle: "A client should not be forced to implement an interface that it doesn’t use."
The Dependency inversion principle: "Depend upon abstractions, not concretions."

#### These are some rules only but clean coding can be ensured by practicing a lot.
