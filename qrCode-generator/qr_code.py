#importing necessary modules
import qrcode as qr

# make() is a function of qrcode module which makes qrcodes
img = qr.make("https://youtu.be/xvFZjo5PgG0?feature=shared")

# sace() functions saves the qrcode with the name given by the developer
img.save("normal_regular_qrcode.png")


