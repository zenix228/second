import random
import tkinter as tk
from tkinter import messagebox



symbols = '[]{}()*;!@#$%^&*()|\/<>?/,+=_-0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

lenght = 8

def pas():
	entry_1.delete(0,tk.END)
	r = entry_1.insert(0,random.sample(symbols,lenght))
	print(r)

win = tk.Tk()
win.title('моя первая работа')
win['bg'] = '#03172F'
win.geometry('400x400+550+200')
win.resizable(True, True)
label_1 = tk.Label(text='your pass',font=('Cambria','15'),background='white')
label_1.place(x=15,y=50)
entry_1 = tk.Entry(font=('Cambria','12'),selectbackground='#800080')
entry_1.place(x=110,y=50)
button_1 = tk.Button(text='password',font=('Cambria','13'),command=pas)
button_1.place(x=110,y=80)
