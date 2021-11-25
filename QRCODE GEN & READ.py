import qrcode
import random
import cv2

qr=qrcode.make("file:///G:/ebill/customerName.html")

qr.save("eb_bill.png")



qr=cv2.imread("G:\\python\\eb_bill.png")
qrcode_detect=cv2.QRCodeDetector()
decodedText,value,some = qrcode_detect.detectAndDecode(qr)

print(decodedText)
