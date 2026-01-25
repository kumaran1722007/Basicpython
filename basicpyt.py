<<<<<<< HEAD
"""
Python Functions Tutorial: From Basic to Advanced
==================================================
This file demonstrates Python functions from beginner to advanced level.
"""

# ============================================================================
# LEVEL 1: BASIC FUNCTIONS
# ============================================================================

def greet():
    """Simple function with no parameters."""
    print("Hello, World!")

def greet_person(name):
    """Function with one parameter."""
    print(f"Hello, {name}!")

def add_numbers(a, b):
    """Function with multiple parameters."""
    return a + b

# Example usage:
# greet()
# greet_person("Alice")
# result = add_numbers(5, 3)
# print(result)  # Output: 8


# ============================================================================
# LEVEL 2: DEFAULT PARAMETERS
# ============================================================================

def greet_with_default(name="Guest"):
    """Function with default parameter value."""
    print(f"Hello, {name}!")

def calculate_power(base, exponent=2):
    """Function with default exponent (squared by default)."""
    return base ** exponent

# Example usage:
# greet_with_default()  # Output: Hello, Guest!
# greet_with_default("Bob")  # Output: Hello, Bob!
# calculate_power(5)  # Output: 25 (5^2)
# calculate_power(5, 3)  # Output: 125 (5^3)


# ============================================================================
# LEVEL 3: KEYWORD ARGUMENTS
# ============================================================================

def create_profile(name, age, city, country="USA"):
    """Function demonstrating keyword arguments."""
    print(f"Name: {name}, Age: {age}, City: {city}, Country: {country}")

# Example usage:
# create_profile("Alice", 25, "New York")  # Positional arguments
# create_profile(name="Bob", age=30, city="London", country="UK")  # Keyword arguments
# create_profile("Charlie", city="Paris", age=28)  # Mixed positional and keyword


# ============================================================================
# LEVEL 4: *args (Variable Positional Arguments)
# ============================================================================

def sum_all(*args):
    """Function that accepts any number of positional arguments."""
    total = 0
    for num in args:
        total += num
    return total

def print_info(*args):
    """Print all arguments passed."""
    for arg in args:
        print(arg)

# Example usage:
# print(sum_all(1, 2, 3))  # Output: 6
# print(sum_all(1, 2, 3, 4, 5))  # Output: 15
# print_info("Alice", 25, "Engineer", "New York")


# ============================================================================
# LEVEL 5: **kwargs (Variable Keyword Arguments)
# ============================================================================

def create_user(**kwargs):
    """Function that accepts any number of keyword arguments."""
    user = {}
    for key, value in kwargs.items():
        user[key] = value
    return user

def print_user_details(**kwargs):
    """Print all keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage:
# user1 = create_user(name="Alice", age=25, role="Developer")
# print(user1)  # Output: {'name': 'Alice', 'age': 25, 'role': 'Developer'}
# print_user_details(name="Bob", city="London", salary=50000)


# ============================================================================
# LEVEL 6: COMBINING *args AND **kwargs
# ============================================================================

def flexible_function(*args, **kwargs):
    """Function that accepts both positional and keyword arguments."""
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# Example usage:
# flexible_function(1, 2, 3, name="Alice", age=25)
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 25}


# ============================================================================
# LEVEL 7: RETURN VALUES AND MULTIPLE RETURNS
# ============================================================================

def divide_and_modulo(a, b):
    """Function returning multiple values (as a tuple)."""
    quotient = a // b
    remainder = a % b
    return quotient, remainder

def get_statistics(numbers):
    """Function returning multiple statistics."""
    if not numbers:
        return None, None, None
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

# Example usage:
# q, r = divide_and_modulo(17, 5)
# print(f"Quotient: {q}, Remainder: {r}")  # Output: Quotient: 3, Remainder: 2
# min_val, max_val, avg = get_statistics([1, 5, 3, 9, 2])
# print(f"Min: {min_val}, Max: {max_val}, Avg: {avg}")


# ============================================================================
# LEVEL 8: VARIABLE SCOPE (Local vs Global)
# ============================================================================

global_var = "I'm global"

def demonstrate_scope():
    """Demonstrating local and global variable scope."""
    local_var = "I'm local"
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")

def modify_global():
    """Function that modifies a global variable."""
    global global_var
    global_var = "Modified global variable"
    print(f"Modified: {global_var}")

# Example usage:
# print(global_var)  # Output: I'm global
# demonstrate_scope()
# modify_global()
# print(global_var)  # Output: Modified global variable


# ============================================================================
# LEVEL 9: LAMBDA FUNCTIONS (Anonymous Functions)
# ============================================================================

# Lambda function syntax: lambda arguments: expression
square = lambda x: x ** 2
add = lambda x, y: x + y
is_even = lambda x: x % 2 == 0

# Lambda with map, filter, reduce
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Example usage:
# print(square(5))  # Output: 25
# print(add(3, 4))  # Output: 7
# print(is_even(4))  # Output: True
# print(squared)  # Output: [1, 4, 9, 16, 25]
# print(evens)  # Output: [2, 4]


# ============================================================================
# LEVEL 10: HIGHER-ORDER FUNCTIONS
# ============================================================================

def apply_operation(func, x, y):
    """Function that takes another function as parameter."""
    return func(x, y)

def multiply(x, y):
    return x * y

def create_multiplier(factor):
    """Function that returns another function."""
    def multiplier(number):
        return number * factor
    return multiplier

# Example usage:
# result = apply_operation(multiply, 5, 3)
# print(result)  # Output: 15
# double = create_multiplier(2)
# triple = create_multiplier(3)
# print(double(5))  # Output: 10
# print(triple(5))  # Output: 15


# ============================================================================
# LEVEL 11: CLOSURES
# ============================================================================

def outer_function(x):
    """Outer function that creates a closure."""
    def inner_function(y):
        """Inner function that captures 'x' from outer scope."""
        return x + y
    return inner_function

def counter():
    """Function that creates a counter using closure."""
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

# Example usage:
# add_five = outer_function(5)
# print(add_five(3))  # Output: 8
# counter1 = counter()
# print(counter1())  # Output: 1
# print(counter1())  # Output: 2
# print(counter1())  # Output: 3


# ============================================================================
# LEVEL 12: DECORATORS
# ============================================================================

def my_decorator(func):
    """Basic decorator that adds functionality before and after function call."""
    def wrapper(*args, **kwargs):
        print("Before function execution")
        result = func(*args, **kwargs)
        print("After function execution")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    """Function decorated with my_decorator."""
    print(f"Hello, {name}!")

def timing_decorator(func):
    """Decorator that measures function execution time."""
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    """Example function that takes time to execute."""
    import time
    time.sleep(1)
    return "Done"

# Example usage:
# say_hello("Alice")
# Output:
# Before function execution
# Hello, Alice!
# After function execution


# ============================================================================
# LEVEL 13: GENERATOR FUNCTIONS
# ============================================================================

def countdown(n):
    """Generator function that yields values instead of returning."""
    while n > 0:
        yield n
        n -= 1

def fibonacci_generator(limit):
    """Generator that produces Fibonacci numbers."""
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

def number_generator(start, end, step=1):
    """Generator with parameters."""
    current = start
    while current < end:
        yield current
        current += step

# Example usage:
# for num in countdown(5):
#     print(num)  # Output: 5, 4, 3, 2, 1
# fib = fibonacci_generator(100)
# print(list(fib))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


# ============================================================================
# LEVEL 14: RECURSION
# ============================================================================

def factorial(n):
    """Calculate factorial using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci_recursive(n):
    """Calculate nth Fibonacci number using recursion."""
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def binary_search(arr, target, left=0, right=None):
    """Binary search using recursion."""
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)

# Example usage:
# print(factorial(5))  # Output: 120
# print(fibonacci_recursive(7))  # Output: 13
# arr = [1, 3, 5, 7, 9, 11, 13]
# print(binary_search(arr, 7))  # Output: 3


# ============================================================================
# LEVEL 15: TYPE HINTS (Python 3.5+)
# ============================================================================

def add_typed(a: int, b: int) -> int:
    """Function with type hints."""
    return a + b

def process_data(data: list[str], count: int = 10) -> dict[str, int]:
    """Function with complex type hints."""
    return {item: len(item) for item in data[:count]}

from typing import Optional, List, Dict, Callable

def find_item(items: List[str], target: str) -> Optional[int]:
    """Function with typing module hints."""
    try:
        return items.index(target)
    except ValueError:
        return None

def apply_func(func: Callable[[int, int], int], x: int, y: int) -> int:
    """Function that accepts a callable with type hints."""
    return func(x, y)

# Example usage:
# result = add_typed(5, 3)
# print(result)  # Output: 8


# ============================================================================
# LEVEL 16: DOCSTRINGS AND ANNOTATIONS
# ============================================================================

def documented_function(param1: str, param2: int = 10) -> str:
    """
    This is a well-documented function.
    
    Args:
        param1 (str): Description of the first parameter
        param2 (int, optional): Description of the second parameter. Defaults to 10.
    
    Returns:
        str: Description of what the function returns
    
    Raises:
        ValueError: Description of when this exception is raised
    
    Example:
        >>> documented_function("hello", 5)
        'hello repeated 5 times'
    """
    return param1 * param2


# ============================================================================
# LEVEL 17: PARTIAL FUNCTIONS
# ============================================================================

from functools import partial

def power(base, exponent):
    """Calculate base raised to exponent."""
    return base ** exponent

# Create partial functions
square = partial(power, exponent=2)
cube = partial(power, exponent=3)

# Example usage:
# print(square(5))  # Output: 25
# print(cube(3))  # Output: 27


# ============================================================================
# LEVEL 18: FUNCTION AS FIRST-CLASS OBJECTS
# ============================================================================

def greet_english(name):
    return f"Hello, {name}!"

def greet_spanish(name):
    return f"¡Hola, {name}!"

def greet_french(name):
    return f"Bonjour, {name}!"

# Functions stored in dictionary
greetings = {
    'english': greet_english,
    'spanish': greet_spanish,
    'french': greet_french
}

# Functions stored in list
operations = [lambda x: x * 2, lambda x: x ** 2, lambda x: x + 10]

# Example usage:
# print(greetings['english']("Alice"))  # Output: Hello, Alice!
# print(greetings['spanish']("Bob"))  # Output: ¡Hola, Bob!
# for op in operations:
#     print(op(5))  # Output: 10, 25, 15


# ============================================================================
# LEVEL 19: MEMOIZATION (Caching Function Results)
# ============================================================================

from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci_cached(n):
    """Fibonacci with memoization for better performance."""
    if n <= 1:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)

def memoize(func):
    """Custom memoization decorator."""
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def expensive_operation(n):
    """Example expensive operation with memoization."""
    # Simulate expensive computation
    return sum(i ** 2 for i in range(n))

# Example usage:
# print(fibonacci_cached(50))  # Much faster than recursive version


# ============================================================================
# LEVEL 20: ADVANCED DECORATORS WITH ARGUMENTS
# ============================================================================

def repeat(times):
    """Decorator factory that creates a decorator."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hi(name):
    """Function that will be called multiple times."""
    print(f"Hi, {name}!")

def validate_type(expected_type):
    """Decorator that validates function argument types."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Expected {expected_type}, got {type(arg)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_type(int)
def add_integers(a, b):
    """Function that only accepts integers."""
    return a + b

# Example usage:
# say_hi("Alice")  # Output: Hi, Alice! (printed 3 times)


# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

def exercise_1():
    """
    Exercise 1: Create a function that takes a list of numbers
    and returns the sum of all even numbers.
    """
    pass  # Your code here

def exercise_2():
    """
    Exercise 2: Create a decorator that logs function calls
    with their arguments and return values.
    """
    pass  # Your code here

def exercise_3():
    """
    Exercise 3: Create a generator function that yields
    prime numbers up to a given limit.
    """
    pass  # Your code here


# ============================================================================
# MAIN EXECUTION (Uncomment to test)
# ============================================================================

if __name__ == "__main__":
    print("=== Python Functions Tutorial ===\n")
    
    # Level 1: Basic Functions
    print("Level 1: Basic Functions")
    greet()
    greet_person("Alice")
    print(f"5 + 3 = {add_numbers(5, 3)}\n")
    
    # Level 2: Default Parameters
    print("Level 2: Default Parameters")
    greet_with_default()
    greet_with_default("Bob")
    print(f"5^2 = {calculate_power(5)}")
    print(f"5^3 = {calculate_power(5, 3)}\n")
    
    # Level 3: Keyword Arguments
    print("Level 3: Keyword Arguments")
    create_profile("Alice", 25, "New York")
    create_profile(name="Bob", age=30, city="London", country="UK")
    print()
    
    # Level 4: *args
    print("Level 4: *args")
    print(f"Sum of 1,2,3 = {sum_all(1, 2, 3)}")
    print(f"Sum of 1,2,3,4,5 = {sum_all(1, 2, 3, 4, 5)}\n")
    
    # Level 5: **kwargs
    print("Level 5: **kwargs")
    user = create_user(name="Alice", age=25, role="Developer")
    print(f"User: {user}\n")
    
    # Level 7: Multiple Returns
    print("Level 7: Multiple Returns")
    q, r = divide_and_modulo(17, 5)
    print(f"17 ÷ 5: Quotient={q}, Remainder={r}\n")
    
    # Level 9: Lambda Functions
    print("Level 9: Lambda Functions")
    print(f"Square of 5: {square(5)}")
    print(f"Add 3+4: {add(3, 4)}")
    print(f"Is 4 even? {is_even(4)}\n")
    
    # Level 10: Higher-Order Functions
    print("Level 10: Higher-Order Functions")
    result = apply_operation(multiply, 5, 3)
    print(f"5 * 3 = {result}")
    double = create_multiplier(2)
    print(f"Double of 5: {double(5)}\n")
    
    # Level 11: Closures
    print("Level 11: Closures")
    add_five = outer_function(5)
    print(f"5 + 3 = {add_five(3)}")
    counter1 = counter()
    print(f"Counter: {counter1()}, {counter1()}, {counter1()}\n")
    
    # Level 12: Decorators
    print("Level 12: Decorators")
    say_hello("Alice")
    print()
    
    # Level 13: Generators
    print("Level 13: Generators")
    print("Countdown from 5:")
    for num in countdown(5):
        print(num, end=" ")
    print("\n")
    
    # Level 14: Recursion
    print("Level 14: Recursion")
    print(f"Factorial of 5: {factorial(5)}")
    print(f"7th Fibonacci: {fibonacci_recursive(7)}\n")
    
    # Level 15: Type Hints
    print("Level 15: Type Hints")
    print(f"Add typed: {add_typed(5, 3)}\n")
    
    # Level 17: Partial Functions
    print("Level 17: Partial Functions")
    print(f"Square of 5: {square(5)}")
    print(f"Cube of 3: {cube(3)}\n")
    
    # Level 18: Functions as First-Class Objects
    print("Level 18: Functions as First-Class Objects")
    print(greetings['english']("Alice"))
    print(greetings['spanish']("Bob"))
    print()
    
    print("=== Tutorial Complete ===")
=======
print("hello")
>>>>>>> origin/main
