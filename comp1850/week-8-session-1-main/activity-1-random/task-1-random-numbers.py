# We need to import the library in order to use in in Python
import random

# And you have a series of short tasks to complete - remember to run your program to check that they are working!

''' Task A

You have been given a little bit of unfinished code to complete and add to.

- Generate 3 random numbers between 0 and 100 and print them out
- Comment and uncomment 'random.seed(10)'
- Run your program with it commented and with it uncommented.
- Write a comment explaining what you think it is doing.
- confirm this by changing the value in the brackets.
'''

# random.seed() is ...
random.seed(10)

num1 = random.randint(0,100)
num2 = random.randint(0,100)
num3 = random.randint(0,100)

print(f"{num1} ~ {num2} ~ {num3}")




''' Task B
- Ask the user to enter a positive integer, and generate that many random numbers.
- Optionally: save these into a file called 'random.txt'
'''
import random
while True:
    try:
        n=int(input("Please input a positive integer:"))
        if n>0:
            break
        else:
            print("please input a positive number!")
    except ValueError:
        print("Please input an integer!")
random_numbers=[random.randint(0,100) for _ in range(n)]
print(f"Generate {len(random_numbers)} numbers:{random_numbers}")



