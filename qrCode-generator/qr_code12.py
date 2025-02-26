import qrcode

#PIL is python pillow which generates , manipulated and saves QR code images
from PIL import Image

#qrcode.QRCode is a class in the qrcode module that lets you customize QR codes before generating them.
qr = qrcode.QRCode(version = 1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size = 10 , border = 10,)


qr.add_data("https://youtu.be/xvFZjo5PgG0?feature=shared")
qr.make(fit=True)
img = qr.make_image(fill_color = "#C71585" , back_color = "white")
img.save("EVERYDAY_CASUAL.png")