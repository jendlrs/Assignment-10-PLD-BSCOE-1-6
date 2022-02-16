#I decided to generate my own qrcode through python.
import qrcode

def generate ():
    with open('personal_data.txt') as f:
        personal_data = f.read()
        QR_code = qrcode.QRCode(
        version =1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size =10,
        border =2,
    )
    QR_code.add_data(personal_data)
    QR_code.make(fit=True)
    QR_code_generated = QR_code.make_image(fill_color = 'black', back_color = 'white')
    QR_code_generated.save('QRcode.png')

generate()