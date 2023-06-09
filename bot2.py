from telegram import ReplyKeyboardMarkup, Update, ReplyKeyboardRemove
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    PicklePersistence,
    CallbackContext,
)
import os
import time
import requests
from random import randrange

TOKEN = os.getenv("TOKEN")
updater = Updater(TOKEN)
# Hello WORLD!!!!!! PUSH AND PULL

def start_handler(update: Update, context: CallbackContext) -> None:
    # with open('fetch2.txt') as f:
    #     for line in f:
    #         reply_text1 = line
    #         # update.message.reply_text(reply_text1)
    #         reply_text2 = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage?chat_id=-1001755597531&text=' + reply_text1
    #         requests.post(reply_text2)
    #         time.sleep(1)

    f = open('fetch2.txt', mode="r", encoding="utf-8")
    lines = f.readlines()
    x = len(lines)
    matn = lines[randrange(x)]
    msg_handler(matn)


def start_handler2(update: Update, context: CallbackContext) -> None:
    msg_handler('Shootool Bomboli')


def msg_handler(message) -> None:
    reply_text = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage?chat_id=-1001755597531&text=' + message
    requests.post(reply_text)


def func_handler(command, function) -> None:
    start_command = CommandHandler(command, function)
    updater.dispatcher.add_handler(start_command)


func_handler("start", start_handler)
func_handler("start2", start_handler2)

updater.start_polling()
updater.idle()
