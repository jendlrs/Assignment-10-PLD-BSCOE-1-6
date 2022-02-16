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

import webbrowser
import cv2

#Opening the webcam by using opencv

webcam = cv2.VideoCapture(0)
detector= cv2.QRCodeDetector()

while True:
    _, img = webcam.read()
    data, _, _ = detector.detectAndDecode (img) #Condition to read the qr code
    if data:
        data = 'QRcode.png'
        break

    cv2.imshow ("QR CODE SCANNER", img)
    if cv2.waitKey (1) == ord("q"):
        break
    webcam.release

cv2.destroyAllWindows()
b = webbrowser.open(str(data))

#call the function