import math
import random
from functools import wraps
from time import perf_counter

def calculate_area(radius):
    """Calculate the area of a circle."""
    return math.pi * radius**2


def greet(name, message="Keep learning!"):
    """Return a personalized greeting."""
    return f"Hello, {name}! {message}"


print(f"Circle area (radius 5): {calculate_area(5):.2f}")
print(greet("Raghav"))
print(greet("Raghav", "Keep building!"))
print("Square root of 81:", math.sqrt(81))
print("Random number (1-10):", random.randint(1, 10))


# ITERATORS

skills = ["Java", "Python", "AI"]
skill_iterator = iter(skills)

print("First skill:", next(skill_iterator))
print("Second skill:", next(skill_iterator))
print("Third skill:", next(skill_iterator))


#GENERATORS

def even_numbers(limit):
    """Yield even numbers up to the given limit."""
    for number in range(2, limit + 1, 2):
        yield number


print("Even numbers:", list(even_numbers(10)))


#DECORATORS
print("\n=== 5. DECORATORS ===")


def timed(func):
    """Print the execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - start
        print(f"{func.__name__} took {elapsed:.6f} seconds")
        return result

    return wrapper


@timed
def calculate_sum(limit):
    """Calculate the sum of numbers from 1 to limit."""
    return sum(range(1, limit + 1))
result = calculate_sum(100_000)
print("Sum:", result)
