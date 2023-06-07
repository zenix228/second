import tkinter
from tkinter import messagebox
window = tkinter.Tk()
window.title('x and o')
window.geometry('350x400+450+200')
window.configure(bg='#C0C0C0')
window.resizable(False,False)
def xando():
	if r_var.get() == True:
		button_1.config(text='X')
	elif r_var.get() == False:
		button_1.config(text='O')
def xando2():
	if r_var.get() == True:
		button_2.config(text='X')
	elif r_var.get() == False:
		button_2.config(text='O')
def xando3():
	if r_var.get() == True:
		button_3.config(text='X')
	elif r_var.get() == False:
		button_3.config(text='O')
def xando4():
	if r_var.get() == True:
		button_4.config(text='X')
	elif r_var.get() == False:
		button_4.config(text='O')
def xando5():
	if r_var.get() == True:
		button_5.config(text='X')
	elif r_var.get() == False:
		button_5.config(text='O')
def xando6():
	if r_var.get() == True:
		button_6.config(text='X')
	elif r_var.get() == False:
		button_6.config(text='O')
def xando7():
	if r_var.get() == True:
		button_7.config(text='X')
	elif r_var.get() == False:
		button_7.config(text='O')
def xando8():

	if r_var.get() == True:
		button_8.config(text='X')
	elif r_var.get() == False:
		button_8.config(text='O')
def xando9():

	if r_var.get() == True:
		button_9.config(text='X')
	elif r_var.get() == False:
		button_9.config(text='O')
def winner():
	if button_1['text'] == button_2['text'] == button_3['text']:
		label_winner.config(text=button_2['text'])
	if button_4['text'] == button_5['text'] == button_6['text']:
		label_winner.config(text=button_5['text'])
	if button_7['text'] == button_8['text'] == button_9['text']:
		label_winner.config(text=button_8['text'])
	if button_1['text'] == button_4['text'] == button_7['text']:
		label_winner.config(text=button_4['text'])
	if button_2['text'] == button_5['text'] == button_8['text']:
		label_winner.config(text=button_5['text'])
	if button_3['text'] == button_6['text'] == button_9['text']:
		label_winner.config(text=button_3['text'])
	if button_1['text'] == button_5['text'] == button_9['text']:
		label_winner.config(text=button_5['text'])
	if button_3['text'] == button_5['text'] == button_7['text']:
		label_winner.config(text=button_5['text'])
	else:
		messagebox.showinfo(' ', message='вы ввели все не правильно, попробуйте еще раз')
		quit()
r_var = tkinter.BooleanVar()
r_var.set(0)
button = tkinter.Button()
label_winner = tkinter.Label(
	text='winner:',
	font=('Cambria', '16'),
	width=9,
	bg='#FFFFFF',
	fg='black')
label_winner.place(x=80,y=30)
radio_x = tkinter.Radiobutton(
	text='X',
	bg='#C0C0C0',
	font=('Roboto', 11,),
	variable=r_var,
	value=1
	)
radio_x.place(x=10,y=0)
radio_o = tkinter.Radiobutton(
	text='O',
	bg='#C0C0C0',
	font=('Roboto', 11,),
	variable=r_var,
	value=0)
radio_o.place(x=50,y=0)
button_who_win = tkinter.Button(
	text='Who win?',
	font=('Cambria','12'),
	width=9,
	bg='#FFFFFF',
	fg='black',
	command=winner)
button_who_win.place(x=200,y=30)
button_1 = tkinter.Button(command=xando)
button_1.place(x=50,y=90,height=80,width=80)
button_2 = tkinter.Button(command=xando2)
button_2.place(x=135,y=90,height=80,width=80)
button_3 = tkinter.Button(command=xando3)
button_3.place(x=220,y=90,width=80,height=80)
button_4 = tkinter.Button(command=xando4)
button_4.place(x=50,y=180,height=80,width=80)
button_5 = tkinter.Button(command=xando5)
button_5.place(x=135,y=180,height=80,width=80)
button_6 = tkinter.Button(command=xando6)
button_6.place(x=220,y=180,width=80,height=80)
button_7 = tkinter.Button(command=xando7)
button_7.place(x=50,y=270,height=80,width=80)
button_8 = tkinter.Button(command=xando8)
button_8.place(x=135,y=270,height=80,width=80)
button_9 = tkinter.Button(command=xando9)
button_9.place(x=220,y=270,width=80,height=80)
window.mainloop()