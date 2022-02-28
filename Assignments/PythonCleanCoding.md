# Clean Code in Python

## How to write Clean variables in Python:

 1. Use **nouns** for variable names.
 2. Use **meaningful** variable names.
 3. **Same vocabulary** for the same type of variable is needed.
 4. Names should be **descriptive/intention-revealing.** Other developers should be able to figure out what a variable stores just by reading its name.
 5. Always use **pronounceable** names.
 6. **Searchable** names are always preferred.
 7. **Variable** names should be **snake_case** and **all lowercase** (first_name).
 8. **Constants** should be **snake_case** and **all uppercase** (PI = 3.14159).

## How to write Clean Functions in Python:

 1. A function should be **small**  because it is easier to know what the function does.
 2. **Do not use different words** for the same concept.
 3. **Avoid duplication** becaUse it creates redundancy and if we make a change to one piece of code, we need to remember to make the same change to another piece of code. If we forget to do so, we will introduce bugs into our code.
 4. Names should be **descriptive**. It is better to write long names rather than write vague names. A long descriptive name is better than a long descriptive comment.
 5. Functions should only perform a **single task**.
 6. A function **should not have more than 3 arguments** since it is a sign that the function is performing multiple tasks. It is also difficult to test a function with more than 3 different combinations of variables.

	**Suggestion:** If a function has more than 3 arguments, you can consider turning it into a class.
 7. **function** names should be **snake_case** and **all lowercase** (quick_sort()).
 8. Function names should be **verbs**.

 ## How to write Clean Comments in Python: 
 1. Comments should not contradict the code.
 2. Comments should be written in complete sentences.
 3. Noise comments should be avoided. Comments that do not add any value to the code are noise comments.
 4. Do not leave a commented-out code. All the debug code or debug messages should be removed before pushing to a version control system.

 ## Naming conventions for classes and modules in Python:

1. **Class** names should be **CamelCase** (MyClass).
2. **Modules** should have short, **snake_case** names (numpy).

## Line formatting in Python:

1. Indent using **4 spaces**.
2. **Avoid multiple statements** on the **same line**.
3. **Top-level function** and **class definitions** are surrounded with **two blank lines**.
4. **Method definitions** inside a class are surrounded by a **single blank line**.
5. **Imports** should be on **separate lines**.

## Example of a python code with the proper Line formatting and naming convention:
```python


class MyCircle:

    def calculate_area(self, radius):
        PI = 3.1416
        self.radius = radius
        area = PI * radius ** 2



def main():
    obj = MyCircle(3)

```