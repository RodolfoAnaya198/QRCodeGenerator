from fileinput import filename
from stat import filemode
import qrcode
import os
string = ("José Rodolfo Martínez Anaya")
img = qrcode.make(string)
type(img)
filename = "rodolfo.png"
img.save(filename)
print(f"Generated file:{os.getcwd()}\{filename}")
os.system(filename)