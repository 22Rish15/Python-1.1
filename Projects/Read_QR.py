import cv2

img = cv2.imread("Phone_No.jpg")   #QR name
det = cv2.QRCodeDetector()
val, pts, st_code = det.detectAndDecode(img)
print(val) 