from pytube.__main__ import YouTube
from config import youtube_link
import re

url = "https://www.youtube.com/watch?v=Vnpef-uWB6s"
url_old = "https://www.youtube.com/watch?v=4vc2kQx5eTc"

range_kbps = []

url = (youtube_link(url))
yt = YouTube(url)

lst_ = (yt.streams.filter(only_audio=True).all())
print(lst_)
for index, i in enumerate(lst_):
    try:
        kbps = re.search(r"abr=\"(.*?)kbps\"", str(i))

        range_kbps.append(int(kbps.group(1)))
        print(index, kbps.group(1))
    except:
        range_kbps.append(1000)

if min(range_kbps) == 50:
    print(min(range_kbps))
    filename = "input.webm"
