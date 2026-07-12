import random
import json
from pathlib import Path

# variables
tingkat, kemungkinan = [f'T{x}' for x in range(1, 6)], [30, 20, 15, 10, 5]
gacha = random.choices(tingkat, weights=kemungkinan)

# database
BASE_DIR = Path(__file__).resolve().parent
db_path = BASE_DIR / 'db.json'
us_path = BASE_DIR / 'sutra_kara.json'

with open(db_path) as database:
    db = json.loads(database.read())
#with open(us_path) as user:
#    us = json.loads(user.read())

# the code
# entity
class Entity:
    def __init__(self, spesies, name):
        self.spesies = spesies
        self.name = name
        self.hp = db['Spesies'][self.spesies]['hp']
        self.emotion = db['Spesies'][self.spesies]['Emosi']
    def __str__(self):
        selfData = {
            'Name': self.name,
            'HP': self.hp,
            'Prana': self.prana,
            'Emotion energy': self.emotion,
            'Sutra usage': self.stotal,
            'Scale': self.tingkat
        }
        return json.dumps(selfData, indent=4, separators=('; ', ' => '))

class Human(Entity):
    def __init__(self, name):
        spesies = 'Manusia'
        super().__init__(spesies, name)
        self.tingkat = gacha[0]
        self.prana = (db['Spesies'][self.spesies]['Tingkat'][self.tingkat]['penggunaan energi emosi'] / 100) * db['Spesies'][self.spesies]['Emosi']
        self.stotal = self.prana > 25

h1 = Human('MMZ')

print(h1)