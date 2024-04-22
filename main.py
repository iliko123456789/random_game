import time
import random

start_time = time.time()
secret_number = random.randint(0,100)
user_num = int(input("Guess a number between 0 and 100:"))

attempts = 1

while user_num != secret_number:
    if user_num > secret_number:
        print("Too high! Try a smaller number.")
    elif user_num < secret_number:
        print("Too low! Try a larger number.")
    user_num = int(input("Enter number"))
    attempts += 1
end_time = time.time()
result_time = int(end_time - start_time)
print(f"You gussed the number in {attempts} attempts! it took you {result_time} second")