import telebot
import os.path
from telebot import types
import auth
bot = telebot.TeleBot('8037242551:AAGm9CE-59fYKfXSv_rOH_wYf3RjuPokaVA')
flag=0
chenka=0
l=[]
@bot.message_handler(commands=['start'])

def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Подтвердить аккаунт")
    markup.add(btn1)
    photo = open('static/img/logo.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, caption="Добро пожаловать в Place2Day. Для удостоверения что вы не робот, получите код верификации:",reply_markup=markup)



@bot.message_handler(content_types=['text'])
def func(message):
    if message.text=="Подтвердить аккаунт":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        try:
            result = bot.get_chat_member(-1002249530735,message.chat.id )
            if result.status not in ('member', 'creator'):
                raise Exception
            photo = open('static/img/verify.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption="Введите выданный на сайте номер")
        except:
            photo = open('static/img/link.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='Необходима подписка на канал @place2day')
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        try:
            idverf=message.text
            try:
                result = bot.get_chat_member(-1002249530735,message.chat.id )
                verifycode=auth.takecode(idverf)
                photo = open('static/img/code.jpg', 'rb')
                bot.send_photo(message.chat.id, photo, caption=str(verifycode))
            except:
                photo = open('static/img/link.jpg', 'rb')
                bot.send_photo(message.chat.id, photo, caption='Необходима подписка на канал @place2day')
        except:
            photo = open('static/img/wrong.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption="Неверный формат запроса")



bot.polling(none_stop=True)