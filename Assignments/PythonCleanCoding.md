# Clean Code in Python
## Table of Contents
- [How to write clean variables](#how-to-write-clean-variables-in-python)
- [How to write clean functions](#how-to-write-clean-functions-in-python)
- [How to write clean comments](#how-to-write-clean-comments-in-python)
- [How to write clean classes](#how-to-write-clean-classes-in-python)
- [How to write clean modules and packages](#how-to-write-clean-modules-and-packages-in-python)
- [How to format lines](#how-to-format-lines-in-python)
- [How to do source file encoding](#how-to-do-source-file-encoding-in-python)
- [How to write imports](#how-to-write-imports)
- [String Quotes](#string-quotes)
- [Other Recommendations](#other-recommendations)
- [Example of a python code with the best practices](#example-of-a-python-code-with-the-best-practices)


## How to write clean variables in Python:

 1. Use **nouns** for variable names.
 2. Use **meaningful** variable names.
 3. **Same vocabulary** for the same type of variable is needed.
 4. Names should be **descriptive/intention-revealing.** Other developers should be able to figure out what a variable stores just by reading its name.
 5. Always use **pronounceable** names.
 6. **Searchable** names are always preferred.
 7. **Variable** names should be **snake_case** and **all lowercase** (first_name).
 8. **Constants** should be **snake_case** and **all uppercase** (PI = 3.14159).

## How to write clean Functions in Python:

 1. Function names should be **verbs**.
 2. **Do not use different words** for the same concept.
 3. **Avoid duplication** because it creates redundancy.
 4. Names should be **descriptive**. It is better to write long names rather than write vague names. A long descriptive name is better than a long descriptive comment.
 5. Functions should only perform a **single task**.
 6. A function **should not have more than 3 arguments** since it is a sign that the function is performing multiple tasks.
    **Suggestion:** If a function has more than 3 arguments, you can consider turning it into a class.
 7. **Function** names should be **snake_case** and **all lowercase** (quick_sort()).
 8. A function should be **small**  because it is easier to know what the function does.

 ## How to write clean comments in Python: 
 1. Comments should not contradict the code.
 2. Comments should be written in complete sentences.
 3. Noise comments should be avoided. Comments that do not add any value to the code are noise comments.
 4. Do not leave a commented-out code. All the debug code or debug messages should be removed before pushing to a version control system.

 ## How to write clean classes in Python:

 1. **Class** names should be **CamelCase** (MyClass).
 2. The naming convention for methods may be used instead in cases where the interface is documented and used primarily as a callable.

## How to write clean modules and packages in Python: 
 1. **Modules** should have short, **snake_case** names (numpy).
 2. Underscores can be used in the module name if it improves readability.
 3. When an extension module written in C or C++ has an accompanying Python module that provides a higher level (e.g. more object oriented) interface, the C/C++ module has a leading underscore (e.g. _socket).

## How to format lines in Python:

 1. Indent using **4 spaces**.
 2. **Avoid multiple statements** on the **same line**.
 3. **Top-level function** and **class definitions** are surrounded with **two blank lines**.
 4. **Method definitions** inside a class are surrounded by a **single blank line**.
 5. **Imports** should be on **separate lines**.

## How to do source file encoding in Python
 1. Code in the core Python distribution should always use UTF-8, and should not have an encoding declaration.
 2. In the standard library, non-UTF-8 encodings should be used only for test purposes. Use non-ASCII characters sparingly, preferably only to denote places and human names.
 3. All identifiers in the Python standard library MUST use ASCII-only identifiers and SHOULD use English words wherever feasible (in many cases, abbreviations and technical terms are used which aren't English).
## How to write imports
 1. Imports should usually be on separate lines.
 2. Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants.
 3. imports should be grouped in the following order:
    1. Standard library imports.
    2. Related third-party imports.
    3. Local application/library specific imports.
 4. You should put a blank line between each group of imports.
## String Quotes
 1. In Python, single-quoted strings and double-quoted strings are the same. This PEP does not make a recommendation for this. Pick a rule and stick to it. When a string contains single or double quote characters, however, use the other one to avoid backslashes in the string. It improves readability.

## Other Recommendations
 1.  Avoid trailing whitespace anywhere. Because it's usually invisible, it can be confusing: e.g. a backslash followed by a space and a newline does not count as a line continuation marker. Some editors don't preserve it and many projects (like CPython itself) have pre-commit hooks that reject it.
 2.   Always surround these binary operators with a single space on either side: assignment (=), augmented assignment (+=,  -=  etc.), comparisons (==,  <,  >,  !=,  <>,  <=,  >=,  in,  not in,  is,  is not), Booleans (and,  or,  not).  
 3.  If operators with different priorities are used, consider adding whitespace around the operators with the lowest priority(ies). Use your own judgment; however, never use more than one space, and always have the same amount of whitespace on both sides of a binary operator.
 4. Don't use spaces around the = sign when used to indicate a keyword argument, or when used to indicate a default value for an _unannotated_ function parameter:
 5. While sometimes it's okay to put an if/for/while with a small body on the same line, never do this for multi-clause statements. Also avoid folding such long lines!
## Example of a python code with the best practices:
```python


class ShapeCircle:

    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self):
        PI = 3.1416
        area = PI * self.radius ** 2
        print(area)



obj = ShapeCircle(3)
obj.calculate_area()
```
