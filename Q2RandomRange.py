import random

# prompt for range limit
lower_limit = int(input("Enter the lower limit of the range: "))
upper_limit = int(input("Enter the upper limit of the range: "))

# random number generatiom
random_number = random.randint(lower_limit, upper_limit)

# Result
print(f"A random number between {lower_limit} and {upper_limit} is: {random_number}")
