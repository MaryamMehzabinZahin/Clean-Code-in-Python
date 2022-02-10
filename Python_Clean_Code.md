# Clean Code in Python
**Clean code** is a set of rules and principles that helps to keep our code readable, maintainable, and extendable.
## How to write Clean variables in Python:

 1. we should use **nouns** for variable names
 2. We should use **meaningful** and **pronounceable** variable names
```text
#this is bad
a = 52
#this is good
age = 52
```
 3.  **same vocabulary** for the same type of variable is needed
```
# This is bad
client_first_name = 'Bob'
customer_last_name = 'Smith'

# This is good
client_first_name = 'Bob'
client_last_name = 'Smith'
```

 4. Names should be **descriptive/intention-revealing.** Other developers should be able to figure out what a variable stores just by reading its name.
 5.  We should always use **pronounceable** names.
 6. **Searchable** names are always preferred.
## How to write Clean Functions in Python:
 1. A function should be **small**  because it is easier to know what the function does.
 2. we should **not use different words** for the same concept
 ```
# This is bad
def get_name(): pass
def fetch_age(): pass

# This is good
def get_name(): pass
def get_age(): pass
```

 3. We should **avoid duplication** because it creates redundancy and if we make a change to one piece of code, we need to remember to make the same change to another piece of code. If we forget to do so, we will introduce bugs into our code.
 4. Names should be **descriptive**. It is better to write long names rather than write vague names. A long descriptive name is better than a long descriptive comment.
 5. Functions should only perform a **single task**
 ```
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
```
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
 ```
 numbers = [1, 2, 3, 4, 5]

 # This is a list of numbers.
 ```
 6. We should not leave a commented-out code. All the debug code or debug messages should be removed before pushing to a version control system.