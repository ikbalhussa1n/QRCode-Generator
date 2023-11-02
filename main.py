import pyqrcode
from pyzbar.pyzbar import decode

from PIL import Image

qr = pyqrcode.create("https://github.com/ikbalhussa1n")

qr.png("myCode.png", scale=10)