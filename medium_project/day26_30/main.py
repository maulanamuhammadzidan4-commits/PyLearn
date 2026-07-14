import classes as c

# variables
used = True
dipakai = True
mind_break = 0

# database
db, us = c.load_db()

# code
print("---Selamat datang di Simulasi Limbic-Compiler Project Lokantara")
while used:
    dipakai = True
    if mind_break > 10:
        raise c.MindBreak("Otakmu mengalami overheat! Tidak bisa apa-apa.")
    user = input('Masukkan nama anda ')
    cek = user.upper()
    if cek in c.pilihan['tolakan']:
        print("Terimakasih sudah bermain!")
        used = False
        continue
    elif user in us:
        p1 = c.Human(user, us[user])
    else:
        p1 = c.Human(user)
        
    while dipakai:
        declaration = input()
        tes = declaration.upper()
        if tes in c.pilihan['deklarasi']:
            p1.declaration(declaration)
            declarated = True
            while declarated:
                if mind_break > 10.0:
                    raise c.MindBreak("OverheatError: Kepalamu terbakar karena terus-terusan menghitung.")
                hasil, _ = p1.penyelarasan_prana()
                print(hasil)
                if p1.prana >= 500 and p1.history:
                    acc = input("Apakah ingin menggunakan hystory? ").upper()
                    if acc in c.pilihan['persetujuan']:
                        hitungan = input(f"Pilihan history: {list(p1.history.keys())}\n")
                        if hitungan not in list(p1.history.keys()):
                            print("Masukkan nilai yang benar!")
                            mind_break += 1
                            continue
                        sutra = us[p1.name]['Sutra history'][hitungan]
                        p1.sutra(sutra['gaya'], sutra['wujud'], sutra['code'], sutra['posisi'])
                        p1.prana -= 50
                        mind_break += 0.5
                        print(p1.prakasa())
                        c.save(p1.get_data_with_history())
                    elif acc in c.pilihan['tolakan']:
                        print()
                    
                    gaya = input()
                    if gaya.upper() in c.pilihan['tolakan']:
                        declarated = False
                        continue
                    else:
                        wujud = input()
                        code = input()
                        tempat = input()
                        p1.sutra(gaya, wujud, code, tempat)
                    mind_break += 1
                    print(p1.prakasa())
                    c.save(p1.get_data())
                    continue


            
        elif tes in c.pilihan['overclock']:
            pass
        elif tes in ['STATUS OPEN', 'OPEN STATUS']:
            print(p1)
            continue
        elif tes in c.pilihan['tolakan']:
            print('Ok')
            dipakai = False