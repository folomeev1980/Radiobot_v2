import os
import config
from pytube import YouTube
import re
import telegram
from flask import Flask
# from pytube import YouTube
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

url="https://www.youtube.com/watch?v=TamKnGkU5j0"

a=[]
yt = YouTube(url)
lst_=(yt.streams.filter(only_audio=True).all())
for i in lst_:
    kbps = re.search(r"abr=\"(.*?)kbps\"", str(i))
    a.append(int(kbps.group(1)))
print(type(min(a)))

