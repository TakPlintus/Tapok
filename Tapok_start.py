# Привет от Takplintus
import random
import colorama
from subprocess import Popen
import sys
import time
import pyglet


def AAAA():
    while True:
        print(f'\033[31m{str(random.randint(0, 1000)) * 250}', end='')
        print(end='\r')


colorama.init()
x = ['!', '?']
for i in range(7):
    print(f'Вычисляем..{random.choice(x)} Разверните окно консоли на весь экран', end='')
    time.sleep(1)
    print(end='\r')
print()
print('\033[31mTapok has been planted!\033[0m')
time.sleep(3)
for j in range(1000):
    print(f'\033[32m{str(random.randint(0, 1000)) * 250}\033[0m', end='')
    print(end='\r')
Popen([sys.executable, 'Data/Borsh.py'])
time.sleep(8)
for n in range(6000):
    print(f'\033[32m{str(random.randint(0, 1000)) * 250}', end='')
    print(end='\r')
pyglet.media.load('Data/AAA.mp3').play()
AAAA()
pyglet.app.run()