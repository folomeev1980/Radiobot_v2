import os
import telegram
from flask import Flask
# from pytube import YouTube
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
#


















TOKEN = os.environ.get("TOKEN",'574990729:AAHvFVDSNg-LQ5RUSaPdbiQ2pOdDA7XI5Xc')
PORT = int(os.environ.get('PORT', '5000'))

def link():
    pass











updater = Updater(TOKEN)
dispatcher = updater.dispatcher


link_handler = MessageHandler(Filters.text, link)

dispatcher.add_handler(link_handler)



##----------------Webhook-----------------------------

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.setWebhook("https://radiobot1.herokuapp.com/" + TOKEN)
updater.idle()

##---------------------Webhook_end---------------------