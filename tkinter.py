from Tkinter import *
from base64 import *



root=Tk()
root.title('base64 mini')
frame=LabelFrame(root,text="it is base64 window frame",padx=70,pady=70,bg="darkgoldenrod")
frame.pack(padx=5,pady=5)

e=Entry(frame,width=40,bg="blue",fg="white")
e.grid(row=0,column=0)
e1=Entry(frame,width=40,bg="blue",fg="white")
e1.grid(row=1,column=0)
def ecode():
	a=e.get().encode()
	result=b64encode(a)

	mylabel=Label(frame,bg="red",text="enoded value is:==>>>  "+result)
	mylabel.grid(row=2,column=0)

def dcode():
	a=e1.get().encode()
	result=b64decode(a)

	lab1=Label(frame,bg="green",fg="white",text="decoded value is:===>>>    "+result)
	lab1.grid(row=3,column=0)

def clear():
	e.delete(0,END)

def clearall():
	e1.delete(0,END)

def helpp():
	l=Label(frame,text="thats the base64 decode & encode window")
	l.grid(row=2,column=1)
	

b=Button(frame,text="help?",command=helpp)
b.grid(row=4,column=0)

but1=Button(frame,text="encode",bg="black",fg="white",command=ecode)
but1.grid(row=0,column=1)
but2=Button(frame,text="decode",bg="black",fg="white",command=dcode)
but2.grid(row=1,column=1)

but3=Button(frame,text="clear",bg="black",fg="white",command=clear)
but3.grid(row=0,column=2)
but4=Button(frame,text="clear",bg="black",fg="white",command=clearall)
but4.grid(row=1,column=2)
