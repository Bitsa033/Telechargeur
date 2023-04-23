from tkinter import *
from Fenetre_class import *

def fenetre_principal():
    "je crée des variables globales qui seront reconnues dans d'autres fonctions"
    global tk
    global bar_nav
    global couleur_fond
    couleur_fond='blue'
    tk=Tk()

    tk.title('Menu bar')
    tk.geometry('1000x600')
    tk.config(bg='indigo')
    img=PhotoImage(file='rugal.png')
    Label(tk,image=img,).place(x=0,y=50)
    entete_frame=Frame(tk,bg=couleur_fond,height=50,width=200).pack(fill=X,side=TOP)
    bar_nav=Button(entete_frame,text='≡',font=('Microsoft',19,'bold'),bg=couleur_fond,bd=0,activebackground=couleur_fond,command=lambda:menu(tk,bar_nav))
    bar_nav.place(x=0,y=0)
    lb=Label(entete_frame,text='Menu bar',font=('Microsoft',20,'bold'),bg=couleur_fond,pady=5,fg='green')
    lb.place(x=35,y=0)


    tk.mainloop()

def menu(a:Tk,b:Button):
    def collapse():
        b['text']='≡'
        menu_bar.destroy()
        global tk
        global bar_nav
        global couleur_fond
        b.config(command=lambda:menu(tk,bar_nav))
        
    "on configure notre bouton pour appeler la methode [collapse]"
    b['text']='X'
    b['command']=collapse
    "on change la position de l'image en X"
    "on adapte la hauteur de la boite en fonction de la taille de la fenetre"
    height_fr=a.winfo_height()
    "on crée une boite qui va contenir notre menu"
    menu_bar=Frame(a,height=height_fr,width=200,bg=couleur_fond)
    menu_bar.place(x=0,y=50)
    "on crée notre menu donc les différents liens"
    nouveau=Button(menu_bar,text='+ Nouveau',font=('Microsoft',15,'bold'),bg=couleur_fond,bd=0,activebackground=couleur_fond,command=fenetre_index)
    nouveau.place(x=0,y=0)
    fin=Button(menu_bar,text='↓ Terminés',font=('Microsoft',15,'bold'),bg=couleur_fond,bd=0,activebackground=couleur_fond)
    fin.place(x=0,y=100)
    en_cours=Button(menu_bar,text='֎ Incomplets',font=('Microsoft',15,'bold'),bg=couleur_fond,bd=0,activebackground=couleur_fond)
    en_cours.place(x=0,y=50)
    infos=Button(menu_bar,text='ꙭ A propos',font=('Microsoft',15,'bold'),bg=couleur_fond,bd=0,activebackground=couleur_fond,command=fenetre_info)
    infos.place(x=0,y=150)