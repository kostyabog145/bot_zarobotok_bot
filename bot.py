import telebot
from telebot import types # кнопки
from hbva import kvnjw
from datetime import datetime
from datetime import timedelta 
import smtplib

bot = telebot.TeleBot(kvnjw)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет,я бот который наконец-то поможет тебе заработать денег в интернете удаленно 😱 ')
    murkup_inline = types.InlineKeyboardMarkup() # создаем коавиатуру под сообщением

    button_yes = types.InlineKeyboardButton(text = 'Да', callback_data = 'yes') # создаем кнопку
    button_no = types.InlineKeyboardButton(text = 'Нет', callback_data = 'no') # создаем кнопку

    murkup_inline.add(button_yes, button_no) # добавляем в клавиатуру кнопки
    bot.send_message(message.chat.id, 'Но для начала,нам нужно твое соглашение на получение от нас писем. Ты готов получать все самые новые виды зароботка на почту ?', reply_markup = murkup_inline)

@bot.callback_query_handler(func = lambda call : True)
def yes_or_no(call):
    if call.data == 'yes':
        murkup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True) # создаем клавиатуру

        button_reg = types.KeyboardButton('Регистрация') # создаем кнопку

        murkup_reply.add(button_reg) # Добавляем в клавиатуру кнопку
        bot.send_message(call.message.chat.id, 'Отлично,теперь вам нужно зарегистрироваться. Для этого нажмите на кнопочку "Регистрация" и получите все знания 👇',reply_markup = murkup_reply)
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, 'Очень жаль что вам это не интересно 😭')

@bot.message_handler(content_types=['text'])
def if_else(message):
    if message.text.lower() == 'регистрация':
        bot.send_message(message.chat.id, 'Для регистрации укажите ваш email,куда мы сможем вам отправлять информацию 😏')

    for baza in message.text:
        if baza == '@':
            bot.send_message(message.chat.id, 'Спасибо,что остались с нами. Вы точно не пожалеете😉')
            try:
                smtpObj = smtplib.SMTP("smtp.meta.ua", 465) 
                smtpObj.starttls()
                smtpObj.login("BaskovaEvfaniya117@meta.ua", "nz2yBzx1zuE5") 
                smtpObj.sendmail("busovrm4@gmail.com", "BaskovaEvfaniya117@meta.ua", message.text)
            finally:
                smtpObj.quit()
bot.polling(none_stop = True)
