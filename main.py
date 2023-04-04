from tkinter import *
def click1() :
  root['bg'] = 'green'
def click2() :
  root['bg'] = 'yellow'
def click3() :
  root['bg'] = 'red'
root = Tk()
button=Button(text='Червоний', command = click1)
button.pack(pady=10)
button=Button(text='Жовтий', command = click2)
button.pack(pady=10)
button=Button(text='Зелений', command = click3) 
button.pack(pady=10)
