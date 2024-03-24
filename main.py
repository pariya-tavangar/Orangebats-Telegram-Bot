import telebot
bot = telebot.TeleBot('Your Token')


key_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
key_markup.add("Proxy | پروکسی","Config | کانفیگ","Advertise | تبلیغات","Donate | حمایت","About Us | درباره ما","Help | راهنما","Broadcast Channel | کانال اطلاع رسانی")


proxy_btn1= telebot.types.InlineKeyboardButton("ُIRANCEL|ایرانسل",url='https://t.me/proxy?server=82.115.21.113&port=443&secret=7vgBA-pMTrRo5SOZ7MwMG6N3d3cudGVzbGEuY29t')
proxy_btn2= telebot.types.InlineKeyboardButton("ُHAMRAH-AVAL|همراه اول",url='https://t.me/proxy?server=82.115.21.113&port=443&secret=7vgBA-pMTrRo5SOZ7MwMG6N3d3cudGVzbGEuY29t')
proxy_btn3= telebot.types.InlineKeyboardButton("ُRYTEL|رایتل",url='https://t.me/proxy?server=82.115.21.113&port=443&secret=7vgBA-pMTrRo5SOZ7MwMG6N3d3cudGVzbGEuY29t')
proxy_btn4= telebot.types.InlineKeyboardButton("ُSHATEL|شاتل",url='https://t.me/proxy?server=82.115.21.113&port=443&secret=7vgBA-pMTrRo5SOZ7MwMG6N3d3cudGVzbGEuY29t')
proxy_btn5= telebot.types.InlineKeyboardButton("ADSL|مودم و ثابت",url='https://t.me/proxy?server=82.115.21.113&port=443&secret=7vgBA-pMTrRo5SOZ7MwMG6N3d3cudGVzbGEuY29t')



markup = telebot.types.InlineKeyboardMarkup(row_width=1)
markup.add(proxy_btn1,proxy_btn2,proxy_btn3,proxy_btn4,proxy_btn5)

@bot.message_handler(commands=['start'])
def say_welcome(message):
    bot.send_message(message.chat.id,
    "سلام خوش اومدید!\nخفاش پرتقالی در خدمت شماست\nHi and Welcome! OrangeBats it's at your service♥",
    reply_markup=key_markup)


@bot.message_handler()
def keyboard(message):
    if message.text == "Config | کانفیگ":
        bot.send_message(message.chat.id,"کانفیگ پرسرعت تمام اپراتورها \n هریک از کانفیگ های زیر را کپی و استفاده کنید \n " " \nvless://45ec6f8d-5ae8-4079-aee2-a08dea4128a7@62.106.95.124:2083?type=tcp&security=none#%F0%9F%8D%8AOrangeBatsProxy-Telegram-Bot\n "" \nvless://98f484e4-b5db-45b4-8927-63701b583f0f@62.106.95.124:2083?type=tcp&security=none#%F0%9F%8D%8AOrangeBatsProxy-qnnzv6gp\n " " \nvless://841c615d-b7e0-42a0-b962-14840e5c5563@62.106.95.124:2083?type=tcp&security=none#%F0%9F%8D%8AOrangeBatsProxy-indhe9oo")

    elif message.text == "Proxy | پروکسی":
        bot.send_message(message.chat.id,"☑لیست پروکسی های بروز شده☑ \n " " \n🔽سرور اول🔽 ",reply_markup=markup)
        bot.send_message(message.chat.id,"☑لیست پروکسی های بروز شده☑ \n " " \n 🔽سرور دوم🔽 ",reply_markup=markup)


bot.infinity_polling()
