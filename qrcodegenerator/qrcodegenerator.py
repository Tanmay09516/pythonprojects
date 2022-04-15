import qrcode
import image
import os
qr= qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)
data=input("Put the data to generate qr for")
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black", back_color='white')
img.save("qr.png")
qrpath='qr.png'
os.startfile(qrpath)