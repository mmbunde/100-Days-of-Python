# Day 10 Functions With Outputs

## 1. What Are Functions With Outputs?
Functions with outputs are functions that use the `return` statement to send a result back to the place where the function was called. Unlike functions that only perform an action, like printing something to the screen, functions with output allow you to store or manipulate the result further

### Anatomy of a Function with outputs

1. **`def` Keyword**: MUST be used and defines the function
2. **Parameters**: Accept input data, these are optional
3. **Logic**: Processes the input data
4. **`return` Statment**: Sends the output back to the caller

#### Example
```python
def multiply(a, b):
    return a * b

result = multiply(5, 10)
print(result)  # Output: 50
```
The `return` statment ends the function's execution and sends back the output. This returned value can be assigned to a variable, passed to another function, or used diretly

## 2. Early Return
Functions can return values early if a condition is met. This is can be useful in:
- Simplifying logic
- Avoiding unecessary computations
- Handling special cases
- Error Handling
#### Example
```python
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    return "Zero"

print(check_number(5))   # Output: Positive
print(check_number(-3))  # Output: Negative
print(check_number(0))   # Output: Zero
```

## 3. Functions With Multiple Returns
Functions can have multiple `return` statements depending on conditions

#### Example
```python
def classify_age(age):
    if age < 18:
        return "Minor"
    elif 18 <= age < 65:
        return "Adult"
    return "Senior"

print(classify_age(15))  # Output: Minor
print(classify_age(30))  # Output: Adult
print(classify_age(70))  # Output: Senior
```

## 4. Docstrings
Docstrings provide documentation for your functions, explaining their purpose, parameters, and return values. They are written using triple quotes(""" or ''')

#### Example
```python
def greet(name):
    """
    Greets a person by their name.
    
    Parameters:
    name (str): The name of the person to greet.
    
    Returns:
    str: A personalized greeting message.
    """
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
```
### Why Use Docstrings?
1. Makes your code self-explanatory
2. Helps others or yourself in the future to understand your functions
3. Used by tools like help() for quick reference