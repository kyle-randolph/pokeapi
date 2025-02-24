# Poke API SDK Overview
This lightweight pokémon API can be used to create a list of all pokemon, search for a pokemon by name, or list all information for a given generation of pokemon including which pokemon are part of a given generation.

# Installation
- Clone this repo
- Change directory into the `pokeapi` repo
- Install requirements by running `pip install -r requirements.txt`
- Install the Pokemon sdk by running `pip install -e .`
- Validate successful installation by running 
`pip list | grep pokeapi`

# Usage
- This SDK has 3 primary functions:
    - get_pokemon(identifier)
        - The identifier can either be a string or integer for a given pokemon. This API will return all information for the specified pokemon. e.g. `get_pokemon("pikachu")` or `get_pokemon(25)`
    - list_pokemon()
        - This function returns an array of all pokemon
    - get_generation(identifier)
        - The identifier can either be a string or integer for the given pokemon generation. E.g. `get_generation("generation-i")` or `get_generation(1)`

# Caveats
- Input validation could be improved for these functions


# Testing
- Run `pytest -v tests/unit_test.py`

# Please add a section in the readme describing any critical design decisions you’ve taken or links to any tools used.
- Despite pokeapi documentation, did not implement caching on this initial rev of the sdk
- In future releases, I would like to implement searching for a given pokemon to return which generation the corresponding pokemon is associated with.