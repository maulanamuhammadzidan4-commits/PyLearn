# ---DICTIONARY---
# Dictionary digunakana untuk menyimpan data dalam pasangan key:values (kata kunci dan isi)
# Dictionary itu terurut, dapat diubah, dan tidak memungkinkan nilai duplikat
# Daripada kita membuat beberapa variabel yang berisi kumpulan data seperti pada mini projek kemarin, lebih baik kita gunakan dictionaries.
anime_watched = {
    'KonoSuba': {
        'alter title': 'Kono Subarashiki Sekai ni Shukufu wo!',
        'char': ["Kazuma", "Aqua", "Megumin", "Darkness"],
        'full name': ("Satou Kazuma", "Aqua", "Megumin", "Dustiness Ford Lalatina"),
    },
    'Re:Zero': {
        'alter title': 'Re: Zero Kara Hajimaru Isekai Seikatsu',
        'char': ["Subaru", "Emilia", "Beako", "Patrasche"],
        'full name': ("Natsuki Subaru", "Emilia", "Beatrice", "Patrasche"),
    },
    'Date a Live': {
        'alter title': 'DAL',
        'char': ["Shidou", "Tohka", "Kurumi", "Kotori"],
        'full name': ("Itsuka Shidou", "Yatogami Tohka", "Tokisaki Kurumi", "Itsuka Kotori"),
    },
    'Log Horizon': {
        'alter title': 'Log Horizon',
        'char': ["Shiroe", "Akatsuki", "Naotsugu", "Marie"],
        'full name': ("Shiroe", "Akatsuki", "Naotsugu", "Marie"),
    },
    'Kore wa Zombie Desu Ka?': {
        'alter title': 'Is This a Zombie?',
        'char': ["Yuu", "Ayumu", "Haruna", "Sera"],
        'full name': ("Eucliwood Hellscythe", "Ayumu Aikawa", "Haruna", "Seraphim"),
    },
    'JJK': {
        'alter title': 'Jujutsu Kaisen',
        'char': ["Yuta", "Yuji", "Todo", "Choso"],
        'full name': ("Yuta Okkotsu", "Itadori Yuji", "Aoi Todo", "Choso"),
    },
    'Dr. Stone': {
        'alter title': 'Dr. Stone',
        'char': ["Senku", "Kohaku", "Chrome", "Sei"],
        'full name': ("Ishigami Senku", "Kohaku", "Chrome", "Nanami Sei"),
    },
    'JoJo Bizzare Adventure': {
        'alter title': 'JoJo Kimyou na Bouken',
        'char': ["Jotaro", "Koichi", "Rohan", "Okuyasu"],
        'full name': ("Jotaro Kujo", "Koichi Hirose", "Kishibe Rohan", "Okuyasu Nijimura"),
    },
    'Uma Musume: Cinderella Gray': {
        'alter title': 'Uma Musume Cnigray',
        'char': ["Ogurin", "Belno", "Tama", "Kitahara"],
        'full name': ("Oguri Cap", "Belno Light", "Tamamo Cross", "Kitahara Jones"),
    }
}
category_characters = {
    'onechar': {"Kurumi", "Aqua", "Darkness", "Emilia", "Tohka", "Marie", "Sera", "Kohaku", "Ogurin"},
    'loli': {"Yuu", "Beako", "Haruna", "Akatsuki", "Megumin", "Kotori"},
    'waifu': frozenset({"Kurumi", "Yuu", "Akatsuki", "Ogurin"})
}
'''
Sama seperti tipe data koleksi lain, dictionary juga bisa bisa menampung semua tipe data, termasuk list, tuple, set, frozenset, dan bahkan dictionary itu sendiri.
Dengan menggunakan dictionary, kita bisa mengelompokkan data yang berhubungan menjadi satu kesatuan, sehingga lebih mudah untuk diakses dan dikelola.
Kita juga bisa membuat penanda untuk memudahkan akses data, misalnya dengan menggunakan nama anime sebagai key untuk mengakses data terkait anime tersebut. Seperti pada contoh di bawah:
'''

konosuba = anime_watched['KonoSuba']
rezero = anime_watched['Re:Zero']
dal = anime_watched['Date a Live']
log_horizon = anime_watched['Log Horizon']
kore_wa_zombie = anime_watched['Kore wa Zombie Desu Ka?']
jjk = anime_watched['JJK']
dr_stone = anime_watched['Dr. Stone']
jojo_bizzare = anime_watched['JoJo Bizzare Adventure']
uma_musume_cingray = anime_watched['Uma Musume: Cinderella Gray']

one_chan = category_characters['onechar']
loli = category_characters['loli']
wife = category_characters['waifu']

'''
Untuk mengakses data dalam dictionary, cara mengaksesnya sama seperti mengakses list, yaitu dengan menggunakan tanda kurung siku [].
Hanya saja, pada dictionary kita menggunakan key sebagai indeks untuk mengakses data, bukan angka.
Namun, jika key yang dimasukkan tidak ada dalam dictionary, maka akan terjadi error KeyError. 
Untuk menghindari error tersebut, kita bisa menggunakan method get() untuk mengakses data dalam dictionary. 
Method get() akan mengembalikan None jika key yang dimasukkan tidak ada dalam dictionary, sehingga kita bisa menangani kasus tersebut dengan lebih baik.
'''

standard_wibu = 5
wibu_level = "Sepuh" if len(anime_watched) > standard_wibu else "Biasa" if len(anime_watched) == standard_wibu else "Pemula" if len(anime_watched) < 3 else "Karbit"
print(wibu_level)

if "KonoSuba" in anime_watched:
    print("STEALLL!!!!")
else:
    print("Karbeat!!!")


for x in anime_watched:
    print(x)
    print(anime_watched[x]['alter title'])

toleransi = 1
def pedometer(onechar, loli):
    oneCount = len(onechar)
    loliCount = len(loli)

    pedometer = "Pengidap pedophilia" if oneCount < loliCount else "Mencurigakan" if loliCount >= 5 else "Biasa"
    return pedometer
def pedometerV2(waifu, loli):
    loliSearch = [z for z in waifu if z in loli]
    totalLoli = len(loliSearch)

    pedometerV2 = "Panggil FBI!!!" if totalLoli > toleransi else "Akan kuawasi" if totalLoli == toleransi else "Aman"
    return pedometerV2

print(pedometer(one_chan, loli))
print(pedometerV2(wife, loli))