import json
import files

user1 = {
    "username": "alfredoa",
    "name": "Alfredo",
    "last_name": "Altamirano",
    "password": "aSDFGHJKASasd"
    }



user2 = {
    "username": "ecandaudap",
    "name": "Eduardo",
    "last_name": "Candaudap",
    "password": "ayhbhujmk"
    }

# files.update('sample.json', user2)

print(files.read('sample.json'))