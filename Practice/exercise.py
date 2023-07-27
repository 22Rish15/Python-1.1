import time

timestamp=time.strftime("%Y-%m-%d \t%H:%M:%S")
print(timestamp)

hour=int(time.strftime("%H"))
print(hour)

if (1<=hour<12):
    print("Good Morning!")

elif(12<=hour<=16):
    print("Good Evening!")
    
else:
    print("Good Night!")