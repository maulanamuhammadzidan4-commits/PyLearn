import json
import classes as c

# variables
used = True

# database
#db, us = c.load_db()

# code
while used:
    user = input('Masukkan nama anda ')
    player = c.Human(user)
    c.save(player.get_data())
    print(player)
    used = False