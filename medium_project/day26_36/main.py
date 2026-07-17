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
    # Loop utama yang mencakup seluruh urutan kode
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
        # Loop yang bertugas untuk melakukan perhitungan. Dimulai dari deklarasi dan seterusnya.
        declaration = input()
        tes = declaration.upper()
        if tes in c.pilihan['deklarasi']:
            p1.declaration(declaration)
            declarated = True
            while declarated:
                # loop perhitungan, bisa memilih menggunakan history atau tidak
                if mind_break > 10.0:
                    raise c.MindBreak("OverheatError: Kepalamu terbakar karena terus-terusan menghitung.")
                hasil, _ = p1.penyelarasan_prana()
                print(hasil)
                if p1.prana >= 500 and p1.history:
                    # blok kode jika memilih menggunakan history
                    acc = input("Apakah ingin menggunakan history? ").upper()
                    if acc in c.pilihan['persetujuan']:
                        hitungan = input(f"Pilihan history: {list(p1.history.keys())}\n")
                        print(p1.is_history)
                        if hitungan not in list(p1.history.keys()):
                            print("Masukkan nilai yang benar!")
                            mind_break += 1
                            continue
                        p1.useHistory(hitungan)
                        print(p1.is_history)
                        p1.prana -= 50
                        mind_break += 0.5
                        print(p1.prakasa())
                        print(mind_break)
                        us.update(p1.get_data())
                        c.save(us)
                        continue
                    elif acc in c.pilihan['tolakan']:
                        print()
                    
                    gaya = input()
                    if gaya.upper() in c.pilihan['tolakan']:
                        break
                    else:
                        wujud = input()
                        code = input()
                        tempat = input()
                        scale = 'Pro' if gaya.upper() in c.pro else 'Noob'
                        if scale == 'Pro':
                            p1.sutra(gaya, wujud, code, tempat)
                            mind_break += 0.5
                            print(p1.prakasa())
                            print(mind_break)
                            us.update(p1.get_data())
                            c.save(us)
                            continue
                        elif scale == 'Noob':
                            p1.sutra(gaya, wujud, code, tempat)
                    mind_break += 1
                    print(p1.prakasa())
                    print(mind_break)
                    us.update(p1.get_data())
                    c.save(us)

                elif p1.is_use_sutra:
                    gaya = input()
                    if gaya.upper() in c.pilihan['tolakan']:
                        break
                    wujud = input()
                    code = input()
                    tempat = input()
                    scale = 'Pro' if gaya.upper() in c.pro else 'Noob'
                    if scale == 'Pro':
                        p1.sutra(gaya, wujud, code, tempat)
                        mind_break += 0.5
                        print(p1.prakasa())
                    elif scale == 'Noob':
                        p1.sutra(gaya, wujud, code, tempat)
                    mind_break += 1
                    print(mind_break)
                    print(p1.prakasa())
                    print(mind_break)
                    us.update(p1.get_data())
                    c.save(us)
                else:
                    print(f"{p1.name} tidak bisa mengolah prananya.")
                    break
            
        elif tes in c.pilihan['overclock']:
            if p1.prana > 25:
                print("Lah buat apa jier")
                continue
            else:
                print("Bahaya, sistem limbik sedang dikuras")
                p1.overclock()
                p1.sutra(input('gaya '), input('wujud '), input(), input('posisi'))
                mind_break += 5
                print(p1.prakasa())
                print(mind_break)
                us.update(p1.get_data())
        elif tes in ['STATUS OPEN', 'OPEN STATUS']:
            print(p1)
            continue
        elif tes in c.pilihan['tolakan']:
            us.update(p1.get_data())
            c.save(us)
            print('Ok')
            dipakai = False