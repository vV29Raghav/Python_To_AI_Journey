# 1. INTRODUCTION TO PYTHON AND BASIC SYNTAX
print("=== PYTHON FUNDAMENTALS ===")

print("Hello, Python!")
print("Starting my journey from Python to AI.")


# 2. VARIABLES AND DATA TYPES
print("\n=== VARIABLES AND DATA TYPES ===")

name = "Raghav"          # String
age = 22                 # Integer
learning_hours = 2.5     # Float
is_learning = True       # Boolean

print("Name:", name)
print("Age:", age)
print("Learning hours:", learning_hours)
print("Currently learning:", is_learning)

print("Type of name:", type(name).__name__)
print("Type of age:", type(age).__name__)
print("Type of learning_hours:", type(learning_hours).__name__)
print("Type of is_learning:", type(is_learning).__name__)


# 3. OPERATORS
print("\n=== OPERATORS ===")

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor division:", a // b)
print("Remainder:", a % b)
print("Exponentiation:", a ** b)

print("Is a greater than b?", a > b)
print("Are a and b equal?", a == b)
print("Logical AND:", a > 5 and b < 5)


# 4. CONDITIONAL STATEMENTS
print("\n=== CONDITIONAL STATEMENTS ===")

if age >= 18:
    print(name, "is an adult.")
else:
    print(name, "is not an adult.")

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "Needs improvement"

print("Score:", score)
print("Grade:", grade)


# 5. LOOPS
print("\n=== LOOPS ===")

print("For loop:")
for number in range(1, 6):
    print(number, end=" ")

print("\n\nWhile loop:")

count = 1
while count <= 3:
    print("Practice attempt:", count)
    count += 1


# 6. FUNCTIONS
print("\n=== FUNCTIONS ===")

def greet_user(user_name):
    """Return a personalized greeting."""
    return f"Welcome, {user_name}! Keep learning Python."

def calculate_sum(first, second):
    """Return the sum of two numbers."""
    return first + second

message = greet_user(name)
result = calculate_sum(10, 20)

print(message)
print("Sum of 10 and 20:", result)


# 7. SIMPLE PRACTICAL EXAMPLE
print("\n=== PRACTICAL EXAMPLE ===")

numbers = [10, 15, 20, 25, 30]

total = sum(numbers)
average = total / len(numbers)

print("Numbers:", numbers)
print("Total:", total)
print("Average:", average)

print("\nPython fundamentals completed successfully!")
