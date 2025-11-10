"""
Exercise 2.3: Remove Pokémon from the Team (Stub)
- Implement a method to remove a Pokémon from the team by name.
- Make sure the team size is updated accordingly.
"""

import httpx

class Team:
    def __init__(self):
        """Initialise an empty team."""
        self.members = []
    
    def add_pokemon(self, name):
        """Add a Pokémon to the team."""
        # (Implementation from Exercise 2.1)
        url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        response=httpx.get(url)
        if response.statys_code==200:
            data=response.json()
            self.menbers.append({
                "name": data['name'].capitalize(),
                "types": [t['type']['name'].capitalize() for t in data['types']],
                "image_url": data['sprites']['front_default']
            })
            print("Name{name.capitalize()} has been added to team.")
        else:
            print("Not found.")
    
    def view_team(self):
        """View the current team with details."""
        # (Implementation from Exercise 2.2)
        if not self.members:
            print("Your team is currently empty.") 
            return
        
        print("Your Team:")
        for idx, pokemon in enumerate(self.members, 1):
            print(f"{idx}. Name: {pokemon['name']}")
            print(f"   Types: {', '.join(pokemon['types'])}")
            print(f"   Image URL: {pokemon['image_url']}")
    
    def remove_pokemon(self, name):
        """Remove a Pokémon from the team by name."""
        # TODO: Find the Pokémon in the team
        for pokemon in self.members:
            # TODO: If found, remove it and print a confirmation message
            if pokemon['name'].lower() == name.lower():
                self.members.remove(pokemon)
                print(f"{pokemon['name']} has been removed from the team.")
                return
            # TODO: If not found, print a message indicating the Pokémon is not in the team
            else:
                print(f"{name.capitalize()} is not in your team.")

# Example usage
# team = Team()
# team.add_pokemon("squirtle")
# team.add_pokemon("charmander")
# team.view_team()
# team.remove_pokemon("squirtle")
# team.view_team()
