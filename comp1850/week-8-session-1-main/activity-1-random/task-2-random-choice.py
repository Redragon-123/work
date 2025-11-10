import random

# reading & cleaning the data
with open("names.txt") as f:
    names = f.readlines()
names = [ name.strip() for name in names ]

'''
names is a list of 1000 names - each name is 2 words long (in format: firstname surname).

You have three tasks:

Task 1:

Ask the user to enter a number, and pick that many random names out of the list.


Task 2:

Create 10 new random names by picking 10 random firstnames and combining them with 10 random surnames.

Task 3:

Shuffle the list and create 250 teams of 4 random people.
Hint: use a list-of-lists to store the teams.

'''
while True:
        input_number=int(input("Please input a positive integer(0-1000):"))
        if 0<input_number<=1000:
            break
        else:
            print("Please input a positive integer in range(0,1000)!")
random_names=random.sample(names,input_number)
for name in random_names:
    print(f"Pick {len(random_names)}: {random_names}")
first_names=[]
last_names=[]
for name in names:
    first,last=name.split(" ")
    first_names.append(first)
    last_names.append(last)
new_random_names=[]
for _ in range(10):
    first=random.choice(first_names)
    last=random.choice(last_names)
    new_random_name=first+" "+last
    new_random_names.append(new_random_name)
print("10 new random names:")
for name in new_random_names:
    print(name)
random.shuffle(names)
teams=[]
for i in range(250):
    team=names[i*4:(i+1)*4]
    teams.append(team)
print("250 teams of 4 random people:")
for i,team in enumerate(teams): 
    print(f"Team {i+1}: {team}")