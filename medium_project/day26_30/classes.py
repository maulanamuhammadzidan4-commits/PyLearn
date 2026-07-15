import random
import json
from pathlib import Path

# variable
pilihan = {
    "tolakan": ['TIDAK', 'KELUAR', 'SUDAH'],
    "deklarasi": ['MULAI', 'SUTRA', 'MEMULAI SUTRA', 'BERHITUNG', 'MEMULAI PERHITUNGAN'],
    "overclock": ['PELEPASAN BATAS', 'OVERCLOCK', 'MELEBIHI BATAS', 'MEMAKAN EMOSI', 'PERTARUHAN'],
    "persetujuan": ['YA', 'IYA', 'OKE', 'OK', 'BAIKLAH', 'LAKUKAN'],
    "physics pillar": ['GRAVITASI', 'GRAVITATION', 'ELEKTROMAGNET', 'ELECTROMAGNET', 'NUKLIR LEMAH', 'WEAK NUCLEAR FORCE', 'NUKLIR KUAT', 'STRONG NUCLEAR FORCE', 'EKA-0-1-1-1', 'DVI-0-2-2-2', 'TRI-3-0-3', 'CATUR-0-4-0-4']
}
noob, pro = pilihan['physics pillar'][0:8], pilihan['physics pillar'][8:]

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

def keygenerator():
    for i in range(1, 30001):
        yield f'X{i}'

# the code
# entity
class Entity:
    def __init__(self, spesies, name):
        """Class induk"""
        db, _ = load_db()
        self.spesies = spesies
        self.name = name
        self.emotion = db['Spesies'][self.spesies]['Emosi']
        self.history = {}
        self.psycology = ''

    def get_data(self):
        data = {
            self.name: {
                'Tingkat': self.tingkat,
                'Emotion energy': self.emotion,
                'Prana': self.prana,
                'Can use Sutra': self.is_use_sutra,
                'Kondisi emosi': self.psycology,
                'Sutra history': self.history
            }
        }
        return data
    
    def get_data_with_history(self):
        data = [
            ['Emotion energy', self.emotion],
            ['Prana', self.prana],
            ['Can use sutra', self.is_use_sutra],
            ['Kondisi emosi', self.psycology]
        ]
        return data

    def __str__(self):
        """Used for open status"""
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
    """Class for human"""
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
        self.key = keygenerator()
        
        if exist:
            self.tingkat = exist['Tingkat']
            self.emotion = exist['Emotion energy']
            self.prana = exist['Prana']
            self.is_use_sutra = exist['Can use Sutra']
            self.psycology = exist['Kondisi emosi']
            self.history = exist['Sutra history']
        
        else:
            tingkat, kemungkinan = [f'T{x}' for x in range(1, 6)], [40, 30, 15, 10, 5]
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
        """Method for sutra"""
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
                next(self.key): {
                    'gaya': self.gaya,
                    'wujud': self.wujud,
                    'code': code,
                    'hasil': self.hitungan,
                    'posisi': self.position
                }
            }
            self.history.update(self.sutra_result)
            return self.sutra_result
        else:
            return f"Error: {alert}"
    
    def prakasa(self, overclock=False):
        if self.sutra_result:
            # keys
            current_keys = list(self.sutra_result.keys())[-1]
            hasil_sutra = self.sutra_result[current_keys]['hasil']
            mana_cost = 75 if len(hasil_sutra) > 2 else 50 if len(hasil_sutra) == 2 else 25
            if self.prana < mana_cost:
                return "Prana tidak cukup!"
            elif overclock:
                self.emotion = max(0, self.emotion - mana_cost)
                self.psycology = 'Nir-Atma: Emotionless' if self.emotion == 0 else 'Monster logis' if self.emotion < 250 else 'Hilang harapan' if self.emotion < 500 else 'Mulai tidak emosional' if self.emotion <= 750 else 'Terkikis'
                return f"{self.name} memanipulasi {self.sutra_result[current_keys]['hasil']} dengan wujud {self.sutra_result[current_keys]['wujud']} menggunakan gaya {self.sutra_result[current_keys]['gaya']} di {self.sutra_result[current_keys]['posisi']}" 
                
            elif self.prana >= mana_cost:
                self.prana -= mana_cost
            return f"{self.name} memanipulasi {self.sutra_result[current_keys]['hasil']} dengan wujud {self.sutra_result[current_keys]['wujud']} menggunakan gaya {self.sutra_result[current_keys]['gaya']} di {self.sutra_result[current_keys]['posisi']}"
        else:
            return 'Hitung dulu!'

class MindBreak(Exception):
    pass