import math

# Prompt for lengths of triangles
a = float(input("Enter the length of the first leg of the triangle (a): "))
b = float(input("Enter the length of the second leg of the triangle (b): "))

# Hypotnuse calulation with pythagorean theorem
c = math.sqrt(a**2 + b**2)

# Result
print(f"The length of the hypotenuse (c) is: {c:.2f}")
