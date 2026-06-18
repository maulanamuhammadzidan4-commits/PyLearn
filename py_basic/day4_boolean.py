# ---Boolean---
# Boolean mewakili salah satu dari nilai benar (true) dan salah (false).
# Kita bisa mengevaluasi ekspresi apapun di Python.
print(67 > 12) # Memberikan nilai True
print(67 == 12) # Memberikan nilai False
print(67 < 12) # Memberikan nilai False

# Kita bisa memanfaatkan ini untuk keprluan logika pada blok if else.
nilai = 70
if nilai > 75:
    print("Selamat! Kamu lulus!")
else:
    print("Remed bang!")

# Kita juga bisa mengevaluasi nilai apapun menggunakan fungsi bool(). Yang akan memberikan nilai True atau False.
print(bool("Jawa jawa jawa")) # Memberikan nilai True
print(bool(2012)) # Memberkan nilai True
print(bool(nilai)) # Memberikan nilai True
# Semua nilai yang memiliki isi akan menghasilkan nilai True. Jadi untuk menghasilkan nilai False, kita cukup menghilangkan nilainya.
print(bool(0))  # Semua nilai ini akan mengembalikan nilai False
print(bool(0.0))
print(bool("")) 
print(bool([])) 
print(bool({}))