import json
import random

mana_values, kemungkinan = [3, 6, 20, 50, 67], [20, 15, 10, 5, 1]
mana_saver = random.choices(mana_values, weights=kemungkinan, k=1)
mana = int(mana_saver[0])
wujudBenda = ['CAIR', 'PADAT', 'GAS', 'BOSE-EINSTEIN CONDENSATE', 'PLASMA']
makhluk = ['MANUSIA']

# Otak program
class MakhlukHidup:
    def __init__(self, nama, spesies, cerdas):
        self.nama = nama
        self.spesies = spesies
        self.cerdas = cerdas

class Manusia(MakhlukHidup):
    def __init__(self, nama, spesies, cerdas, berbakat, berpendidikan):
        super().__init__(nama, spesies, cerdas)
        self.berbakat = berbakat
        self.berpendidikan = berpendidikan
        self.prana = mana
        self.pakaisihir = berbakat and self.prana > 2
        self._gaya = ''
        self._wujud = ''
        self.hitungan = ''

    def open_status(self):
        status = {'Nama': self.nama, 'Spesies': self.spesies, 'Prana': self.prana, 'Bisa sihir': self.pakaisihir}
        return json.dumps(status, indent=4)

    def gaya(self, metode):
        self._gaya = metode
        return self._gaya
    
    def wujud(self, wujud_benda):
        self._wujud = wujud_benda
        return self._wujud

    def hitung(self, code):
        cells = [0] * 30000
        ptr = 0
        code_ptr = 0
        loop_map = {}
        stack = []
        output = []

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
                ptr += 1
            elif char == '<':
                ptr -= 1
            elif char == '+':
                cells[ptr] = (cells[ptr] + 1) % 256
            elif char == '-':
                cells[ptr] = (cells[ptr] - 1) % 256
            elif char == '.':
                output.append(chr(cells[ptr]))
            elif char == '[' and cells[ptr] == 0:
                code_ptr = loop_map[code_ptr]
            elif char == ']' and cells[ptr] != 0:
                code_ptr = loop_map[code_ptr]
            code_ptr += 1
            self.hitungan = ''.join(output)
        return self.hitungan
    
    def prakasa(self, lokasi):
        self.lokasi = lokasi
        if not self._gaya or not self._wujud or not self.hitungan:
            return "Lengkapi dulu yang lainnya!"
        if self.pakaisihir and self.prana > 0:
            self.prana -= 1
            return f'{self.nama} memanipulasi {self.hitungan} berwujud {self._wujud} dengan gaya {self._gaya} di {self.lokasi}.'
        else:
            return f'{self.nama} tidak bisa menggunakan sihir!'

# Keluaran program
used = True
hak = [True, False]
pilihan = ['KELUAR', 'STATUS OPEN', 'YA']
print("Selamat datang di simulasi power system (prototype).")
while used:
    berhak = random.choice(hak)
    dipake = True
    print(f"Pilih dulu spesiesmu: {''.join(makhluk).lower()}")
    login = input("Kamu spesies apa? ")
    # verifikasi
    verisikasi = login.upper()
    if verisikasi not in makhluk:
        print(f"Spesies {login} belum/tidak ada.")
        continue
    
    user1 = Manusia(input("Masukkan nama anda: "), "Manusia", True, True, berhak)
    print(f"Selamat datang tuan {user1.nama}. Ini adalah status anda:\n{user1.open_status()}\n{user1.berbakat, user1.berpendidikan, user1.cerdas}")
    
    while dipake:
        main = input("Apakah ingin mulai menghitung sihir? ")
        vmain = main.upper()
        if vmain not in pilihan:
            print("Masukkan input yang benar!")
            continue
        elif vmain == pilihan[0]:
            print("Terimakasih sudah menghitung sihir!")
            dipake = False
            used = False
        elif vmain == pilihan[1]:
            print(user1.open_status())
            continue
        else:
            if not user1.pakaisihir:
                print(f"Maaf {user1.nama}, kau tidak bisa menggunakan sihir.")
                continue
            user1.gaya(input("Ingin menggunakan gaya apa dari 4 gaya fundamental? "))
            user1.wujud(input("Ingin menggunakan wujud apa? (Wujud benda) "))
            user1.hitung(input("Masukkan kode Brainfuck mu di sini!\n"))
            print(user1.prakasa(input("Di mana sihirnya akan dijalankan? ")))
            continue