import json

class entity:
    def __init__(self, nama):
        self.nama = nama

    def move(self, arah):
        print(f'{self.nama} bergerak ke {arah}')

class Player(entity):
    def __init__(self, nama, kelas, lvl, coin):
        self.nama = nama
        self.kelas = kelas
        self.lvl = lvl
        self.coin = coin
        self.hpmp()
        self.heal = self.HealSkil()

    def hpmp(self):
        pangkat = 'Master' if self.lvl >= 100 else 'Veteran' if self.lvl >= 75 else 'Senior' if self.lvl >= 45 else 'Junior'
        self.hp = 100
        self.mp = 50
        self.atk = 10
        match pangkat:
            case 'Master':
                self.hp += 900
                self.mp += 450
                self.atk += 90
            case 'Veteran':
                self.hp += 650
                self.mp += 325
                self.atk += 65
            case 'Senior':
                self.hp += 400
                self.mp += 200
                self.atk += 40
            case 'Junior':
                self.hp += 100
                self.mp += 50
                self.atk += 10
            
    def status_open(self):
        status = {"Name": self.nama, "Class": self.kelas, "Level": self.lvl, "HP": self.hp, "MP": self.mp}
        tampilkan = json.dumps(status, indent=3)
        return tampilkan
    
    def attack(self, target):
        target.hp = target.hp - self.atk
        print(f'{target.nama} diserang oleh {self.nama}.\n{target.nama} menerima kerusakan sebesar {self.atk}')
        if isinstance(target, Monster) and target.hp <= 0:
            print(f'{target.nama} telah dikalahkan!')
            if target.coin > 0:
                self.coin += target.coin
                print(f'{self.nama} mendapatkan {target.coin} koin dari {target.nama}!')
                target.coin = 0
    class HealSkil():
        def selfheal(self):
            mp_cost = 50
            mp_cek = 'fair' if self.mp >= mp_cost else 'warning'
            hp_heal = 50
            match mp_cek:
                case 'fair':
                    self.hp += hp_heal
                    self.mp -= mp_cost
                    print(f'{self.nama} menyembuhkan dirinya sendri!')
                case 'warning':
                    print(f"{self.name} tidak punya cukup energi untuk menyembuhkan!")
        def heal(self, target):
            mp_cost = 50
            mp_cek = 'fair' if self.mp >= mp_cost else 'warning'
            hp_heal = 50
            match mp_cek:
                case 'fair':
                    target.hp += hp_heal
                    self.mp -= mp_cost
                    print(f'{self.nama} menyembuhkan {target}!')
                case 'warning':
                    print(f"{self.name} tidak punya cukup energi untuk menyembuhkan {target.name}!")

class Monster(entity):
    def __init__(self, nama, hp, coin, atk):
        self.nama = nama
        self.hp = hp
        self.coin = coin
        self.atk = atk
    def attack(self, target):
        target.hp = target.hp - self.atk
        print(f'{target.nama} diserang oleh {self.nama}.\n{target} menerima kerusakan sebesar {self.atk}')
    


p1 = Player('SKG', 'Petualang', 120, 12345432)
p2 = Player('ASKG', 'Sword master', 90, 4554545)
s1 = Monster('Slime', 100, 5, 20)
print(p1.status_open())
print(p2.status_open())
p1.attack(p2)
print(p2.status_open())
heal = p2.HealSkil.selfheal(p2)
print(p2.status_open())
p1.move("Kanan")
p2.move("Kiri")
p1.attack(s1)