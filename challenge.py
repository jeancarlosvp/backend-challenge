import requests

baseUrl = "https://pokeapi.co/api/v2/pokemon"


def quantityOfPokemons():
    response = requests.get(baseUrl)
    return response.json()["count"]


def getAllPokemons():
    limit = quantityOfPokemons()
    result = requests.get(baseUrl+"?limit="+str(limit))
    return result.json()["results"]


def isCorrectName(name):
    return name.count("at") and name.count("a") == 2


def getNumberofPokemons():
    pokemons = getAllPokemons()
    countPokemons = 0
    for pokemon in pokemons:
        if isCorrectName(pokemon["name"]):
            countPokemons += 1

    print(countPokemons)


getNumberofPokemons()


def eggGroupsForRaichu():
    urlForRaichu = "https://pokeapi.co/api/v2/pokemon-species/raichu/"
    response = requests.get(urlForRaichu)
    names = response.json()["egg_groups"]
    namesList = list(map(lambda group: group["name"], names))
    return namesList


def numberOfPokemonsWithRaichu():
    eggsList = eggGroupsForRaichu()
    namesPokemonsWithRaichu = []
    for egg in eggsList:
        urlEgg = "https://pokeapi.co/api/v2/egg-group/" + egg
        response = requests.get(urlEgg)
        pokemonsWithRaichu = response.json()["pokemon_species"]
        for pokemon in pokemonsWithRaichu:
            namesPokemonsWithRaichu.append(pokemon["name"])

    setPokemons = set(namesPokemonsWithRaichu)

    print(len(setPokemons))


numberOfPokemonsWithRaichu()


def getMinMaxWeightPokemons():
    weightsPokemon = []
    urlForFighting = "https://pokeapi.co/api/v2/type/fighting"
    response = requests.get(urlForFighting)
    pokemonsObject = response.json()["pokemon"]
    for pokemon in pokemonsObject:
        id = getId(pokemon["pokemon"]["url"])
        weight = getWeight(id)
        if id <= 151:
            weightsPokemon.append(weight)
    print([max(weightsPokemon), min(weightsPokemon)])


def getId(urlPokemon):
    id = int(urlPokemon.split("/")[-2])
    return id


def getWeight(id):
    urlForPokemon = "https://pokeapi.co/api/v2/pokemon/" + str(id)
    response = requests.get(urlForPokemon)
    return response.json()["weight"]


getMinMaxWeightPokemons()
