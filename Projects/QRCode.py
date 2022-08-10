import PIL.Image
import qrcode
img = qrcode.make("https://www.linkedin.com/in/rishi-khandelwal-848546210/")
img.save("LinkedIn.jpg")

img = qrcode.make("+91 9634036365")
img.save("Phone_No.jpg")