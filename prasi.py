from tkMessageBox import *
from Tkinter import *
import math
import sqlite3

root=Tk()
first_time=1
root.configure(bg='light blue')
root.title('fixture generator')
Label(root,text="Fixture Generator",font=('Courier',35),relief='ridge').grid(row=0,column=0)
Label(root,text="choose the sport for which you want the fixtures",font=('Courier',35),relief='ridge').grid(row=1,column=0)
v1=IntVar()
r1=Radiobutton(root,text='Cricket',font=('Courier',15),variable=v1,value=1,bg='light blue').grid(row=2,column=0)
r2=Radiobutton(root,text='Badminton',font=('Courier',15),variable=v1,value=2,bg='light blue').grid(row=3,column=0)
r3=Radiobutton(root,text='Table Tennis',font=('Courier',15),variable=v1,value=3,bg='light blue').grid(row=4,column=0)
r4=Radiobutton(root,text='Football',variable=v1,font=('Courier',15),value=4,bg='light blue').grid(row=5,column=0)
r5=Radiobutton(root,text='Volley Ball',variable=v1,font=('Courier',15),value=5,bg='light blue').grid(row=6,column=0)
global N
global m
global non_bye
global team_bye
non_bye=[]
team_bye=[]
def stop(j):
        display=Tk()
        display.configure(bg='light blue')
        Label(display,text="Congratulations",font=('Courier',40),bg='light blue').grid(row=0,column=0)
        Label(display,text="The winner is Team ",font=('Courier',40),bg='light blue').grid(row=1,column=0)
        Label(display,text=j[0],font=('Courier',40),bg='light blue').grid(row=1,column=1)
        
def play(final):
        ok=Tk()
        ok.configure(bg='light blue')
        final2=[]
        if len(final)==2:
                print final
        final_entry=[]
        i=0
        while i<len(final):   
                Label(ok,text=str(final[i])+ "vs" + str(final[i+1]),font=('Courier',15),bg='light blue').grid(row=i+1,column=0)
                lm=Entry(ok)
                lm.grid(row=i+1,column=1)
                i=i+2
                final_entry.append(lm)
        def pre():
                final=[]
                for i in range(len(final_entry)):
                        final.append(final_entry[i].get())
                Label(ok,text=final,font=('Courier',15),bg='light blue').grid()
        
        def proceed():
                ok.destroy()
                if len(final)==2:
                        stop(final)
                else:
                        play(final) 
        Button(ok,text="Proceed",command=lambda:proceed()).grid(row=i+3,column=1)
        Button(ok,text="Winner",command=lambda:pre()).grid(row=i+3,column=0)
        ok.mainloop()
def second(x):
        x.destroy()
        new=Tk()
        new.configure(bg='light blue')
        again,win=[],[]
        Label(new,text="First Round:",font=('Courier',15),bg='light blue').grid(row=0,column=0)
        bb=0
        for i in range(len(non_bye)/2):
            Label(new,text=str(non_bye[bb])+" vs "+str(non_bye[bb+1]),font=('Courier',15),bg='light blue').grid(row=i+1,column=0)
            k=Entry(new)
            k.grid(row=i+1,column=1)   
            bb=bb+2
            again.append(k)
        def blow():
            bb=0
            for i in range(len(again)):
                win.append(again[i].get())
            Label(new,text=win,font=('Courier',15),bg='light blue').grid(row=i+5,column=0)
        Button(new,text='winners',command=blow).grid(row=i+6,column=0)    
        final=[]
        final_entry=[]
        def boom():
            new.destroy()
            new1=Tk()
            new1.configure(bg='light blue')
            if len(win)>len(team_bye):
                i=0
                for i in range(len(team_bye)):
                    Label(new1,text=str(win[i])+ " vs " + str(team_bye[i]),font=('Courier',15),bg='light blue').grid(row=i+1,column=0)
                    lm=Entry(new1)
                    lm.grid(row=i+1,column=1)
                    i=i+1
                    final_entry.append(lm)
                while i<len(win):    
                    Label(new1,text=str(win[i])+ " vs " + str(win[i+1]),font=('Courier',15),bg='light blue').grid(row=i+1,column=0)
                    lm=Entry(new1)
                    lm.grid(row=i+1,column=1)
                    i=i+2
                    final_entry.append(lm)
            else:
                i=0    
                for i in range(len(win)):
                    Label(new1,text=str(win[i])+ " vs " + str(team_bye[i]),font=('Courier',15),bg='light blue').grid(row=i+1,column=0)
                    lm=Entry(new1)
                    lm.grid(row=i+1,column=1)
                    i=i+1
                    final_entry.append(lm)
                while i<len(team_bye):
                    Label(new1,text=str(team_bye[i])+ " vs " + str(team_bye[i+1]),font=('Courier',15),bg='light blue').grid(row=i+1,column=0)
                    lm=Entry(new1)
                    lm.grid(row=i+1,column=1)
                    i=i+2
                    final_entry.append(lm)
            def finalround():
                for i in range(len(final_entry)):
                    final.append(final_entry[i].get())    
                Label(new1,text=final,font=('Courier',15),bg='light blue').grid()
            Button(new1,text="Winner",command=finalround).grid(row=i+2,column=0)
            Button(new1,text="Proceed",command=lambda:play(final)).grid(row=i+2,column=1)
            new1.mainloop()
        Button(new,text='round 2',command=boom).grid(row=i+6,column=1)
        new.mainloop()
                
def Badminton():
        root.destroy()
        root2=Tk()
        root2.title('fixture generator')
        root2.configure(bg='light blue')
##        photo=PhotoImage(file="sports.gif")
##        w=Label(root,image=photo)
##        w.place(x=0,y=0,relwidth=1,relheight=1)
##        w.photo=photo
##        w.grid()
        Label(root2,text='Enter the no. teams',font=('Courier',25),bg='light blue').grid(row=0,column=1)
        e=Entry(root2)
        e.grid(row=0,column=2)
        def proceed():
                root3=Tk()
                root3.title('fixture generator')
                root3.configure(bg='light blue')
                m=int(e.get())
                N=m-1
                a=[]
                
                for i in range(1,m+1):
                        Label(root3,text='Enter the Team name',font=('Courier',15),bg='light blue').grid(row=i,column=0)
                        f=Entry(root3)
                        f.grid(row=i,column=1)
                        a.append(f)
                def fun():
                        x=Tk()
                        x.title('fixture generator')
                        x.configure(bg='light blue')
                        count=0
                        if m%2==0:
                                Label(x,text='Upperhalf',font=('Courier',15),bg='light blue').grid(row=0,column=0)
                                for i in range(0,m/2):
                                        Label(x,text=str(a[i].get()),font=('Courier',15),bg='light blue').grid(row=i+1,column=0)
                                Label(x,text='lowerhalf',font=('Courier',15),bg='light blue').grid(row=(m/2)+1,column=0)
                                for i in range(0,(m/2)):
                                        Label(x,text=str(a[i+(m/2)].get()),font=('Courier',15),bg='light blue').grid(row=i+(m/2)+2,column=0)

                        else:
                                Label(x,text='Upperhalf',font=('Courier',25),bg='light blue').grid(row=0,column=0)
                                for i in range(0,((m+1)/2)):
                                        a[i].get()
                                        Label(x,text=str(a[i].get()),font=('Courier',15),bg='light blue').grid(row=i+1,column=0)
                                Label(x,text='Lowerhalf',font=('Courier',25),bg='light blue').grid(row=((m+1)/2)+1,column=0)
                                for i in range(0,((m-1)/2)):
                                        Label(x,text=str(a[i+(m/2)+1].get()),font=('Courier',15),bg='light blue').grid(row=i+(m/2)+3,column=0)
                        
                        def power_of_two(m):
                                b = 2
                                change = 0
                                power = 0
                                for i in range(m+1):
                                        number = b ** change
                                        change = i
                                        if number >= m:
                                                power = number    
                                                return power
                        #-----------------------------------------
                        g=power_of_two(m)
                        kk=g-m
                        Label(x,text='No.of Byes will be : '+str(kk),font=('Courier',15),bg='light blue').grid(row=m+5,column=0)
                        Label(x,text='No.of matches will be: '+str(N),font=('Courier',15),bg='light blue').grid(row=m+6,column=0)
                        global team_bye
                        global non_bye
                        up,down=0,0
                        r=m
                        for i in range(kk):
                            if i==3 and m%2==0:
                                team_bye.append(a[(m/2)-1].get())
                            elif i==2 and m%2==0:
                                team_bye.append(a[(m/2)].get())
                            elif i==2 and m%2==1:
                                team_bye.append(a[((m+1)/2)].get())
                            elif i==3 and m%2==1:
                                team_bye.append(a[((m+1)/2)-1].get())
                            else:
                                if i%2==1:
                                    if up==0:
                                        team_bye.append(a[1-1].get())
                                        up=up+1
                                    else:
                                        team_bye.append(a[up-1].get())
                                    up=up+1
                                else:
                                    team_bye.append(a[r-down-1].get())
                                    down=down+1
                        
                        for i in a:
                                if i.get() not in team_bye:
                                        non_bye.append(i.get())
                        Label(x,text='Byes are given to these teams:-',font=('Courier',15),bg='light blue').grid(row=m+7,column=0)
                        Label(x,text=team_bye,font=('Courier',15),bg='light blue').grid(row=m+8,column=0)
                        Button(x,text="proceed",command=lambda:second(x)).grid(row=m+9,column=1)
                        x.mainloop()
                        
                Button(root3,text="Get",command=fun).grid()
                root3.mainloop()
        Button(root2,text="Proceed",command=proceed).grid(row=3,column=2)
        root2.mainloop()
def choice():
    if(v1.get()==1):
        Badminton()
        #Label(root,text='cricket').grid(row=7,column=1)
    if(v1.get()==2):
        Badminton()
        #Label(root,text='Badminton').grid(row=8,column=1)
    if(v1.get()==3):
        Badminton()
        #Label(root,text='Table tennis').grid(row=9,column=1)
    if(v1.get()==4):
        Badminton()
        #Label(root,text='cricket').grid(row=10,column=1)
    if(v1.get()==5):
        Badminton()
        #Label(root,text='volley ball').grid(row=11,column=1)
Button(root,text='Enter',command=Badminton).grid(row=12,column=0)
root.mainloop()
