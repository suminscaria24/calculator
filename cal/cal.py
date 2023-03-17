from tkinter import *
exp=""
def press(num):
	global exp
	exp=exp+str(num)
	equation.set(exp)
def equalpress():
	try:
		global exp
		total=str(eval(exp))
		equation.set(total)
		exp=""
	except:
		equation.set(" error ")
		exp=""
def clear():
	global exp
	exp=""
	equation.set("")

mgui=Tk()
mgui.geometry("270x150")
mgui.config(bg="pink")
mgui.title("SIMPLE CALCULATOR")
equation=StringVar()
exp_field=Entry(mgui,textvariable=equation)
exp_field.grid(columnspan=4,ipadx=70)
b1=Button(mgui,text="1",command=lambda: press(1),height=1,width=7,bg="pink",fg="dark green")
b1.grid(row=2,column=0)
b2=Button(mgui,text="2",command=lambda: press(2),height=1,width=7,bg="pink",fg="dark green")
b2.grid(row=2,column=1)
b3=Button(mgui,text="3",command=lambda: press(3),height=1,width=7,bg="pink",fg="dark green")
b3.grid(row=2,column=2)
b4=Button(mgui,text="4",command=lambda: press(4),height=1,width=7,bg="pink",fg="dark green")
b4.grid(row=2,column=3)
b5=Button(mgui,text="5",command=lambda: press(5),height=1,width=7,bg="pink",fg="dark green")
b5.grid(row=3,column=0)
b6=Button(mgui,text="6",command=lambda: press(6),height=1,width=7,bg="pink",fg="dark green")
b6.grid(row=3,column=1)
b7=Button(mgui,text="7",command=lambda: press(7),height=1,width=7,bg="pink",fg="dark green")
b7.grid(row=3,column=2)
b8=Button(mgui,text="8",command=lambda: press(8),height=1,width=7,bg="pink",fg="dark green")
b8.grid(row=3,column=3)
b9=Button(mgui,text="9",command=lambda: press(9),height=1,width=7,bg="pink",fg="dark green")
b9.grid(row=4,column=0)
b0=Button(mgui,text="0",command=lambda: press(0),height=1,width=7,bg="pink",fg="dark green")
b0.grid(row=4,column=1)
plus=Button(mgui,text="+",command=lambda: press("+"),height=1,width=7,bg="pink",fg="dark green")
plus.grid(row=4,column=2)
minus=Button(mgui,text="-",command=lambda: press("-"),height=1,width=7,bg="pink",fg="dark green")
minus.grid(row=4,column=3)
mul=Button(mgui,text="*",command=lambda: press("*"),height=1,width=7,bg="pink",fg="dark green")
mul.grid(row=5,column=0)
divi=Button(mgui,text="/",command=lambda: press("/"),height=1,width=7,bg="pink",fg="dark green")
divi.grid(row=5,column=1)
eql=Button(mgui,text="=",command=equalpress,height=1,width=7,bg="pink",fg="dark green")
eql.grid(row=5,column=2)
clear=Button(mgui,text="CLR",command=clear,height=1,width=7,bg="pink",fg="dark green")
clear.grid(row=5,column=3)
deci=Button(mgui,text=".",command=lambda: press("."),height=1,width=7,bg="pink",fg="dark green")
deci.grid(row=6,column=0)
mgui.mainloop()