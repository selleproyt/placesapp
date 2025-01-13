from userbase import createuser
import random

createuser('3', f'{random.random()}',
           "'0', '', 0); INSERT INTO Users (name, login, password, info ,tg) VALUES ('lol', 'lol', 'lol', 'lol', 12); --",
           123)
print("done")
