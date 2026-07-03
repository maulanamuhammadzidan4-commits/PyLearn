import json
from day10_py_dictionary import anime_watched as listanime
import re

JSONitem = '{"name":"Zidan", "status":"siswa", "skils":{"hardskills":"Python", "softskills":"Good at comunication"}, "hobi":"ngoding"}'

aksesJSON = json.loads(JSONitem)
ubahkJSON = json.dumps(listanime, indent=4, separators=("! ", " -> "))

print(aksesJSON["name"])
print(ubahkJSON)

# regEx
teks = 'Hai nama saya Sukarbit. Saya suka ngeklem bini orang.'
cari = re.search('aya', teks) # nyari pola 'aya'
if cari:
    print("aya? ayaya ayaya.")
else:
    print("wehan")

carisemua = re.findall('[a-k]', teks) # nyari semua huruf yang ada di rentan a sampe k
print(carisemua)

potongkata = re.split('\s', teks, maxsplit=2) # motong berdasarkan spasi untuk 2 bagian utama
print(potongkata)

gantikata = re.sub('\s', '67', teks) # ganti semua spasi jadi '67'. Bisa juga pilih seperti di atas, tapi itu opsional
print(gantikata)

# pip
'''
pip adalah manajer paket (package) untuk python.
paket berisi semua file yang dibutuhkan untuk sebuah modul.
'''

# try except else finally
# blok kode ini digunakan untuk mencegah kode berhenti jika terjadi error.
try: # digunakan untuk ngecek kode
    print(jawa) # ini akan mengebabkan error karena varabel jawa tidak ada
except NameError: # kode untuk mengatasi error
    print("Error, variabel itu tidak ada!")
except SyntaxError:
    print("sintaksnya salah bang!")
else: # kode yang dijalankan jika tidak error
    print("Kode berjalan semestinya!")
finally: # kode yang akan tetap dijalankan, tidak peduli pada blok-blok di atas
    print("Pengecekan selesai!")

# memunculkan error
class AnimeError(Exception):
    '''Ini contoh membuat sebuah exception sendiri. Harus membuat sebuah class terlebih dulu.'''
    pass

konosuba = listanime["KonoSuba"]

listanime.pop("KonoSuba")
if "KonoSuba" not in listanime: # kita bisa membuat sebuah error secara bebas (disarankan harus sesuai kebutuhan).
    listanime.update(konosuba)
    raise AnimeError("HAH! Kau tidak nonton KonoSuba!? Gak mungkin. Ini pasti kesalahan!") # bahkan jenis error nya bisa kita pilih dan edit