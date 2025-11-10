"""
Exercise 2.2: View the Current Team (Stub)
- Implement a method to view the current team.
- Display each Pokémon's name, types, and image URL.
"""

import httpx

class Team:
    def __init__(self):
        """Initialize an empty team."""
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
        # TODO: Check if the team is empty
        if not self.members:
            
                # TODO: If empty, print a message indicating the team is empty
            print("Your team is currently empty.") 
            return
        
        # TODO: Print the team members with their details
        print("Your Team:")
        for idx, pokemon in enumerate(self.members, 1):
            # TODO: Extract and format the Pokémon's details
            print(f"{idx}. Name: {pokemon['name']}")
            print(f"   Types: {', '.join(pokemon['types'])}")
            print(f"   Image URL: {pokemon['image_url']}")
    
# Example usage
# team = Team()
# team.add_pokemon("squirtle")
# team.add_pokemon("charmander")
# team.view_team()
