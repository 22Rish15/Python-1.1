message = "This is a fong string"   #want kto replace f with l
msg = message.index("f")
print(msg)
new_msg= message[:10] + "l" + message[11:]
print(new_msg)