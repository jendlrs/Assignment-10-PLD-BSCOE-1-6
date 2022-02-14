# Assignment 10

# Contact Tracing App
# 	- Create a python program that will read QRCode using your webcam
# 	- You may use any online QRCode generator to create QRCode
# 	- All personal data are in QRCode 
# 	- You may decide which personal data to include
# 	- All data read from QRCode should be stored in a text file including the date and time it was read

# Note: 
# 	- Search how to generate QRCode
# 	- Search how to read QRCode using webcam
# 	- Search how to create and write to text file
# 	- Your source code should be in github before Feb 19
# 	- Create a demo of your program (1-2 min) and send it directly to my messenger.

import cv2
import qrcode

#I decided to generate my own qrcode through python.
def generate ():
    with open('personal_data.txt') as f:
        personal_data= f.read()
    #personal_data = open('personal_data.txt')
    QR_code = qrcode.make(personal_data)
    QR_code.save('QRcode.png')

#Opening the webcam by using opencv
webcam = cv2.VideoCapture(0)
detector= cv2.QRCodeDetector()

while True:
    _, img = webcam.read()
    data = detector.detectAndDecode (img) #It is where I will put the condition to read the qr code

    cv2.imshow ("QR CODE SCANNER", img)
    if cv2.waitKey (1) == ord("q"):
       break

cv2.destroyAllWindows()

#call the function
generate()
