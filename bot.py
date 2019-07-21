import os
import config
from pytube import YouTube
import re
import telegram
from flask import Flask
# from pytube import YouTube
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler


TOKEN = os.environ.get("TOKEN",'574990729:AAHvFVDSNg-LQ5RUSaPdbiQ2pOdDA7XI5Xc')
PORT = int(os.environ.get('PORT', '5000'))

def link(bot, update):
    if len(re.findall(r'(https?://[^\s]+)', update.message.text)) > 0:
        try:
            config.remove_files()
            mp3_link = config.youtube_link(update.message.text)
            yt = YouTube(mp3_link)

            range_kbps = []
            lst_ = (yt.streams.filter(only_audio=True).all())
            for i in lst_:
                kbps = re.search(r"abr=\"(.*?)kbps\"", str(i))
                range_kbps.append(int(kbps.group(1)))


            if min(range_kbps)== 50:

                filename = "input.webm"
                update.message.reply_text(yt.title+"\n....Начало скачивания....")
                config.youtube_download_min(mp3_link)



                update.message.reply_text("Конец скачивания: " + config.file_size(filename))
                config.convert_low32(filename)
                update.message.reply_text("Конец конвертации: " + config.file_size('output.mp3'))
                bot.send_chat_action(update.message.chat.id, 'upload_audio')
                audio = open('output.mp3', 'rb')
                bot.send_audio(update.message.chat.id, audio)


            else:
               update.message.reply_text("Минимальный битрейт: "+str(min(range_kbps))+"kbps")

        except Exception as ex:
            update.message.reply_text(str(ex))


    else:
        update.message.reply_text(config.help)


def update(bot, update):
    update.message.reply_text(str(update.message))


def echo(bot, update):
    update.message.reply_text(config.help)


def log(bot, update):
    with open('mylog.log', 'r') as myfile:
        update.message.reply_text(str(myfile.read()))


updater = Updater(TOKEN)
dispatcher = updater.dispatcher

#    Commands

log_handler = CommandHandler('log', update)
dispatcher.add_handler(log_handler)

update_handler = CommandHandler('update', update)
dispatcher.add_handler(update_handler)

#    Messages


link_handler = MessageHandler(Filters.text, link)
dispatcher.add_handler(link_handler)


##----------------Webhook-----------------------------

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.setWebhook("https://radiobot1.herokuapp.com/" + TOKEN)
updater.idle()

##---------------------Webhook_end---------------------