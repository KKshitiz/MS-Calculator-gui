from tkinter import *
from tkinter import ttk


entry1t=""
entry2t="0"
memory="0"


#functions to add memory operations
def memclear():
    global memory
    memory="0"

def memadd():
    global memory
    memory=int(memory)+int(entry2t)

def memsub():
    global memory
    memory-=int(entry2t)

def memsave():
    global memory
    memory=int(entry2t)

def memrecall():
    global memory,entry2t
    entry2t=str(memory)
    entry2.config(text=entry2t)

#mathematical operations

def equal():
    
    global entry1t,entry2t
    if not "=" in entry1t:
        entry1t+=" "+entry2t+"="
        entry1.config(text=entry1t)
        entry2.config(text=eval(entry1t[:-1]))
        entry2t=str(eval(entry1t[:-1]))

def add():
    global entry1t,entry2t
    entry1t=entry2t+"+"
    disp=entry2t+" + "
    entry1.config(text=disp)
    entry2t=""

def sub():
    global entry1t,entry2t
    entry1t=entry2t+"-"
    disp=entry2t+" - "
    entry1.config(text=disp)
    entry2t=""

def mul():
    global entry1t,entry2t
    entry1t=entry2t+"*"
    disp=entry2t+" X "
    entry1.config(text=disp)
    entry2t=""

def div():
    global entry1t,entry2t
    entry1t=entry2t+"/"
    disp=entry2t+" ÷ "
    entry1.config(text=disp)
    entry2t=""

#to separate digits
def separator(a):
    for x in range(len(a)-3,-1,-3):
        if x!=0:
            a=a[:x]+","+a[x:]
    return a

#func to implement c button
def clear12():
    global entry2t,entry1t
    entry1t=""
    entry2t="0"
    entry1.config(text=entry1t)
    entry2.config(text=entry2t)

#negate button
def negate():
    global entry2t
    entry2t=str(-1*int(entry2t))
    entry2.config(text=entry2t)

#to implement backspace
def backspace():
    global entry2t
    entry2t=entry2t[:-1]
    if entry2t=="":
        entry2t="0"
    entry2.config(text=separator(entry2t))

#func to implement ce button
def clear2():
    global entry2t
    entry2t="0"
    entry2.config(text=entry2t)

#func to input and display
def inputentry2(a):
    global entry2t
    if a=="." and ("." in entry2t):
        pass
    else:
        if entry2t=="0" and a=="0":
            pass
        else:
            if entry2t=="0":
                entry2t=""
            entry2t+=a
            entry2.config(text=separator(entry2t))

def startCalc():
    root=Tk()
    root.title("Calculator")
    root.configure(bg="#1F1F1F")
    root.resizable(0,0)
    root.iconphoto(False,PhotoImage(file='C:\\Users\\skili\\Documents\\GitHub\\MS-Calculator-gui\\icon.png'))
    
    # root.geometry()

    #making the display
    global entry1,entry2
    entry1=Label(root,bg="#1F1F1F",fg="#FFFFFF")
    entry1.grid(row=0,column=0,columnspan=12,sticky=E,padx=3,pady=3)
    entry2=Label(root,font=('Helvetica',35,'bold'),bg="#1F1F1F",fg="#FFFFFF")
    entry2.grid(row=1,column=0,columnspan=12,rowspan=2,sticky=E,padx=3,pady=10)
    entry2.config(text="0")

    #bd=0 to remove border
    #adding the memory buttons
    mcb=Button(root,text="MC",padx=12,pady=5,bg="#1F1F1F",fg="#FFFFFF",bd=0,command=memclear)
    mrb=Button(root,text="MR",padx=12,pady=5,bg="#1F1F1F",fg="#FFFFFF",bd=0,command=memrecall)
    mpb=Button(root,text="M+",padx=12,pady=5,bg="#1F1F1F",fg="#FFFFFF",bd=0,command=memadd)
    mmb=Button(root,text="M-",padx=12,pady=5,bg="#1F1F1F",fg="#FFFFFF",bd=0,command=memsub)
    msb=Button(root,text="MS",padx=12,pady=5,bg="#1F1F1F",fg="#FFFFFF",bd=0,command=memsave)
    mlb=Button(root,text="M^",padx=12,pady=5,bg="#1F1F1F",fg="#FFFFFF",bd=0)

    mcb.grid(row=3,column=0,columnspan=2)
    mrb.grid(row=3,column=2,columnspan=2)
    mpb.grid(row=3,column=4,columnspan=2)
    mmb.grid(row=3,column=6,columnspan=2)
    msb.grid(row=3,column=8,columnspan=2)
    mlb.grid(row=3,column=10,columnspan=2)

    #row1 of main button
    modb=Button(root,text="%",bg="#131313",fg="#FFFFFF",bd=0)
    modb.grid(row=4,column=0,rowspan=2,columnspan=3,ipadx=30,ipady=14,padx=1,pady=1)
    ceb=Button(root,text="CE",bg="#131313",fg="#FFFFFF",bd=0,command=clear2)
    ceb.grid(row=4,column=3,rowspan=2,columnspan=3,ipadx=28,ipady=14,padx=1,pady=1)
    cb=Button(root,text="C",bg="#131313",fg="#FFFFFF",bd=0,command=clear12)
    cb.grid(row=4,column=6,rowspan=2,columnspan=3,ipadx=30,ipady=14,padx=1,pady=1)
    bb=Button(root,text="<-",bg="#131313",fg="#FFFFFF",bd=0,command=backspace)
    bb.grid(row=4,column=9,rowspan=2,columnspan=3,ipadx=27,ipady=14,padx=1,pady=1)


    #row2 of main button
    rb=Button(root,text="1/x",bg="#131313",fg="#FFFFFF",bd=0)
    rb.grid(row=6,column=0,rowspan=2,columnspan=3,ipadx=26,ipady=14,padx=1,pady=1)
    sb=Button(root,text="x²",bg="#131313",fg="#FFFFFF",bd=0)
    sb.grid(row=6,column=3,rowspan=2,columnspan=3,ipadx=29,ipady=14,padx=1,pady=1)
    rootb=Button(root,text="√x",bg="#131313",fg="#FFFFFF",bd=0)
    rootb.grid(row=6,column=6,rowspan=2,columnspan=3,ipadx=28,ipady=14,padx=1,pady=1)
    divb=Button(root,text="÷",bg="#131313",fg="#FFFFFF",bd=0,command=div)
    divb.grid(row=6,column=9,rowspan=2,columnspan=3,ipadx=29,ipady=14,padx=1,pady=1)


    #row3 of main button
    b7=Button(root,text="7",bg="#060606",fg="#FFFFFF",font=('bold'),bd=0,command=lambda : inputentry2("7"))
    b7.grid(row=8,column=0,rowspan=2,columnspan=3,ipadx=26,ipady=8,padx=1,pady=1)
    b8=Button(root,text="8",bg="#060606",fg="#FFFFFF",font=('bold'),bd=0,command=lambda : inputentry2("8"))
    b8.grid(row=8,column=3,rowspan=2,columnspan=3,ipadx=26,ipady=8,padx=1,pady=1)
    b9=Button(root,text="9",bg="#060606",fg="#FFFFFF",font=('bold'),bd=0,command=lambda : inputentry2("9"))
    b9.grid(row=8,column=6,rowspan=2,columnspan=3,ipadx=26,ipady=8,padx=1,pady=1)
    mulb=Button(root,text="X",bg="#131313",fg="#FFFFFF",font=('bold'),bd=0,command=mul)
    mulb.grid(row=8,column=9,rowspan=2,columnspan=3,ipadx=26,ipady=8,padx=1,pady=1)


    #row4 of main button
    b4=Button(root,text="4",bg="#060606",fg="#FFFFFF",font=('bold'),bd=0,command=lambda : inputentry2("4"))
    b4.grid(row=10,column=0,rowspan=2,columnspan=3,ipadx=26,ipady=8,padx=1,pady=1)
    b5=Button(root,text="5",bg="#060606",fg="#FFFFFF",font=('bold'),bd=0,command=lambda : inputentry2("5"))
    b5.grid(row=10,column=3,rowspan=2,columnspan=3,ipadx=26,ipady=8,padx=1,pady=1)
    b6=Button(root,text="6",bg="#060606",fg="#FFFFFF",font=('bold'),bd=0,command=lambda : inputentry2("6"))
    b6.grid(row=10,column=6,rowspan=2,columnspan=3,ipadx=26,ipady=8,padx=1,pady=1)
    subb=Button(root,text="-",bg="#131313",fg="#FFFFFF",font=('bold'),bd=0,command=sub)
    subb.grid(row=10,column=9,rowspan=2,columnspan=3,ipadx=28,ipady=8,padx=1,pady=1)


    #row5 of main button
    b1=Button(root,text="1",bg="#060606",fg="#FFFFFF",font=('bold'),bd=0,command=lambda : inputentry2("1"))
    b1.grid(row=12,column=0,rowspan=2,columnspan=3,ipadx=26,ipady=8,padx=1,pady=1)
    b2=Button(root,text="2",bg="#060606",fg="#FFFFFF",font=('bold'),bd=0,command=lambda : inputentry2("2"))
    b2.grid(row=12,column=3,rowspan=2,columnspan=3,ipadx=26,ipady=8,padx=1,pady=1)
    b3=Button(root,text="3",bg="#060606",fg="#FFFFFF",font=('bold'),bd=0,command=lambda : inputentry2("3"))
    b3.grid(row=12,column=6,rowspan=2,columnspan=3,ipadx=26,ipady=8,padx=1,pady=1)
    addb=Button(root,text="+",bg="#131313",fg="#FFFFFF",font=('bold'),bd=0,command=add)
    addb.grid(row=12,column=9,rowspan=2,columnspan=3,ipadx=26,ipady=8,padx=1,pady=1)


    #row6 of main button
    negb=Button(root,text="+/-",bg="#060606",fg="#FFFFFF",font=('bold'),bd=0,command=negate)
    negb.grid(row=14,column=0,rowspan=2,columnspan=3,padx=1,pady=1,ipadx=20,ipady=8)
    b0=Button(root,text="0",bg="#060606",fg="#FFFFFF",font=('bold'),bd=0,command=lambda : inputentry2("0"))
    b0.grid(row=14,column=3,rowspan=2,columnspan=3,ipadx=26,ipady=8,padx=1,pady=1)
    pointb=Button(root,text=".",bg="#060606",fg="#FFFFFF",font=('bold'),bd=0,command=lambda : inputentry2("."))
    pointb.grid(row=14,column=6,rowspan=2,columnspan=3,ipadx=28,ipady=8,padx=1,pady=1)
    equalb=Button(root,text="=",bg="#2F3031",fg="#FFFFFF",font=('bold'),bd=0,command=equal)
    equalb.grid(row=14,column=9,rowspan=2,columnspan=3,ipadx=26,ipady=8,padx=1,pady=1)


    root.mainloop()

if __name__ == "__main__":
    startCalc()