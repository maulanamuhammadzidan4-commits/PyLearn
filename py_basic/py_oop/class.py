class Karakter:
    def __init__(self, name, levl=1):
        self.name = name
        self.levl = levl
    def desc(self):
        return f'Nama: {self.name}\nLevel: {self.levl}'
    def levup(self):
        self.levl += 1
        return f"{self.name} naik satu level!"

player1 = Karakter("Konnie", 15)
print(player1.desc())
print(player1.levup(), player1.desc())

player1.levl = 18
print(player1.desc())