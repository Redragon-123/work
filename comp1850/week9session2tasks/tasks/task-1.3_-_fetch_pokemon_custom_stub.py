"""
Exercise 1.3: Custom Output (Raw vs Summary) (Stub)
- Fetch Pokémon data from the PokéAPI.
- Display either the full raw JSON or a summarised version based on a parameter.
"""

import httpx
import json

def fetch_pokemon_custom(name, display_raw=False):
    """Fetch Pokémon details and display either raw JSON or a summary."""
    # TODO: Construct the URL using the Pokémon name
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    # TODO: Make a GET request to the URL
    response=httpx.get(url)
    # TODO: Check if the response is successful (status_code == 200)
    if response.status_code == 200:
        # TODO: Parse the JSON response
        response_data = response.json()
    
        if display_raw:
            # TODO: Pretty-print the raw JSON
            print(json.dumps(response_data, indent=4))
        else:
            # TODO: Extract the Pokémon's name, types, base stats, and image URL
            pokemon_name = response_data['name']
            types = [t['type']['name'] for t in response_data['types']]
            stats = {stat['stat']['name']: stat['base_stat'] for stat in response_data['stats']}
            image_url = response_data['sprites']['front_default']
            # TODO: Print the details in a readable format
        print(f"Name: {name}")
        print(f"Types: {', '.join(types)}")
        print("Base Stats:")
        for stat, value in stats.items():
            print(f"  {stat.capitalize()}: {value}")
        print(f"Image URL: {image_url}")
    # TODO: Print an error message if the Pokémon is not found
    else:
        print(f"Error: Pokémon '{name}' not found!") 

# Example usage
# fetch_pokemon_custom("squirtle")  # Display summary by default
# fetch_pokemon_custom("squirtle", display_raw=True)  # Display raw JSON
fetch_pokemon_custom("squirtle")
fetch_pokemon_custom("squirtle", display_raw=True)
"""
Hints:
- Use json.dumps(data, indent=4) for raw JSON output.
- Extract specific keys like 'types', 'stats', and 'sprites' for summaries.
- Use if display_raw to toggle between outputs.
"""
