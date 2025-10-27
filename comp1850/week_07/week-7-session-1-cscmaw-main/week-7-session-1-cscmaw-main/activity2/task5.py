# Define a Recipe class to represent a recepi with ingredients, instructions, and servings.
# The Recipe class should have the following fields:
# (1) name: The name of the recipe (e.g., "Chocolate Cake").
# (2) ingredients: A dictionary where keys are ingredient names and values are quantities (float or int), e.g., {"flour": 200, "sugar": 100}.
# (3) instructions: The preparation instructions for the recipe. (e.g., "1. Mix ingredients. 2. Bake at 350°F for 30 minutes.")
# (4) servings: The number (integer) of servings the recipe is intended to make.

# The Recipe class should have the following methods:
# (1): display_recipe(): Prints the name, ingredients, instructions, and servings of the recipe.
#      Format the output so that it is easy to read and understand. For example,
#      Recepi: Chocolate Cake
#      Servings: 4
#      Ingredients:
#        - flour: 200
#        - sugar: 100
#     Instructions:
#        1. Preheat oven to 350°F.
#        2. Mix flour and sugar.
#
# (2) add_ingredient(name, quantity): Adds a new ingredient to the recipe with the specified quantity.
#     If the ingredient already exists, update its quantity by adding the specified amount to the existing quantity.
#     Example: If "flour" already has 200 grams, calling add_ingredient("flour", 50) will update "flour" to 250.
class Recipe:
    def __init__(self, name, ingredients, instructions, servings):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.servings = servings

    def display_recipe(self):
        print(f"Recipe: {self.name}")
        print(f"Servings: {self.servings}")
        print("Ingredients:")
        for ingredient, quantity in self.ingredients.items():
            print(f"  - {ingredient}: {quantity}")
        print("Instructions:")
        print(self.instructions)

    def add_ingredient(self, name, quantity):
        if name in self.ingredients:
            self.ingredients[name] += quantity
        else:
            self.ingredients[name] = quantity
recipe1=Recipe(
    name="Chocolate Cake",
    ingredients={"flour": 200, "sugar": 100, "cocoa powder": 50},
    instructions="1. Preheat oven to 350°F.\n2. Mix flour, sugar, and cocoa powder.\n",
    servings=4
)
recipe1.display_recipe()
recipe1.add_ingredient("flour", 50)  
recipe1.add_ingredient("eggs", 2) 
recipe1.display_recipe()










# Once completed, create an instance of Recepi with your favourite dish and 
# call each method least once.
