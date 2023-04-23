from tkinter import *
from tkinter import ttk
from Ouvrir_repertoire_class import ouvrir_repertoire
    
def fenetre_index():
    fenetre = Toplevel()
    fenetre.geometry("700x400")
    fenetre.iconbitmap('fairytail.ico')
    color='white'
    bac='indigo'
    boite=Frame(fenetre,height=500,width=500,bg=bac)
    Label(boite,text='Url', font=('Arial',25),fg=color,bg=bac).place(x=10,y=10)
    lien=Entry(boite, font=('Arial',20),fg=color,bg=bac)
    lien.place(x=10,y=50)
    Label(boite,text='Enregistrer sous',fg=color,bg=bac, font=('Arial',25)).place(x=10,y=100)
    location_btn=Button(boite,fg=color,bg=bac,activebackground=bac,activeforeground=color,text='...',pady=7,width=5,font=('Arial',10,'bold'),command=lambda:ouvrir_repertoire(location))
    location_btn.place(x=250,y=100)
    location=Entry(boite, font=('Arial',20),fg=color,bg=bac)
    location.place(x=10,y=150)
    arreter_btn=Button(boite,fg=color,bg=bac,activebackground=bac,activeforeground=color,text='Arreter',pady=7,width=15,font=('Arial',10,'bold'))
    arreter_btn.place(x=10,y=250)
    check=Checkbutton(boite,fg='green',bg=bac,activebackground=bac,activeforeground='green',text='Rappeler ce chemin',pady=7,width=15,font=('Arial',10,'bold'))
    check.place(x=10,y=200)
    demarer_btn=Button(boite,fg=color,bg=bac,activebackground=bac,activeforeground=color,text='Demarer',pady=7,width=15,font=('Arial',10,'bold'))
    demarer_btn.place(x=180,y=250)
    boite.pack(side=LEFT)
    fenetre.mainloop(10)
    
def fenetre_info():
    
    fenetre = Toplevel()
    fenetre.geometry("700x400")
    fenetre.iconbitmap('fairytail.ico')
    bac='indigo'
    boite=Frame(fenetre,height=500,width=800,bg=bac)
    
    # define columns
    columns = ('first_name', 'last_name', 'email')

    style=ttk.Style(boite)
    tree = ttk.Treeview(boite, columns=columns, show='headings')
    style.theme_use('clam')
    style.configure('Treeview',fieldbackground='indigo')

    # define headings
    tree.heading('first_name', text='First Name')
    tree.heading('last_name', text='Last Name')
    tree.heading('email', text='Email')
    tree.insert('',index=0,values=('PASCAL','YANNICK','bitsapascal@gmail.com'))
    tree.insert('',index=0,text='',values=('ROGRIGUE','LUCIEN','lucien@gmail.com'))
    
    tree.place(x=1,y=10)
    boite.pack(side=LEFT)
    fenetre.mainloop(10)
    
