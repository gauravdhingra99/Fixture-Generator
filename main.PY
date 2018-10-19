from Tkinter import *
import subprocess
def fun1():
    subprocess.call("python prasi.py")
front_page=Tk()
front_page.geometry('1024x768')
front_page.configure(bg="light blue")
front_page.title('fixture generator')
icon=PhotoImage(file='new.gif')
Label(front_page,image=icon).place(relx=-0.0001,rely=0.000000111)
Label(front_page,text="FIXTURES GENERATOR",font=('Courier',25),bg="white").grid(row=10,column=0)
l1=Label(front_page,text=" ",bg='white')
l1.after(1000,fun1)
front_page.mainloop()

