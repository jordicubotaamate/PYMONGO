from Tkinter import *
from querys import loginQuery

import hashlib

class App:

    def __init__(self, master):

        #configuracio finestra
        global w 
        w = master.winfo_screenwidth()/2
        global h 
        h = master.winfo_screenheight()/2
        master.resizable(width=FALSE, height=FALSE)
        master.geometry('{}x{}'.format(w, h))
        master["bg"] = "white"

        #iniciem screen1
        self.screen1(master)
        
    #probar a conectar
    def connect(self, u, p, master, f4):
        username = u.get()
        password = hashlib.sha512(p.get()).hexdigest() #p.get()
        
        worked = loginQuery(username, password)

        if worked:
            self.cleanFrame(master)
        
        else:
            f4.place(in_=master, anchor="c", relx=.5, rely=.525)

    #def login(user, pass):
    def cleanFrame(self, frame):
        for widget in frame.winfo_children():
                widget.destroy()

    def screen1(self, master):
        #configuracio frames
        f1 = Frame(master)
        f1.pack()
        f1.place(in_=master, anchor="c", relx=.5, rely=.3)
        f1["bg"] = "white"

        f2 = Frame(master)
        f2.pack()
        f2.place(in_=master, anchor="c", relx=.5, rely=.4)
        f2["bg"] = "white"

        f3 = Frame(master)
        f3.pack()
        f3.place(in_=master, anchor="c", relx=.5, rely=.65)

        f4 = Frame(master)
        f4.pack()
        f4.place(in_=master, anchor="c", relx=.5, rely=.525)

        #username
        Luser = Label(f1, text="Username", bg="white")
        Luser.pack( side = LEFT)
        u = StringVar()
        Euser = Entry(f1, bd =5, textvariable=u)
        Euser.pack(side = LEFT)

        #password
        Lpass = Label(f2, text="Password ", bg="white",)
        Lpass.pack( side = LEFT)
        p = StringVar()
        Epass = Entry(f2, bd =5, show="*", textvariable=p)
        Epass.pack(side = LEFT)

        #button
        btLogin = Button(f3, text="Connect", command= lambda: self.connect(u, p, master, f4), width=w/60)
        btLogin.pack(side=LEFT)

        #Label error login
        Lerr = Label(f4, text="User or password error", bg="white", fg="red")
        Lerr.pack( side = LEFT)
        f4.place_forget()

        #self.screen(master)
        
        #
    #def screen2(self, master)

