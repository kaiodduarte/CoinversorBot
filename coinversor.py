import configparser
import telebot
import requests
from aux import get_texts, get_emojis
from telebot import types

config = configparser.ConfigParser()
config.sections()
config.read('bot.conf')

bot_token = config['DEFAULT']['bot_token']
bot = telebot.TeleBot(bot_token)

coins = {'AUD': 'Dólar Australiano', 'BRL': 'Real',
         'EUR': 'Euro', 'GBP': 'Libra Esterlina', 'JPY': 'Yen',
         'PYG': 'Guaraní Paraguaio', 'USD': 'Dólar Americano'}

def get_json(frm):
    rates = str(tuple([frm+i for i in list(coins.keys()) if(i != frm)]))
    url = (
        'http://query.yahooapis.com/v1/public/yql?q=select '
        +'* from yahoo.finance.xchange where pair'
        +' in%s&format=json&env=store://datatables.org/alltableswithkeys'%(rates)
        )

    try:
        response = requests.get(url)
        json = response.json()

    except Exception as e:
        print(e)

    else:
        return json['query']['results']['rate']

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, get_texts()[0], parse_mode='HTML')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, get_texts()[1], parse_mode='HTML')

@bot.message_handler(commands=['list'])
def send_currencylist(message):
    bot.reply_to(message, get_texts()[2], parse_mode='HTML')

def get_options(results, amount):
    options, index = [], 0

    try:
        amount = float(amount)
    except ValueError:
        amount = 1.0
        
    for currency in results:
        index += 1
        title = currency['id'][3:]
        title_, rate, date, time =  ' - ' + coins[title], round(float(currency['Rate'])*amount, 2), currency['Date'], currency['Time']

        msg_bot = (
            get_emojis()[1] + 'Conversão pronta!\n\n' + get_emojis()[4] + currency['Name']
            + ' = '+ str(rate) + get_emojis()[0] + str(float(amount))
            + get_emojis()[2] + date + get_emojis()[3] + time
            )

        option = types.InlineQueryResultArticle(str(index), title+title_,
                                       types.InputTextMessageContent(msg_bot), description = str(rate))
        options.append(option)

    return options

@bot.inline_handler(func=lambda m: True)
def query_text(inline_query):
    try:
        query = inline_query.query.upper()
        amount, coin = query[:-3], query[-3:]

        if(coin in coins):            
            bot.answer_inline_query(inline_query.id, get_options(get_json(coin), amount), cache_time=1, is_personal=True)
        
    except Exception as e:
        print(e)

if __name__ == '__main__':
    bot.polling()
