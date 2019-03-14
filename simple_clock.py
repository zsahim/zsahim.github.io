# zsahim.github.io
from tkinter import *

import  numpy as np

fen = Tk()
a=270
b=270
c=270
w=0
v=StringVar()
heure=12
minute=0
seconde=0



canvas = Canvas(fen, width=600, height=600)

canvas.create_oval(150,150,450,450,fill="skyblue")

for n in range(300,660,30):
    w+=1


    canvas.create_text(140*np.cos(n*np.pi/180)+300,140*np.sin(n*np.pi/180)+300,text=str(w))


canvas.pack()
canvas.create_oval(295,295,305,305,fill='black')
label=Label(fen,textvariable=v)
label.pack()

def sec():
    global  a
    global  b
    global c
    global heure
    global  minute
    global  seconde
    a+=6
    v.set(str(heure)+":"+str(minute)+":"+str(seconde))

    seconde += 1
    if seconde == 61:
        seconde = 1
        minute += 1
        if minute == 61:
            minute = 1
            heure += 1
            if heure == 13:
                heure = 1

    if a == 630:
        a=270
        b+=6
        c += 0.5



    if b == 630:
        b = 270



    if c==630:
        c=270



    canvas.delete("line")




    canvas.create_line(300, 300, 100 * np.cos(c * np.pi / 180) + 300, 100 * np.sin(c * np.pi / 180) + 300, tag="line",width=5,fill="blue")
    canvas.create_line(300, 300, 120 * np.cos(b * np.pi / 180) + 300, 120 * np.sin(b * np.pi / 180) + 300, tag="line",
                       width=3, fill="blue")
    canvas.create_line(300, 300, 140 * np.cos(a * np.pi / 180) + 300, 140 * np.sin(a * np.pi / 180) + 300, tag="line",
                       width=1, fill="blue")
    fen.after(1000,sec)


sec()


fen.mainloop()
