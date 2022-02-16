#I decided to generate my own qrcode through python.
import qrcode
def generate ():
    with open('personal_data.txt') as f:
        personal_data= f.read()
    QR_code = qrcode.make(personal_data)
    QR_code.save('QRcode.png')

generate()