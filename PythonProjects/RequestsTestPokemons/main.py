import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = '66d4bef095344f5d7caae26d624cacbf'
HEADER = {'Content-Type':'application/json','trainer_token':TOKEN}

body_create = {
    "name": "Пирожок",
    "photo_id": 35
}
body_change = {
    "pokemon_id": "43461",
    "name": "Огонек",
    "photo_id": 5
}
body_pokebol = {
    "pokemon_id": "43461"
}
response_create = requests.post(url= f'{URL}pokemons', headers=HEADER, json=body_create)
print(response_create.text)

response_change = requests.put(url= f'{URL}pokemons', headers=HEADER, json=body_change)
print(response_change.text) 

response_pokebol = requests.post(url= f'{URL}trainers/add_pokeball', headers=HEADER, json=body_pokebol)
print(response_pokebol.text)