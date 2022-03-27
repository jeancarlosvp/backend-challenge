import requests

BASE_URI = "https://pokeapi.co/api/v2/pokemon"


def quantityOfPokemons():
    response = requests.get(BASE_URI)
    return response.json()["count"]


def getAllPokemons():
    limit = quantityOfPokemons()
    result = requests.get(BASE_URI+"?limit="+str(limit))
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
