from helpers import *
import requests

baseUrl = "https://pokeapi.co/api/v2/"


def getNumberofPokemons():  # first answer
    pokemons = getAllPokemons()
    countPokemons = 0
    for pokemon in pokemons:
        name = pokemon["name"]
        if (name.count("at") and name.count("a") == 2):
            countPokemons += 1

    return countPokemons


def getNumberOfPokemonsWithRaichu():  # second answer
    eggsList = eggGroupsForPokemon()
    namesPokemonsWithRaichu = []
    for egg in eggsList:
        urlEgg = baseUrl + "egg-group/" + egg
        response = requests.get(urlEgg)
        pokemonsWithRaichu = response.json()["pokemon_species"]
        for pokemon in pokemonsWithRaichu:
            namesPokemonsWithRaichu.append(pokemon["name"])

    setPokemons = set(namesPokemonsWithRaichu)

    return len(setPokemons)


def getMaxMinWeightPokemonsByType():  # third answer
    pokemonType = "fighting"
    urlForPokemon = baseUrl + "type/" + pokemonType
    pokemonWeights = []

    response = requests.get(urlForPokemon)
    pokemonsObject = response.json()["pokemon"]

    for pokemon in pokemonsObject:
        id = getId(pokemon["pokemon"]["url"])
        if id <= 151:
            weight = getWeightById(id)
            pokemonWeights.append(weight)
    return [max(pokemonWeights), min(pokemonWeights)]


def solutions():
    print("Loading the responses")
    solOne = getNumberofPokemons()
    solTwo = getNumberOfPokemonsWithRaichu()
    solThree = getMaxMinWeightPokemonsByType()

    print(f"First answer: {solOne}")
    print(f"Second answer: {solTwo}")
    print(f"Third answer: {solThree}")


solutions()
