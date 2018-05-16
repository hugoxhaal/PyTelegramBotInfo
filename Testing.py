import telebot
import time
import requests
# import urllib
import json

bot = telebot.TeleBot(token='553333202:AAEkpNMrESpaEXKpw0hAUlVFZbibUdvXVxY')


@bot.message_handler(commands=['start'])
def welcome(m):
    cid = m.chat.id
    markup = telebot.types.InlineKeyboardMarkup()
    b = telebot.types.InlineKeyboardButton("Help", callback_data='help')
    c = telebot.types.InlineKeyboardButton("About", callback_data='amir')
    markup.add(b, c)
    nn = telebot.types.InlineKeyboardButton("Inline Mode", switch_inline_query='')
    oo = telebot.types.InlineKeyboardButton("Channel", url='https://telegram.me/offlineteam')
    markup.add(nn, oo)
    bot.send_message(cid, "Hi \n\n Welcome To TweenRoBOT \n\n Please Choose One :)",
                     disable_notification=True, reply_markup=markup)


@bot.message_handler(commands=['info'])
def basicInfo(m):
    text = m.text.replace("/info ", "")
    if text.lower().strip() == "btc":
        text = 1
    else:
        text = 0
    url = 'https://api.coinmarketcap.com/v2/ticker/{}'.format(text)
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    dataKey_Parsed = parsed["data"]
    usdKey_Parsed = parsed["data"]["quotes"]["USD"]


# KEY_INCLUDE. Incluye los datos relevantes a mostrar del diccionario
    dataKey_include = set(('name', 'symbol',))
    dict_dataKey = {k: v for k, v in dataKey_Parsed.items() if k in dataKey_include}

    usdKey_include = set(('price', 'percent_change_1h',))
    dict_usdKey = {k: v for k, v in usdKey_Parsed.items() if k in usdKey_include}
# KEY_INCLUDE FIN

    print(dict_dataKey)
    print(dict_usdKey)
    dict_print = dict_dataKey+dict_usdKey
    print(dict_print)

    printext = " *INFO* : ```{}``` \n".format(parsed)
    bot.send_message(m.chat.id, printext, parse_mode="Markdown")


bot.polling(none_stop=True)
