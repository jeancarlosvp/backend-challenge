import requests

baseUrl = "https://pokeapi.co/api/v2/"


# for answer1
def quantityOfPokemons():
    response = requests.get(baseUrl + "pokemon")
    return response.json()["count"]


def getAllPokemons():
    limit = quantityOfPokemons()
    response = requests.get(baseUrl+"pokemon?limit="+str(limit))
    return response.json()["results"]


# for answer2
def eggGroupsForPokemon():
    pokemonName = "raichu"
    urlForPOkemon = baseUrl + "pokemon-species/" + pokemonName
    response = requests.get(urlForPOkemon)
    names = response.json()["egg_groups"]
    namesList = list(map(lambda group: group["name"], names))
    return namesList


# for answer3
def getId(urlPokemon):
    id = int(urlPokemon.split("/")[-2])
    return id


def getWeightById(id):
    urlForIdPokemon = baseUrl + "pokemon/" + str(id)
    response = requests.get(urlForIdPokemon)
    return response.json()["weight"]
