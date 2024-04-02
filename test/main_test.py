#------- IMPORTS ------
import telebot

bot = telebot.TeleBot('Your Token')


#---------------- KEYBOARD BUTTONS --------------
key_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
key_markup.add("Title1","Title2","Title3","Title4","Title5")

btn1= telebot.types.InlineKeyboardButton("proxy1")
btn2= telebot.types.InlineKeyboardButton("proxy2")
btn3= telebot.types.InlineKeyboardButton("proxy3")
btn4= telebot.types.InlineKeyboardButton("proxy4")
btn5= telebot.types.InlineKeyboardButton("proxy5")

markup = telebot.types.InlineKeyboardMarkup(row_width=1)
markup.add(btn1,btn2,btn3,btn4,btn5)


#------------ COMMANDS -------------
@bot.message_handler(commands=['start'])
def say_welcome(message):
    bot.send_message(message.chat.id,
    "Hi and Welcome! OrangeBats it's at your service♥",
    reply_markup=key_markup)


#-------- HANDLER CHECK ------------
@bot.message_handler()
def keyboard(message):
    if message.text == "Your text":
        bot.send_message(message.chat.id,"Your Description")

    elif message.text == "Your text":
        bot.send_message(message.chat.id,"Message1",reply_markup=markup)
        bot.send_message(message.chat.id,"Message2",reply_markup=markup)


#---------- RUN ------------
bot.infinity_polling()