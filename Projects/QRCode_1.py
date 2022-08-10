import qrcode
import PIL.Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=2,
)

qr.add_data("khandelwalrishi36@gmail.com ✉")

qr.make(fit=True)

img = qr.make_image(fill_color = "White",back_color = "Black")

img.save("Email.png")