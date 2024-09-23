#Making Google Translator
from fnmatch import translate
from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES
def change(text="type",src="English",dest="Hindi"):
    textt=text
    src2=src
    dest1=dest
    trans=Translator()
    trans1=trans.translate(textt,src=src2,dest=dest1)
    return trans1
def data():
    s=combo1.get()
    d=combo2.get()
    msg=sor_text1.get(1.0,END)
    yep=change(text=msg,src=s,dest=d)
    sor_text2.delete(1.0,END)
    sor_text2.insert(END,yep)

root=Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg="light pink")
leb=Label(root,text="TRANSLATOR",font=("Roman Italic",40,"bold"),bg="Light Pink")
leb.place(x=60,y=40,height=50,width=400)
frame=Frame(root)
frame.pack(side=BOTTOM)
leb=Label(root,text="SOURCE TEXT",font=("Roman Italic",20,"bold"),bg="light pink",fg="blue")
leb.place(x=60,y=100,height=40,width=400)
sor_text1=Text(root,font=("Roman Italic",40,"bold"),wrap=WORD)
sor_text1.place(x=10,y=150,height=100,width=480)
list_box=list(LANGUAGES.values())
combo1=ttk.Combobox(root,value=list_box)
combo1.place(x=10,y=270,height=40,width=120)
combo1.set("English")
button=Button(root,text="Translate",relief=SUNKEN,command=data)
button.place(x=170,y=270,height=40,width=150)
combo2=ttk.Combobox(root,value=list_box)
combo2.place(x=360,y=270,height=40,width=120)
combo2.set("English")
lb1=Label(root,text="TRANSLATED TEXT")
lb1.place(x=50,y=330,height=40,width=400)
sor_text2=Text(root,font=("Roman Italic",40,"bold"),wrap=WORD)
sor_text2.place(x=10,y=400,height=250,width=480)

root.mainloop()
