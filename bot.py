import telebot
import os.path
import secrets
import string
from telebot import types
import auth
from userbase import only,change_password
bot = telebot.TeleBot('8037242551:AAGm9CE-59fYKfXSv_rOH_wYf3RjuPokaVA')
flag=0
chenka=0
l=[]
@bot.message_handler(commands=['start'])

def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Подтвердить аккаунт")
    btn2 = types.KeyboardButton("Восстановить пароль")
    markup.add(btn1,btn2)
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
    elif message.text=="Восстановить пароль":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да, уверен")
        btn2 = types.KeyboardButton("/start")
        markup.add(btn1,btn2)
        bot.send_message(message.chat.id,text="Вы уверены? Действие невозможно отменить. Чтобы вернуться назад нажмите /start",reply_markup=markup )
    elif message.text=="Да, уверен":
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(10))
        change_password(message.chat.id,password)
        bot.send_message(message.chat.id,text=f"Пароль сменен на: {password}")
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        try:
            idverf=message.text
            try:
                result = bot.get_chat_member(-1002249530735,message.chat.id )
                verifycode=auth.takecode(idverf)
                if only(str(message.chat.id))==False:
                    photo = open('static/img/wrong.jpg', 'rb')
                    bot.send_photo(message.chat.id, photo, caption="К телеграму уже привязан аккаунт. Он пройдет проверку администрации на нарушения.")
                else:
                    photo = open('static/img/code.jpg', 'rb')
                    auth.dopoln(idverf,str(message.chat.id))
                    if str(verifycode)!="Неверный код":
                        bot.send_photo(message.chat.id, photo, caption=str(verifycode))
                    else:
                        photo = open('static/img/wrong.jpg', 'rb')
                        bot.send_photo(message.chat.id, photo, caption="Неверный код")

            except:
                photo = open('static/img/link.jpg', 'rb')
                bot.send_photo(message.chat.id, photo, caption='Необходима подписка на канал @place2day')
        except:
            photo = open('static/img/wrong.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption="Неверный формат запроса")



bot.polling(none_stop=True)