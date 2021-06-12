from tkinter import *

root=Tk()
root.geometry('600x900')
root.maxsize(650,850)
root.config(bg='black')

def click(event):
    global scvalue
    text=event.widget.cget('text')

    if text=='=':
        if scvalue.get().isdigit():
            value=int(scvalue.get())

        else:
            try:
              value=eval(var.get())
            except Exception as ex:
                print(ex)
                value='Error'
        scvalue.set(value)
        var.update()

    elif text=='C':
        scvalue.set('')
        var.update()
    else:
        scvalue.set(scvalue.get()+text)
        var.update()




scvalue=StringVar()
scvalue.set('')
var=Entry(root,textvariable=scvalue,font ='lucida 40 bold',relief=SUNKEN)
var.pack(fill=X,padx=10,pady=10,ipadx=9)

f=Frame(root,bg='gray')
b=Button(f,text='9',padx=20,pady=15,font='Aialblack 30 bold')
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=23,pady=20)
b=Button(f,text='8',padx=20,pady=15,font='Aialblack 30 bold')
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=23,pady=20)
b=Button(f,text='7',padx=20,pady=15,font='Aialblack 30 bold')
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=23,pady=20)
b=Button(f,text='C',padx=20,pady=15,font='Aialblack 30 bold')
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=23,pady=20)
f.pack()


f=Frame(root,bg='gray')
b=Button(f,text='6',padx=20,pady=15,font='Aialblack 30 bold')
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=23,pady=20)
b=Button(f,text='5',padx=20,pady=15,font='Aialblack 30 bold')
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=23,pady=20)
b=Button(f,text='4',padx=20,pady=15,font='Aialblack 30 bold')
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=23,pady=20)
b=Button(f,text='+',padx=23,pady=15,font='Aialblack 30 bold')
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=23,pady=20)
f.pack()

f=Frame(root,bg='gray')
b=Button(f,text='3',padx=20,pady=15,font='Aialblack 30 bold')
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=23,pady=20)
b=Button(f,text='2',padx=20,pady=15,font='Aialblack 30 bold')
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=23,pady=20)
b=Button(f,text='1',padx=20,pady=15,font='Aialblack 30 bold')
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=23,pady=20)
b=Button(f,text='-',padx=28,pady=15,font='Aialblack 30 bold')
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=23,pady=20)
f.pack()

f=Frame(root,bg='gray')
b=Button(f,text='0',padx=20,pady=15,font='Aialblack 30 bold')
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=23,pady=20)
b=Button(f,text='*',padx=21,pady=15,font='Aialblack 30 bold')
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=23,pady=20)
b=Button(f,text='/',padx=25,pady=15,font='Aialblack 30 bold')
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=23,pady=20)
b=Button(f,text='%',padx=20,pady=15,font='Aialblack 30 bold')
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=23,pady=20)
f.pack()


f=Frame(root,bg='gray')
b=Button(f,text='=',padx=236,pady=15,font='Aialblack 30 bold')
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=23,pady=20,fill=X)

f.pack()



root.mainloop()