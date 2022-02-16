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
from pyzbar import pyzbar 

#Opening the webcam by using opencv

def detect():
    webcam = cv2.VideoCapture(0)
    _, img = webcam.read()

    while True:
        _, img = webcam.read()
        img = decode (cv2.resize (img, None, fx =1.0, fy=1.0, interpolation = cv2.INTER_AREA))
        cv2.imshow ("QR CODE SCANNER", img)
        if cv2.waitKey (1) ==ord ("p"):
            break

    webcam.release
    cv2.destroyAllWindows()

def decode (img):
    Qr_code = pyzbar.decode(img)
    for info in Qr_code: #This loop is for decoding the qr code
        #utf-8 or Unicode Transformation Format -8 is used for encoding the info from qr code into another file
        Qr_data = info.data.decode ("utf-8")
        with open ("qr_result.txt", "w") as textfile:  #It will automatically open a text file
            textfile.write (Qr_data)                   #Writing the data from qr code to the new text file
    return img

#call the function
detect()