import os
import config
import logging
#from pytube.__main__ import YouTube
from pytube3.__main__ import YouTube as YouTube3
import re
import telegram
from flask import Flask
# from pytube import YouTube
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

TOKEN = os.environ.get("TOKEN", '574990729:AAHvFVDSNg-LQ5RUSaPdbiQ2pOdDA7XI5Xc')
PORT = int(os.environ.get('PORT', '5000'))
logger = logging.getLogger(__name__)


def link(bot, update):
    try:
        if len(re.findall(r'(https?://[^\s]+)', update.message.text)) > 0:

            config.remove_files()
            mp3_link = config.youtube_link(update.message.text)

            yt = YouTube3(mp3_link)
            print(yt)
            filename = "input.webm"
            titl = str(yt.title)[0:35]
            audio = yt.streams.filter(only_audio=True, file_extension="webm")[0]
            #update.message.reply_text("\n....Начало скачивания....")
            audio.download(filename='input')

            update.message.reply_text("Начало конвертации: " + config.file_size(filename))
            config.convert_low32(filename)
            update.message.reply_text("Конец конвертации: " + config.file_size('output.mp3'))
            bot.send_chat_action(update.message.chat.id, 'upload_audio')
            audio = open("output.mp3", 'rb')
            bot.send_audio(update.message.chat.id, audio, title=titl)





        else:
            update.message.reply_text(config.help)

    except Exception as ex:
        update.message.reply_text("Error <<<{}>>>>".format(str(ex)))


def update(bot, update):
    update.message.reply_text(str(update.message))


def echo(context, update):
    update.message.reply_text(config.help)


def log(bot, update):
    with open('mylog.log', 'r') as myfile:
        update.message.reply_text(str(myfile.read()))


# def error(update, bot):
#     """Log Errors caused by Updates."""
#     logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
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

  #  dispatcher.add_error_handler(error)

    ##----------------Webhook-----------------------------

    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN)
    updater.bot.setWebhook("https://radiobot3.herokuapp.com/" + TOKEN)
    updater.idle()

    ##---------------------Webhook_end---------------------


if __name__ == '__main__':
    main()
