import pyqrcode
import png 
from pyqrcode import QRCode



string = input("texts for qr : ")

url = pyqrcode.create(string)
url.png("qr.png" , scale = 8)


