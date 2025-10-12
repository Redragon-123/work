
animals = [ 'dog','cat','hamster','goldfish' ]

not_fish = [ item for item in animals if item != 'goldfish']

print(not_fish)

# write the equivalent for loop to create the not_fish list from animals
# print your result to verify it is the same
not_fish_loop = []
for item in animals:
    if item != 'goldfish':
        not_fish_loop.append(item)
print(not_fish_loop)