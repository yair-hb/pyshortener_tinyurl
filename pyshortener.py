import pyshorteners
from tkinter import *

s = pyshorteners.Shortener()

print (s.tinyurl.short('https://github.com/yair-hb'))