import pytube
url="https://www.youtube.com/watch?v=6DVYAsL8lxU"
yt=pytube.YouTube(url)
print(yt.title)