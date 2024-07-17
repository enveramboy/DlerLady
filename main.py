from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from pygame import mixer
import math
import cards

# Initial Window Set Up

# music
mixer.init()
MASTER_VOL = 0.5
for i in range(8): mixer.Channel(i).set_volume(MASTER_VOL)
music = {
    "click_1": mixer.Sound(r"sounds\click_1.mp3"),
    "alarm_1": mixer.Sound(r"sounds\alarm_1.mp3"),
    "click_2": mixer.Sound(r"sounds\click_2.mp3"),
    "Price": mixer.Sound(r"sounds\Price.mp3"),
    "Beneath the Mask": mixer.Sound(r"sounds\Beneath the Mask.mp3"),
    "Nami's Theme": mixer.Sound(r"sounds\One Piece - Nami's Theme.mp3"),
}

win = Tk()
win.title("DlerLady")
icn = ImageTk.PhotoImage(Image.open(r"imgs\icon.jpg.png"))
win.iconphoto(False, icn)
win.minsize(190, 198)
win.maxsize(190, 198)

def txt_ani(texts):
    cnt_o = 0
    def h1():
        nonlocal cnt_o, texts
        msg = ""
        cnt_i = 0

        def h2():
            nonlocal cnt_i, txt, msg
            if cnt_i < len(txt):
                msg = msg + txt[cnt_i]
                lbl_out.config(text=msg)
                cnt_i += 1
                win.after(50, h2)

        if cnt_o < len(texts):
            txt = texts[cnt_o]
            h2()
            wait = (len(texts[cnt_o]) + 16) * 50
            cnt_o += 1
            win.after(wait, h1)
    h1()

def play(file, channel, loop): mixer.Channel(channel).play(mixer.Sound(file), loops=loop)

def openImg(path, width, height):
        img = Image.open(path)
        img.thumbnail((width, height))
        img = ImageTk.PhotoImage(img)
        return img

def confirm(btn_confirm):
    val = ent_msg.get()
    ent_msg.delete(0, END)
    btn_confirm.destroy()
    return val

def exe():
    play(music["click_1"], 0, 0)
    txt = ent_msg.get()
    ent_msg.delete(0, END)

    if txt == "" or txt == "Enter a command here": txt_ani(["sorry darling", "i'm gonna need you to speak up", "so what will it be?"])

    elif txt == "hey": txt_ani(["hey yourself. :)", "what can I do for you?"])
    
    elif txt == "what's your favorite color?": txt_ani(["purple darling. hehe", "purple flowers are just amazing", "anything else you need to know?"])

    elif txt == "songs":
        txt_ani(["you got it!", "made you a list of all my songs", "need anything else? :)"])
        cWin = Toplevel(win, bg="#0A0C18")
        songs = ""
        for i in range(len(music)): songs = songs+list(music.keys())[i]+"\n"
        Label(cWin, text=songs, fg="#FFEE02", bg="#0A0C18", font=('Calisto MT', 10)).pack()
        cWin.mainloop()

    elif txt == "play":
        txt_ani(["sure thing.", "what song would you like to play?"])
        def h():
            song = confirm(btn_confirm)
            if not any(map(lambda e: song == e, list(music.keys()))): 
                txt_ani(["i'm afraid i don't have that one...", "sorry!", "anything else i can do for you?"])
                return
            play(music[song], 1, -1)
            txt_ani(["ok, playing " + song, "anything else i can do?"])
        
        btn_confirm = Button(frm_msg, text="©", bg="#080205", fg="#9EEFD6", relief=RAISED, font=('Calisto MT', 10), command=h)
        btn_confirm.grid(column=1, row=0)

    
    elif txt == "stop":
        mixer.Channel(1).stop()
        txt_ani(["sure thing mister.", "stopped the music.", "what else will it be?"])
    
    elif txt == "volume":
        def h():
            MASTER_VOL = int(confirm(btn_confirm))
            for i in range(8): mixer.Channel(i).set_volume(MASTER_VOL)
            txt_ani(["volume set to " + str(MASTER_VOL), "anything else? :)"])
        
        btn_confirm = Button(frm_msg, text="©", bg="#080205", fg="#9EEFD6", relief=RAISED, font=('Calisto MT', 10), command=h)
        btn_confirm.grid(column=1, row=0)
        txt_ani(["sure thing dandy.", "what would you like to set it to?"])

    elif txt == "mute":
        txt_ani(["sure thing dandy.", "what else do you need? ;)"])
        for i in range(8): mixer.Channel(i).set_volume(0)

    elif txt == "unmute":
        txt_ani(["on it!", "anything else?"])
        for i in range(8): mixer.Channel(i).set_volume(MASTER_VOL)

    elif txt == "timer":
        
        def timerWin():
            btn_confirm.destroy()
            t = ent_msg.get()
            s = int(float(t)*60)
            ent_msg.delete(0, END)
            txt_ani(["roger that dandy.", f"timer set for {t} min(s)", "anything else you need?"])

            tWin = Toplevel(win, bg="#0F202A")
            tWin.title(f"Timer for {t} min(s)")
            tWin.iconphoto(False, icn)

            prog = ttk.Progressbar(tWin, orient=HORIZONTAL, length=100, mode='determinate')
            prog.pack(pady=4)

            lbl_t = Label(tWin, text="t", fg="#32ADCF", bg="#0F202A", font=('Malgun Gothic', 10))
            lbl_t.pack()

            def update():
                nonlocal s
                s -= 1
                lbl_t.config(text=f"{math.floor(s/60)}:{s%60}") if s % 60 >= 10 else lbl_t.config(text=f"{math.floor(s/60)}:0{s%60}")
                prog['value'] += (1/(float(t)*60))*100

            for i in range(s): tWin.after(i*1000, update)

            def h():
                def b(): tWin.destroy()
                def z(c, timeout, inc):
                    if timeout == 0: return
                    def j():
                        nonlocal c
                        lbl_t.config(fg="#EA5DC5") if c else lbl_t.config(fg="#32ADCF")
                    tWin.after(1000*inc, j)
                    z(not c, timeout-1, inc+1)
                play(music["alarm_1"], 2, 1)
                z(True, 12, 1)
                tWin.after(12000, b)

            tWin.after(s*1000, h)

        txt_ani(["you got it dandy.", "for how many minutes?"])
        btn_confirm = Button(frm_msg, text="©", bg="#080205", fg="#9EEFD6", relief=RAISED, font=('Malgun Gothic', 10), command=timerWin)
        btn_confirm.grid(column=1, row=0)

    elif txt == "cards":
        txt_ani(["sure dandy.", "here are all the cards.", "anything else you need? ;)"])
        cWin = Toplevel(win, bg="#141218")
        cWin.title("cards")
        cWin.iconphoto(False, icn)
        Label(cWin, text="Standard Deck (52 Cards)", fg="#DAFC5D", bg="#30341F", font=('Malgun Gothic', 12)).pack(pady=5)
        frm_cards = Frame(cWin, bg="#141218")
        frm_cards.pack()
        c = 0
        r = 0
        imgs = []
        for card in cards.deck:
            img = openImg(card.p, 60, 60)
            imgs.append(img)
            if (c % 7 == 0 and c != 0):
                Label(frm_cards, image=img).grid(row=r, column=c, padx=5, pady=5)
                r += 1
                c = 0
            else:
                Label(frm_cards, image=img).grid(row=r, column=c, padx=5, pady=5)
                c += 1
        cWin.mainloop()
    
    elif txt == "card":
        pos = 0
        def f():
            play(music["click_2"], 2, 0)
            nonlocal pos
            pos = 0 if pos >= (len(imgs)-1) else pos + 1
            img.configure(image=imgs[pos])
            name.configure(text=names[pos])
        def b():
            play(music["click_2"], 2, 0)
            nonlocal pos
            pos = (len(imgs)-1) if pos == 0 else pos - 1
            img.configure(image=imgs[pos])
            name.configure(text=names[pos])


        txt_ani(["on it. ;)", "need anything else?"])
        cWin = Toplevel(win, bg="#11181B")
        cWin.title("card")
        cWin.minsize(154, 120)
        cWin.maxsize(154, 120)

        imgs = []
        names = []
        for card in cards.deck: imgs.append(openImg(card.p, 80, 80))
        for card in cards.deck: names.append(card.n)

        img = Label(cWin, image=imgs[pos])
        img.pack(pady=4)

        frm_inp = Frame(cWin, bg="#11181B")
        frm_inp.pack()

        btn_l = Button(frm_inp, text="«", font=('Malgun Gothic', 8), bg="#11181B", fg="#FEFC00", padx=3, command=b).pack(side=LEFT, padx=3)

        frm_bd = Frame(frm_inp, bg="#FEFC00", borderwidth=1, relief=RIDGE)
        frm_bd.pack(side=LEFT, pady=2)
        name = Label(frm_bd, text=names[pos], bg="#4E4D02", fg="#FEFC00", font=('Malgun Gothic', 8), pady=1, width=16)
        name.pack()

        Button(frm_inp, text="»", font=('Malgun Gothic', 8), bg="#11181B", fg="#FEFC00", padx=3, command=f).pack(side=LEFT, padx=3)

        cWin.mainloop()

    else: txt_ani(["sorry darling I can't do that for you.", "what else can I help you with?"])

dealer_1 = ImageTk.PhotoImage(Image.open(r"imgs\dealer_2.jpeg"))
Label(win, image=dealer_1, width=190, height=150).pack()

frm_bd = Frame(win, bg="#9EEFD6", bd=1)
lbl_out = Label(frm_bd, text="", fg="#9EEFD6", bg="#080205", bd=4, font=('Calisto MT', 8))
frm_bd.pack(fill=X)
lbl_out.pack(fill=X)

frm_msg = Frame(win, bg="#080205")
frm_msg.pack()
ent_msg = Entry(frm_msg, bg="#080205", fg="#07D976", width=28, relief=FLAT)
ent_msg.insert(END, "Enter a command here")
ent_msg.bind("<Button-1>", lambda e: ent_msg.delete(0, END))
ent_msg.grid(column=0, row=0, sticky="n")
btn_msg = Button(frm_msg, text="»", bg="#080205", fg="#9EEFD6", relief=RAISED, font=('Calisto MT', 10), command=exe)
btn_msg.grid(column=1, row=0)

txt_ani(["hey, dear", "how can I help you today?"])

win.mainloop()