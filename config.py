import os
import re
import base64
import time
import cloudconvert
from pytube.__main__ import YouTube



data = str(base64.b64decode(b'NTc0OTkwNzI5OkFBSHZGVkRTTmctTFE1UlVTYVBkYmlRMnBPZERBN1hJNVhj'))
TOKEN =data[2:len(data)-1]
print(TOKEN)
data1 = str(base64.b64decode(b'QG1hbHRzZXY1MTExNw=='))
ln=data1[2:len(data1)-1]



help="Привет Это RadioBot, для скачивания mp3 c youtube:\n\n\
Пожалуйста, введите ссылку на видео, вида:  https:.......... ?"

def convert(filename):
    '''
    Функция конвертации файла в mp3
    :param filename: имя файла подаваемого для конвертации
    :return: Возвращает сконвертированный файл
    '''
    # try:
    #  os.remove('output.mp3')
    # except FileNotFoundError:
    #        pass


    api = cloudconvert.Api('yW5eTpoFJKgINxd7wpdeBdlsl1T5OyWlQ9xMrGyVkRJbxRwHWKpJYNQuz36P7KPY')

    process = api.convert({
        "inputformat": "webm",
        "outputformat": "mp3",
        "input": "upload",
        "converteroptions": {
            "audio_bitrate": 48,
            "audio_frequency": "22050",
            "audio_codec": "MP3",
            "audio_qscale": -1,

        },
        "file": open(filename, 'rb')
    })
    process.wait()

    process.download('output.mp3')

def convert_low32(filename):
    time.sleep(15)

    try:
     os.remove('output.mp3')
    except FileNotFoundError:
           pass

    time.sleep(15)
    api = cloudconvert.Api('yW5eTpoFJKgINxd7wpdeBdlsl1T5OyWlQ9xMrGyVkRJbxRwHWKpJYNQuz36P7KPY')
    process = api.convert({
        "inputformat": "webm",
        "outputformat": "mp3",
        "input": "upload",
        "converteroptions": {
            "audio_bitrate": 40,
            "audio_frequency": "44100",
            "audio_codec": "MP3",
            "audio_qscale": -1,

        },
        "file": open(filename, 'rb')
    })
    process.wait()

    process.download('output.mp3')



def remove_html_markup(s):
    tag = False
    quote = False
    out = ""

    for c in s:
            if c == '<' and not quote:
                tag = True
            elif c == '>' and not quote:
                tag = False
            elif (c == '"' or c == "'") and tag:
                quote = not quote
            elif not tag:
                out = out + c

    return out



def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size(file_path):

    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)

# Получение YOUTUBE_ID

def youtube_link(message_text):

    if len(message_text) == 28:
        youtube_id = re.search('\w\/(.*)', message_text).group(1)
    elif (message_text) == 57:
        youtube_id = re.search('/watch...(.*).feature', message_text).group(1)
    else:
        youtube_id = re.search('/watch...(...........)', message_text).group(1)

    mp3_link = 'https://www.youtube.com/watch?v=' +youtube_id

    return mp3_link


def youtube_download_test(mp3_link):
    yt = YouTube(mp3_link)
    f = yt.streams.filter(only_audio=True).all()
    flag=False
    a="50kbps"

    for i in f:

         if (str(i)[48:54])==a:
              flag=True
              i.download(filename='input')

              filename="input."+"webm"
              return filename
    if flag==False:
        return "No audo with 50kbps"




def youtube_download_min(mp3_link):
    yt = YouTube(mp3_link)

    f = yt.streams.filter(only_audio=True).all()
    start = int((re.search('abr=.(.*)kbps', str(f[0])).group(1)))
    for i in range(0, len(f), 1):
        a = str(f[i])
        b = int((re.search('abr=.(.*)kbps', a).group(1)))
        if b < start:
            start = b
            f[i].download(filename='input')
            rash=str((re.search('audio/(.*).', str(f[i])).group(1)))
            filename="input."+rash
            return filename
        # else:
        #     f[i].download(filename='input')
        #     rash = str((re.search('audio/(.*).', str(f[i])).group(1)))
        #     filename = "input." + rash
        #     return filename

def youtube_filename_min(mp3_link):
    yt = YouTube(mp3_link)

    f = yt.streams.filter(only_audio=True).all()
    start = int((re.search('abr=.(.*)kbps', str(f[0])).group(1)))
    for i in range(0, len(f), 1):
        a = str(f[i])
        b = int((re.search('abr=.(.*)kbps', a).group(1)))
        if b < start:
            start = b
            rash=str((re.search('audio/(.*)" abr=', str(f[i])).group(1)))
            filename="input."+rash
            return filename
        # else:
        #     rash = str((re.search('audio/(.*)" abr=', str(f[i])).group(1)))
        #     filename = "input." + rash
        #     return filename


def youtube_bitrate_min(mp3_link):
    yt = YouTube(mp3_link)
    f = yt.streams.filter(only_audio=True).all()
    start = int((re.search('abr=.(.*)kbps', str(f[0])).group(1)))
    for i in range(0, len(f), 1):
        a = str(f[i])
        b = int((re.search('abr=.(.*)kbps', a).group(1)))
        if b < start:
            start = b
            return start
        # else:
        #     return start


def youtube_size_min(mp3_link):
    yt = YouTube(mp3_link)
    f = yt.streams.filter(only_audio=True).all()
    start = int((re.search('abr=.(.*)kbps', str(f[0])).group(1)))
    for i in range(0, len(f), 1):
        a = str(f[i])
        b = int((re.search('abr=.(.*)kbps', a).group(1)))
        if b < start:
            start = b
            size = f[i].filesize
            return int(size)
        # else:
        #     size = f[i].filesize
        #     return int(size)





def tutle(mp3_link):
    return YouTube(mp3_link).title


def bitrate(mp3_link):
    yt = YouTube(mp3_link)
    f = yt.streams.filter(only_audio=True, ).all()
    return f

def remove_files():
    if os.path.exists('input.webm'):
        os.remove('input.webm')

    if os.path.exists('input.mp4'):
        os.remove('input.mp4')

    if os.path.exists('output.mp3'):
            os.remove('output.mp3')

    else:
        print('Нет файлов для удаления')




def youtube_bitrate_next(mp3_link):
    yt = YouTube(mp3_link)
    f = yt.streams.filter(only_audio=True).all()
    start = int((re.search('abr=.(.*)kbps', str(f[0])).group(1)))
    for i in f:

        if int((re.search('abr=.(.*)kbps', str(i)).group(1)))>start:
            start=int((re.search('abr=.(.*)kbps', i).group(1)))
    return start

if __name__ == '__main__':
    print(youtube_bitrate_next("https://www.youtube.com/watch?v=4uQHLw-JMgA"))





