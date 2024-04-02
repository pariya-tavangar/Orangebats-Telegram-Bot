import time
import mysql.connector
from telebot import TeleBot
from telebot import *
from config import *
from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup

bot = TeleBot(token='Your Token')

# -------- INLINE OR KEYBOARDS --------
first_markup = InlineKeyboardMarkup(row_width=1)
button1 = InlineKeyboardButton(text="Main Menu",callback_data="proceed")
button2 = InlineKeyboardButton(text="About Bot",callback_data="proceed")
first_markup.add(button1,button2)

second_markup = InlineKeyboardMarkup(row_width=1)
button3 = InlineKeyboardButton(text="",url="https://t.me/orangebats_proxy")
button4 = InlineKeyboardButton(text="",url="https://t.me/tablighsara_group")
button5 = InlineKeyboardButton(text="Joined",callback_data="proceed")
second_markup.add(button3,button4,button5)


third_markup = InlineKeyboardMarkup(row_width=2)
button6 = InlineKeyboardButton(callback_data="proxy")
button7 = InlineKeyboardButton(callback_data="config")
button8 = InlineKeyboardButton(callback_data="support")
button9 = InlineKeyboardButton(callback_data="shop")
button10 = InlineKeyboardButton(callback_data="ourchannel")
button11 = InlineKeyboardButton(callback_data="back")
third_markup.add(button6,button7,button8,button9,button10,button11)


proxy_markup = telebot.types.InlineKeyboardMarkup(row_width=1)
proxy_btn1= telebot.types.InlineKeyboardButton("",url='')
proxy_btn2= telebot.types.InlineKeyboardButton("",url='')
proxy_btn3= telebot.types.InlineKeyboardButton("",url='')
proxy_btn4= telebot.types.InlineKeyboardButton("",url='')
proxy_btn5= telebot.types.InlineKeyboardButton("",url='')
proxy_back= telebot.types.InlineKeyboardButton("",callback_data="proxyback")
proxy_markup.add(proxy_btn1,proxy_btn2,proxy_btn3,proxy_btn4,proxy_btn5,proxy_back)


config_back_markup = telebot.types.InlineKeyboardMarkup(row_width=1)
config_back= telebot.types.InlineKeyboardButton("Back",callback_data="configback")
config_back_markup.add(config_back)

config_back_markup = telebot.types.InlineKeyboardMarkup(row_width=1)
config_back= telebot.types.InlineKeyboardButton("Back",callback_data="configback")
config_back_markup.add(config_back)

support_back_markup = telebot.types.InlineKeyboardMarkup(row_width=1)
support_back= telebot.types.InlineKeyboardButton("Back",callback_data="supportback")
support_back_markup.add(support_back)

shop_back_markup = telebot.types.InlineKeyboardMarkup(row_width=1)
shop_back= telebot.types.InlineKeyboardButton("Back",callback_data="shopback")
shop_back_markup.add(shop_back)

ourchannel_back_markup = telebot.types.InlineKeyboardMarkup(row_width=1)
ourchannel_back= telebot.types.InlineKeyboardButton("Back",callback_data="ourchannelback")
ourchannel_back_markup.add(ourchannel_back)


# ------------- COMMANDS --------------
@bot.message_handler(commands=['start'])
def say_welcome(message):


    greet = bot.send_message(message.chat.id,
    "Hi and Welcome! OrangeBats it's at your service♥",reply_markup=first_markup)

    global greeting
    greeting = greet.message_id


def check_join(user, channels):
    for i in channels:
        is_member = bot.get_chat_member(chat_id=i,user_id=user)

        if is_member.status in ['kicked','left']:
            return False
    return True



#------------ CALL BACKS ----------------
@bot.callback_query_handler(func = lambda call: call.data=="proceed")
def checking_proceed(call):


    is_member = check_join(user=call.from_user.id, channels=channels)

    if is_member is False:
        ad = bot.send_message(chat_id=call.message.chat.id, text="For Further usage, join our channel",reply_markup=second_markup)
        time.sleep(10)
        adv = ad.message_id
        bot.delete_message(chat_id=call.message.chat.id,message_id=adv)
    else:
        bot.delete_message(chat_id=call.message.chat.id,message_id=greeting)
        main_menu = bot.send_message(chat_id=call.message.chat.id, text="You're in main menu",reply_markup=third_markup)
    global anchor_main
    anchor_main = main_menu.message_id


@bot.callback_query_handler(func = lambda call: call.data=="proxy")
def checking_proxy(call):

    bot.delete_message(chat_id=call.message.chat.id,message_id=anchor_main)
    is_member = check_join(user=call.from_user.id, channels=channels)
    if is_member is False:
        bot.send_message(chat_id=call.message.chat.id,text="For Further usage, join our channel",reply_markup=second_markup)
    else:
        a1 = bot.send_message(chat_id=call.message.chat.id,text="☑",reply_markup=proxy_markup)
    global anchor1
    anchor1=a1.message_id


@bot.callback_query_handler(func = lambda call: call.data=="config")
def checking_config(call):

    bot.delete_message(chat_id=call.message.chat.id,message_id=anchor_main)
    is_member = check_join(user=call.from_user.id, channels=channels)
    if is_member is False:
        bot.send_message(chat_id=call.message.chat.id,text="For Further usage, join our channel",reply_markup=second_markup)
    else:
        b2 = bot.send_message(chat_id=call.message.chat.id,text=""
                              ,reply_markup=config_back_markup)
    global anchor2
    anchor2=b2.message_id


@bot.callback_query_handler(func = lambda call: call.data=="support")
def checking_support(call):

    bot.delete_message(chat_id=call.message.chat.id,message_id=anchor_main)
    is_member = check_join(user=call.from_user.id, channels=channels)
    if is_member is False:
        bot.send_message(chat_id=call.message.chat.id, text="For Further usage, join our channel",reply_markup=second_markup)
    else:
        c3 = bot.send_message(chat_id=call.message.chat.id, text="Support♥"
                              ,reply_markup=support_back_markup)
    global anchor3
    anchor3=c3.message_id


@bot.callback_query_handler(func = lambda call: call.data=="shop")
def checking_shop(call):

    bot.delete_message(chat_id=call.message.chat.id,message_id=anchor_main)
    is_member = check_join(user=call.from_user.id, channels=channels)
    if is_member is False:
        bot.send_message(chat_id=call.message.chat.id, text="For Further usage, join our channel",reply_markup=second_markup)
    else:
        d4 = bot.send_message(chat_id=call.message.chat.id, text="https://t.me/orangebats_shop",reply_markup=shop_back_markup)
    global anchor4
    anchor4=d4.message_id


@bot.callback_query_handler(func = lambda call: call.data=="ourchannel")
def checking_ourchannel(call):

    bot.delete_message(chat_id=call.message.chat.id,message_id=anchor_main)
    is_member = check_join(user=call.from_user.id, channels=channels)
    if is_member is False:
        bot.send_message(chat_id=call.message.chat.id, text="For Further usage, join our channel",reply_markup=second_markup)
    else:
        e5 = bot.send_message(chat_id=call.message.chat.id, text="https://t.me/orangebats_proxy",reply_markup=ourchannel_back_markup)

    global anchor5
    anchor5=e5.message_id




#------------- BACK TO MENU  --------------
@bot.callback_query_handler(func = lambda call: call.data=="back")
def checking_back(call):

    bot.delete_message(chat_id=call.message.chat.id,message_id=anchor_main)
    greet = bot.send_message(chat_id=call.message.chat.id,text=
    "Hi and Welcome! OrangeBats it's at your service♥",reply_markup=first_markup)
    global greeting
    greeting = greet.message_id


@bot.callback_query_handler(func = lambda call: call.data=="proxyback")
def back_proxyback(call):

    bot.delete_message(chat_id=call.message.chat.id,message_id=anchor1)
    main_menu = bot.send_message(chat_id=call.message.chat.id, text="You're in main menu",reply_markup=third_markup)
    global anchor_main
    anchor_main = main_menu.message_id

@bot.callback_query_handler(func = lambda call: call.data=="configback")
def back_configback(call):

    bot.delete_message(chat_id=call.message.chat.id,message_id=anchor2)
    main_menu = bot.send_message(chat_id=call.message.chat.id, text="You're in main menu",reply_markup=third_markup)
    global anchor_main
    anchor_main = main_menu.message_id

@bot.callback_query_handler(func = lambda call: call.data=="supportback")
def back_supportback(call):

    bot.delete_message(chat_id=call.message.chat.id,message_id=anchor3)
    main_menu = bot.send_message(chat_id=call.message.chat.id, text="You're in main menu",reply_markup=third_markup)
    global anchor_main
    anchor_main = main_menu.message_id


@bot.callback_query_handler(func = lambda call: call.data=="shopback")
def back_shopback(call):

    bot.delete_message(chat_id=call.message.chat.id,message_id=anchor4)
    main_menu = bot.send_message(chat_id=call.message.chat.id, text="You're in main menu",reply_markup=third_markup)
    global anchor_main
    anchor_main = main_menu.message_id


@bot.callback_query_handler(func = lambda call: call.data=="ourchannelback")
def back_ourchannel(call):

    bot.delete_message(chat_id=call.message.chat.id,message_id=anchor5)
    main_menu = bot.send_message(chat_id=call.message.chat.id, text="You're in main menu",reply_markup=third_markup)
    global anchor_main
    anchor_main = main_menu.message_id


#--------- RUN -----------
bot.infinity_polling(skip_pending=True)
