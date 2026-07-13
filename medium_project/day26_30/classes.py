import random
import json
from pathlib import Path

# variable
pilihan = {
    "tolakan": ['TIDAK', 'KELUAR', 'SUDAH'],
    "deklarasi": ['MULAI', 'SUTRA', 'MEMULAI SUTRA', 'BERHITUNG', 'MEMULAI PERHITUNGAN'],
    "overclock": ['PELEPASAN BATAS', 'OVERCLOCK', 'MELEBIHI BATAS', 'MEMAKAN EMOSI', 'PERTARUHAN'],
    "perstujuan": ['YA', 'IYA', 'OKE', 'OK', 'BAIKLAH', 'LAKUKAN']
}

# database
BASE_DIR = Path(__file__).resolve().parent
db_path = BASE_DIR / 'db.json'
us_path = BASE_DIR / 'user.json'

def load_db():
    """function for load database"""
    with open(db_path) as database:
        db = json.loads(database.read())
    with open(us_path) as user:
        us = json.loads(user.read())
    return db, us

def save(us_data):
    """function for save user data to user.json"""
    with open(us_path, 'w') as usdb:
        json.dump(us_data, usdb, indent=4)

# the code
# entity
class Entity:
    def __init__(self, spesies, name):
        db, _ = load_db()
        self.spesies = spesies
        self.name = name
        self.emotion = db['Spesies'][self.spesies]['Emosi']
        self.history = {}

    def get_data(self):
        return {
            'Tingkat': self.tingkat,
            'Emotion energy': self.emotion,
            'Prana': self.prana,
            'Can use Sutra': self.is_use_sutra,
            'Sutra history': self.history
        }

    def __str__(self):
        selfData = {
            'Name': self.name,
            'Prana': self.prana,
            'Emotion energy': self.emotion,
            'Emotion health': self.psycology,
            'Can use Sutra': self.is_use_sutra,
            'Scale': self.tingkat
        }
        return json.dumps(selfData, indent=4, separators=('; ', ' => '))

class Human(Entity):
    def __init__(self, name, exist=None):
        spesies = 'Manusia'
        super().__init__(spesies, name)
        db, _ = load_db()
        self.is_use_sutra = False
        self.is_declarated = False
        self.is_overclock = False
        self.bisa = None
        self.sutra_result = {}
        self.psycology = "Aman"
        
        if exist:
            self.tingkat = exist['Tingkat']
            self.prana = exist['Prana']
            self.is_use_sutra = exist['Can use Sutra']
            self.history = exist['Sutra history']
        
        else:
            tingkat, kemungkinan = [f'T{x}' for x in range(1, 7)], [40, 30, 15, 10, 4, 1]
            gacha = random.choices(tingkat, weights=kemungkinan)
            self.tingkat = gacha[0]
            self.prana = (db['Spesies'][self.spesies]['Tingkat'][self.tingkat]['penggunaan energi emosi'] / 100) * db['Spesies'][self.spesies]['Emosi']
            self.is_use_sutra = self.prana > 25
    
    def declaration(self, deklarasi=False):
        self.is_declarated = deklarasi
    
    def overclock(self, deklarasi=False):
        self.is_overclock = deklarasi
    
    def penyelarasan_prana(self):
        db, _ = load_db()
        if self.prana < 25:
            self.bisa = False
            return f"{self.name} sudah berada di batas penggunaan!", False
        elif (self.is_declarated or self.is_overclock) and self.is_use_sutra:
            hasil = f"{self.name} bisa menggunakan {db['Spesies'][self.spesies]['Tingkat'][self.tingkat]['penggunaan energi emosi']}% dari total {self.emotion} atau {self.prana}"
            self.bisa = True
            return hasil, self.bisa
        self.bisa = False
        return "Deklarasikan dulu!", False
    
    def sutra(self, gaya, wujud, code, position):
        alert, self.bisa = self.penyelarasan_prana()
        if self.bisa:
            cells = [0] * 30000
            ptr = 0
            code_ptr = 0
            loop_map = {}
            stack = []
            output = []
            self.hitungan = ""

            # Pre-process loops
            for i, char in enumerate(code):
                if char == '[':
                    stack.append(i)
                elif char == ']':
                    start = stack.pop()
                    loop_map[start] = i
                    loop_map[i] = start

            # Execution
            while code_ptr < len(code):
                char = code[code_ptr]
                if char == '>':
                    ptr = (ptr + 1) % 30000
                elif char == '<':
                    ptr = (ptr - 1) % 30000
                elif char == '+':
                    cells[ptr] = (cells[ptr] + 1) % 256
                elif char == '-':
                    cells[ptr] = (cells[ptr] - 1) % 256
                elif char == '.':
                    output.append(chr(cells[ptr]))
                elif char == '[':
                    if cells[ptr] == 0:
                        code_ptr = loop_map[code_ptr]
                elif char == ']':
                    if cells[ptr] != 0:
                        code_ptr = loop_map[code_ptr]
                        continue
                code_ptr += 1
                self.hitungan = ''.join(output)
            self.wujud = wujud
            self.gaya = gaya
            self.position = position
            self.sutra_result = {
                'gaya': self.gaya,
                'wujud': self.wujud,
                'hasil': self.hitungan,
                'posisi': self.position
            }
            return self.sutra_result
        else:
            return f"Error: {alert}"
    
    def prakasa(self):
        db, _ = load_db()
        if self.sutra_result:
            mana_cost = 75 if len(self.sutra_result['hasil']) > 2 else 50 if len(self.sutra_result['hasil']) == 2 else 25
            self.history = self.sutra_result
            if self.prana < mana_cost:
                return "Prana tidak cukup!"
            elif self.is_overclock:
                self.emotion = max(0, self.emotion - mana_cost)
                self.psycology = 'Monster logis' if self.emotion < 250 else 'Hilang harapan' if self.emotion < 500 else 'Mulai tidak emosional' if self.emotion <= 750 else 'Terkikis'
                self.prana = (db['Spesies'][self.spesies]['Tingkat'][self.tingkat]['penggunaan energi emosi'] / 100) * self.emotion
            
            elif self.prana >= mana_cost:
                self.prana -= mana_cost
            return f"{self.name} memanipulasi {self.sutra_result['hasil']} dengan wujud {self.sutra_result['wujud']} menggunakan gaya {self.sutra_result['gaya']} di {self.sutra_result['posisi']}"
        else:
            return 'Hitung dulu!'