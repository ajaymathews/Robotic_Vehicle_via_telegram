import telegram
from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def start(bot, update):
    update.message.reply_text('Welcome')
    custom_keyboard = [['STATUS','FRONT','FIRE'],['LEFT','STOP','RIGHT'],['DIST','BACK','CAM']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.sendMessage(update.message.chat_id,text="Checking status...",reply_markup=reply_markup)

def status(bot, update):
    update.message.reply_text('Welcome')


def front(bot, update):
    update.message.reply_text('moving forward')

def fire(bot, update):
    update.message.reply_text('fire')

def left(bot, update):
    update.message.reply_text('left')

def stop(bot, update):
    update.message.reply_text('stop')

def right(bot, update):
    update.message.reply_text('right')

def dist(bot, update):
    update.message.reply_text('distancw is x meters')

def back(bot, update):
    update.message.reply_text('Welcome')

def cam(bot, update):
    update.message.reply_text('Welcome')

bot = telegram.Bot(token='627333566:AAGanhIPY2BP7UqOJcdAhjYRlmOJZG6OuyM')
updater = Updater('627333566:AAGanhIPY2BP7UqOJcdAhjYR1mOJZG6OuyM')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('status', status))
updater.dispatcher.add_handler(CommandHandler('front', front))
updater.dispatcher.add_handler(CommandHandler('fire', fire))
updater.dispatcher.add_handler(CommandHandler('left', left))
updater.dispatcher.add_handler(CommandHandler('stop', stop))
updater.dispatcher.add_handler(CommandHandler('right', right))
updater.dispatcher.add_handler(CommandHandler('dist', dist))
updater.dispatcher.add_handler(CommandHandler('back', back))
updater.dispatcher.add_handler(CommandHandler('cam', cam))

try:    
   updater.start_polling()
   updater.idle()
  
except:
   print("Error: unable to start thread")

while 1:
   pass


    
