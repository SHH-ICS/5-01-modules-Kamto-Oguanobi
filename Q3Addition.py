import random

# numbers between 1 and 100 
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

# addition question
print(f"What is {num1} + {num2}?")

# answer input
user_answer = int(input("Enter your answer: "))

# calculation
correct_answer = num1 + num2

# check for answer
if user_answer == correct_answer:
    print("Correct")
else:
    print(f"wrong the answer is {correct_answer}.")
