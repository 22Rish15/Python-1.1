import qrcode
import PIL.Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=2,
)

qr.add_data("https://github.com/22Rish15?tab=repositories")

qr.make(fit=True)

img = qr.make_image(fill_color = "White",back_color = "Black")

img.save("GitHub.png")