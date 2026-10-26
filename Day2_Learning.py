
print("=== STRINGS ===")

text = "  Python Learning  "

print("Original:", repr(text))
print("Strip:", text.strip())
print("Uppercase:", text.upper())
print("Replace:", text.strip().replace("Learning", "Programming"))
print("Slice [0:6]:", text.strip()[0:6])
print("Contains Python:", "Python" in text)
print("Length:", len(text.strip()))

# Strings are immutable
language = "Python"
print("First character:", language[0])
print("Reversed:", language[::-1])


# 2. LISTS
print("\n=== LISTS ===")

fruits = ["Apple", "Banana", "Cherry"]
fruits.append("Mango")
print("After append:", fruits)
print("First fruit:", fruits[0])
print("Slice [1:3]:", fruits[1:3])

fruits.remove("Banana")
print("After remove:", fruits)

squares = [number ** 2 for number in range(1, 6)]
print("Squares:", squares)


# 3. TUPLES
print("\n=== TUPLES ===")

coordinates = (10, 20, 30)

print("Coordinates:", coordinates)
print("First coordinate:", coordinates[0])
print("Length:", len(coordinates))

x, y, z = coordinates
print(f"Unpacking: x={x}, y={y}, z={z}")

values = (10, 20, 10, 30)
print("Count of 10:", values.count(10))
print("Index of 30:", values.index(30))


# 4. SETS
print("\n=== SETS ===")

numbers = {1, 2, 3, 4, 5}
numbers.add(6)
numbers.discard(3)
print("After add and discard:", sorted(numbers))

other = {4, 5, 6, 7}

print("Union:", sorted(numbers | other))
print("Intersection:", sorted(numbers & other))
print("Difference:", sorted(numbers - other))
print("Symmetric difference:", sorted(numbers ^ other))

duplicate_values = [1, 2, 2, 3, 3, 4]
print("Unique values:", sorted(set(duplicate_values)))


# 5. DICTIONARIES
print("\n=== DICTIONARIES ===")

student = {
    "name": "Raghav",
    "age": 22,
    "course": "Computer Science"
}

student["city"] = "India"
student["age"] = 23

print("Student:", student)
print("Name:", student.get("name"))
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))

removed_city = student.pop("city")
print("Removed city:", removed_city)
print("Final student details:", student)
