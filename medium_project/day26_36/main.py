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
    user = input('Masukkan nama anda ')
    if user.upper() in c.pilihan['tolakan']:
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
        if declaration.upper() in c.pilihan['deklarasi']:
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
                            print(f"{p1.name} mind health: {mind_break}")
                            continue
                        p1.useHistory(hitungan)
                        p1.prana -= 10
                        mind_break += 0.5
                        print(p1.prakasa())
                        print(f"{p1.name} mind health: {mind_break}")
                        us.update(p1.get_data())
                        c.save(us)
                        continue
                    elif acc in c.pilihan['tolakan']:
                        pass
                    
                    gaya = input()
                    if gaya.upper() in c.pilihan['tolakan']:
                        print("Keluar...")
                        break
                    else:
                        wujud = input()
                        code = input()
                        tempat = input()
                        # validasi input
                        if wujud.upper() not in c.pilihan['state of matter'] and gaya.upper() not in c.pilihan['physics pillar']:
                            print(f"Wujud {wujud} dan gaya {gaya} tidak ada!")
                            mind_break += 2
                            break
                        elif wujud.upper() not in c.pilihan['state of matter'] or gaya.upper() not in c.pilihan['physics pillar']:
                            mind_break += 4
                            if wujud.upper() not in c.pilihan['state of matter']:
                                print(f"Wujud {wujud} tidak ada!")
                                break
                            else:
                                print(f"Gaya {gaya} tidak ada!")
                                break
                        scale = 'Pro' if gaya.upper() in c.pro else 'Noob'
                        if scale == 'Pro':
                            perhitungan = p1.sutra(gaya, wujud, code, tempat)
                            if perhitungan == 'Error':
                                print(f"{perhitungan}: Perhitungan salah.")
                                mind_break += 5
                                print(f"{p1.name} mind health: {mind_break}")
                                continue
                            mind_break += 0.5
                            print(p1.prakasa())
                            print(f"{p1.name} mind health: {mind_break}")
                            us.update(p1.get_data())
                            c.save(us)
                            continue
                        elif scale == 'Noob':
                            perhitungan = p1.sutra(gaya, wujud, code, tempat)
                            if perhitungan == 'Error':
                                print(f"{perhitungan}: Perhitungan salah.")
                                mind_break += 5
                                continue
                    mind_break += 1
                    print(p1.prakasa())
                    print(f"{p1.name} mind health: {mind_break}")
                    us.update(p1.get_data())
                    c.save(us)

                elif p1.is_use_sutra:
                    gaya = input()
                    if gaya.upper() in c.pilihan['tolakan']:
                        print("Keluar...")
                        break
                    else:
                        wujud = input()
                        code = input()
                        tempat = input()
                        # validasi input
                        if wujud.upper() not in c.pilihan['state of matter'] and gaya.upper() not in c.pilihan['physics pillar']:
                            print(f"Wujud {wujud} dan gaya {gaya} tidak ada!")
                            mind_break += 2
                            break
                        elif wujud.upper() not in c.pilihan['state of matter'] or gaya.upper() not in c.pilihan['physics pillar']:
                            mind_break += 4
                            if wujud.upper() not in c.pilihan['state of matter']:
                                print(f"Wujud {wujud} tidak ada!")
                                break
                            else:
                                print(f"Gaya {gaya} tidak ada!")
                                break
                        scale = 'Pro' if gaya.upper() in c.pro else 'Noob'
                        if scale == 'Pro':
                            perhitungan = p1.sutra(gaya, wujud, code, tempat)
                            if perhitungan == 'Error':
                                print(f"{perhitungan}: Perhitungan salah.")
                                mind_break += 5
                                continue
                            mind_break += 0.5
                            print(p1.prakasa())
                            print(f"{p1.name} mind health: {mind_break}")
                            us.update(p1.get_data())
                            c.save(us)
                            continue
                        elif scale == 'Noob':
                            perhitungan = p1.sutra(gaya, wujud, code, tempat)
                            if perhitungan == 'Error':
                                print(f"{perhitungan}: Perhitungan salah.")
                                mind_break += 5
                                continue
                    mind_break += 1
                    print(p1.prakasa())
                    print(f"{p1.name} mind health: {mind_break}")
                    us.update(p1.get_data())
                    c.save(us)
                else:
                    print(f"{p1.name} tidak bisa mengolah prananya.")
                    break
            
        elif declaration.upper() in c.pilihan['overclock']:
            if p1.prana > 25:
                print("Lah buat apa jier")
                continue
            else:
                print("Bahaya, sistem limbik sedang dikuras")
                p1.overclock()
                hasil, _ = p1.penyelarasan_prana()
                if hasil == 'Nir atma':
                    print(f'{p1.name} melakukan pelanggaran berat. Energi emosi langsung dihapus.')
                    us.update(p1.get_data())
                    c.save(us)
                    break
                print(hasil)
                gaya = input()
                if gaya.upper() in c.pilihan['tolakan']:
                    print("Keluar...")
                    break
                else:
                    wujud = input()                        
                    code = input()
                    tempat = input()
                    # validasi input
                    if wujud.upper() not in c.pilihan['state of matter'] and gaya.upper() not in c.pilihan['physics pillar']:
                        print(f"Wujud {wujud} dan gaya {gaya} tidak ada!")
                        mind_break += 2
                        break
                    elif wujud.upper() not in c.pilihan['state of matter'] or gaya.upper() not in c.pilihan['physics pillar']:
                        mind_break += 4
                        if wujud.upper() not in c.pilihan['state of matter']:
                            print(f"Wujud {wujud} tidak ada!")
                            break
                        else:
                            print(f"Gaya {gaya} tidak ada!")
                            break
                p1.sutra(gaya, wujud, code, tempat)
                print(p1.sutra_result)
                mind_break += 5
                print(p1.prakasa())
                print(f"{p1.name} mind health: {mind_break}")
                us.update(p1.get_data())
                c.save(us)
        elif declaration.upper() in ['STATUS OPEN', 'OPEN STATUS']:
            print(p1)
            continue
        elif declaration.upper() in c.pilihan['tolakan']:
            mind_break = 0
            print('Ok')
            dipakai = False