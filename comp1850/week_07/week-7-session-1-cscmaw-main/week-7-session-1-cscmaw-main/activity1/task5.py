# Create a Character class with the following fields:
# (1) name - the name of the character
# (2) health - the health of the character, with value between 0 to 100
# (3) attack_power - the attack power of the character, with value between 10 to 100

# When an instance of Character is created, the value to all three fields are required.





# Once completed, create two instances of Character to two of your most favourite game characters.
# Then, write code to print the details of each character.



# How would you change the __init__ function so that by default the health is 100
# and attack_power is 10.
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
NEMISIS= Character("NEMISIS",100,100)
print(f"Name: {NEMISIS.name}")
print(f"Health: {NEMISIS.health}")   
print(f"Attack Power: {NEMISIS.attack_power}")
WESKER= Character("WESKER",90,95)
print(f"Name: {WESKER.name}")
print(f"Health: {WESKER.health}")   
print(f"Attack Power: {WESKER.attack_power}")

#def __init__(self, name, health=100, attack_power=10):
