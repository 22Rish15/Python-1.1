from tkinter import *
import os

def res():
    os.system("shutdown /r /t 1")
    
def res_time():
    os.system("shutdown /r /t 20")

def log():
    os.system("shutdown -1")
    
def shut():
    os.system("shutdown /s /t 1")
 
st = Tk()
st.title("ShutDown App")
st.geometry("300x210")
st.config(bg = "Black")

r_button = Button(st,text = "Restart", font=("Times New Roman",20,"bold"),
                  relief=RAISED,cursor="plus", command=res)
r_button.place(x = 80, y = 10, height = 40, width = 140)

rt_button = Button(st,text = "Restart Time", font=("Times New Roman",15,"bold"),
                   relief=RAISED,cursor="plus", command=res_time)
rt_button.place(x = 80, y = 60, height = 40, width = 140)

lg_button = Button(st,text = "Log Out", font=("Times New Roman",15,"bold"),
                   relief=RAISED,cursor="plus", command=log)
lg_button.place(x = 80, y = 110, height = 40, width = 140)

st_button = Button(st,text = "Shut Down", font=("Times New Roman",15,"bold"),
                   relief=RAISED,cursor="plus", command=shut)
st_button.place(x = 80, y = 160, height = 40, width = 140)

st.mainloop()