# intall all the libraries needed
# create a function that collects a text and converts it to a QR code
# save the QR code as an image
# run the function

import qrcode  # https://pypi.org/project/qrcode/


def qrcode_generator(text, arq_name):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        # ERROR_CORRECT_L: About 7% or less errors can be corrected.
        # ERROR_CORRECT_M (default): About 15% or less errors can be corrected.
        # ERROR_CORRECT_Q: About 25% or less errors can be corrected.
        # ERROR_CORRECT_H: About 30% or less errors can be corrected.
        box_size=10,  # the size of the qr code in pixels
        border=4,  # the background border outside the qr code
    )
    qr.add_data(text)
    qr.make(fit=True)

    image = qr.make_image(fill_color='black', back_color='white')
    # The extension of the image can be .png .jpg
    image.save('QRCode-' + arq_name + '.png')


message = input('\nInput data to be converted into an QR Code: \n\n').strip()
arq_name = input(
    '\nEnter the name of the file containing the QR Code: \n\n').strip()

qrcode_generator(message, arq_name)
