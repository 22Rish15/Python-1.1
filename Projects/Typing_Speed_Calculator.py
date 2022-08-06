from time import *
import random as rm

def error(para,user):
    error = 0
    for i in range(len(para)):
        try:
            if para[0] != user[0]:
                error = error + 1
        except:
            error = error + 1
    return error

def tim(t1,t2,us):
    time = t2 - t1
    tps = round(time,2)
    speed = len(us)/tps
    return round(speed)

test = ["Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc)." ,
        "Python has a simple syntax similar to the English language." ,
        "Python has syntax that allows developers to write programs with fewer lines than some other programming languages.",
        "Python runs on an interpreter system, meaning that code can be executed as soon as it is written.",
        "This means that prototyping can be very quick.",
        "Python can be treated in a procedural way, an object-oriented way or a functional way."]

test1 = rm.choices(test)
print("             ***** Typing Speed Calculator *****")
print(test1)
print()

time_1 = time()
user_1 = input("Start Typing : ")
time_2 = time()
print("Speed :",tim(time_1,time_2,user_1),"word/sec")
print("Error :",error(test1,user_1))