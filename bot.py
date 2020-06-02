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

@bot.message_handler(commands=['statistic'])
def statistic(message):
    bot.send_message(message.chat.id, 'До начала рассылки осталось : 994/1000 email-адресов в базе')

@bot.callback_query_handler(func = lambda call : True)
def yes_or_no(call):
    if call.data == 'yes':
        murkup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True) # создаем клавиатуру

        button_reg = types.KeyboardButton('Регистрация') # создаем кнопку

        murkup_reply.add(button_reg) # Добавляем в клавиатуру кнопку
        bot.send_message(call.message.chat.id, 'Отлично,теперь вам нужно зарегистрироваться. Для этого нажмите на кнопочку "Регистрация" и получите все знания 👇',reply_markup = murkup_reply)
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, 'Очень жаль что вам это не интересно 😭')

baza_email = []

@bot.message_handler(commands=['email'])
def email_in_baza(message):
    bot.send_message(message.chat.id, f'Email-адресса в базе : {baza_email}')

@bot.message_handler(commands=['send_message'])
def send_message(message):
    try:
        smtpObj = smtplib.SMTP("smtp.gmail.com", 587) 
        smtpObj.starttls()
        smtpObj.login("kolya.com145@gmail.com", "Kolya14102005") 
        for i in baza_email:
            smtpObj.sendmail("kolya.com145@gmail.com", "kolya.com145@gmail.com", i)
    finally:
        smtpObj.quit()
        baza_email.clear()
        bot.send_message(message.chat.id, 'Сообщения все отправлены и список очищен')

@bot.message_handler(content_types=['text'])
def all(message):
    if message.text.lower() == 'регистрация':
        bot.send_message(message.chat.id, 'Для регистрации укажите ваш email,куда мы сможем вам отправлять информацию 😏') 

    for baza in message.text:
        if baza == '@':
            bot.send_message(message.chat.id, 'Спасибо,что остались с нами. Вы точно не пожалеете😉')
            bot.send_message(message.chat.id, 'Если хочешь узнать когда начнется рассылка -> Введи команду : /statistic')
            baza_email.append(f'\n {message.text}')            

if __name__ == "__main__":
    bot.infinity_polling()
