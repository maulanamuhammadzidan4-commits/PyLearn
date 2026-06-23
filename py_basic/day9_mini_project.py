# Mini project
title_fav_anime = ["KonoSuba", "Re:Zero", "Date a Live", "Log Horizon", "Kore wa Zombie Desu Ka?", "JJK", "Dr. Stone", "JoJo Bizzare Adventure"]
alter_title = ("Kono Subarashiki Sekai ni Shukufu wo!", "Re: Zero Kara Hajimaru Isekai Seikatsu", "DAL", "Log Horizon", "Kore wa Zombie Desu Ka?", "Jujutsu Kaisen", "Dr. Stone", "JoJo Kimyou na Bouken")
fav_char_name = (
    ["Kazuma", "Aqua", "Megumin", "Darkness"],
    ["Subaru", "Emilia", "Beako", "Patrasche"], # Jangan cari yang tidak ada
    ["Shidou", "Tohka", "Kurumi", "Kotori"],
    ["Shiroe", "Akatsuki", "Naotsugu", "Marie"],
    ["Yuu", "Ayumu", "Haruna", "Sera"],
    ["Yuta", "Yuji", "Todo", "Choso"],
    ["Senku", "Kohaku", "Chrome", "Sei"],
    ["Jotaro", "Koichi", "Rohan", "Okuyasu"]
)
full_name = [
    ("Satou Kazuma", "Aqua", "Megumin", "Dustiness Ford Lalatina"),
    ("Natsuki Subaru", "Emilia", "Beatrice", "Patrasche"),
    ("Itsuka Shidou", "Yatogami Tohka", "Tokisaki Kurumi", "Itsuka Kotori"),
    ("Shiroe", "Akatsuki", "Naotsugu", "Marie"),
    ("Eucliwood Hellscythe", "Ayumu Aikawa", "Haruna", "Seraphim"),
    ("Yuta Okkotsu", "Itadori Yuji", "Aoi Todo", "Choso"),
    ("Ishigami Senku", "Kohaku", "Chrome", "Nanami Sei"),
    ("Jotaro Kujo", "Koichi Hirose", "Kishibe Rohan", "Okuyasu Nijimura")
]
print(f'{type(title_fav_anime)}\n{type(alter_title)}\n{type(fav_char_name)}\n{type(full_name)}')

for x in alter_title:
    print(x)

if "KonoSuba" in title_fav_anime or "Kono Subarashiki Sekai ni Shukufu wo!" in alter_title:
    print("STEALLL!!!!")
else:
    print("Woi Karbit")

print(full_name[2:5])

total_fav_anime = len(alter_title)
standar_wibu = 5

tipe_wibu = "Sepuh" if total_fav_anime > standar_wibu else "Biasa" if total_fav_anime == standar_wibu else "Pemula" if total_fav_anime < 3 else "Karbit"
print(tipe_wibu)

print(fav_char_name[2][2])

oneChar = {"Kurumi", "Aqua", "Darkness", "Emilia", "Tohka", "Marie", "Sera", "Kohaku"}
loliChar = {"Yuu", "Beako", "Haruna", "Akatsuki", "Megumin", "Kotori"}
oneCount = len(oneChar)
loliCount = len(loliChar)

pedometer = "Pengidap pedophilia" if oneCount < loliCount else "Mencurigakan" if loliCount >= 5 else "Biasa"
print(pedometer)

waifu = frozenset({"Kurumi", "Yuu", "Akatsuki"})
toleransi = 1

loliSearch = [z for z in waifu if z in loliChar]
totalLoli = len(loliSearch)

pedometerV2 = "Panggil FBI!!!" if totalLoli > toleransi else "Akan kuawasi" if totalLoli == toleransi else "Aman"
print(pedometerV2)