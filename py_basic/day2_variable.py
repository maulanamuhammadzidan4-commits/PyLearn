# Variabel adalah wadah untuk menyimpan data
# Di Python, untuk mendeklarasikan sebuah variabel, tidak ada kata kunci khusus. Contoh:
x = 'Jawa'

# Ada aturan penamaan di Python, yakni:
"""
1. Harus diawali huruf atau underscore '_'
2. Tidak boleh diawali angka

contoh salah:
1pulau = 'Sumatra'
pulau-satu = 'Kalimantan'
pulau ini = 'Papua'
"""

# Multiple values
a, b, c, = "Sunda", 2012, True # menyimpan beberapa data pada beberapa variabel
print(a, b, c) # Hasil: Sunda 2012 True

d = e = f = "Aceh" # menyimpan satu data ke beberapa variabel
print(d, e, f) # Hasil: Aceh Aceh Aceh

pulau = ["Jawa", "Papua", "Kalimantan"] # Ini disebut "unpacking", yang memungkinkan untuk mengekstrak data dari list
g, h, i = pulau
print(g, h, i) # Hasil: Jawa Papua Kalimantan

# Output variabel
# Menggunakan statement print()
print(a, b, c, d, e, f, g, h, i) # Hasil: Sunda 2012 True Aceh Aceh Aceh Jawa Papua Kalimantan
print(b + 67) # Hasil: 2079. Operator "+" menjadi operator matematika
print(a + d) # Hasil: SundaAceh. Operator "+" tidak menjadi operator matematika

# Varabel global
# Semua variabel di atas adalah variabel global
negara = "Indonesia"
def fungsiGweh():
    negara = "Jepang"
    print(negara) # Hasil: Jepang. Karena var negara merupakan var lokal
fungsiGweh()
print(negara) # Hasil: Indonesia. Karena var negara di sini adalah variabel global