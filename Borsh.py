# Привет от Богдана
import colorama
from tkinter import *
import pyglet
import random
import os


colorama.init()
print('''          ,----------------,                 ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |  \033[31mWHAT A SHAME!\033[0m  |  |  |     |         |      |
     |  |  Bad command or |  |  |/----|`---=    |      |
     |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |," 
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------'
''')
window = Tk()
window['bg'] = 'green'
window.overrideredirect(True)
image_monkey = PhotoImage(file='Data/brat.png')
panel = Label(window, image=image_monkey)
panel.pack()


def dead():
    image_dead = PhotoImage(file='Data/dead.png')
    panel.configure(image=image_dead, bg='black')
    panel.image = image_dead
    os.system('shutdown -s')


def swap_image():
    image_dem = PhotoImage(file='Data/Демотиватор без мыла.png')
    panel.configure(image=image_dem)
    panel.image = image_dem
    btn.destroy()
    pyglet.media.load('Data/Mem.mp3').play()
    window.after(12000, dead)


btn = Button(text='Нажмите', font=('Times New Roman', 15), command=swap_image, bg='black', fg='green')
btn.pack()
window.mainloop()
pyglet.app.run()