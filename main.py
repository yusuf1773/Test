import requests
from bs4 import BeautifulSoup as bs
import re
from notifiers import get_notifier
import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

pattern = r"\­"

token=""

telegram = get_notifier("telegram")

r = requests.get("https://fight.ru/fighter-ratings/ufc/")

class Weight_r:
    def __init__(self, nomer, champ):
        self.nomer = nomer
        self.champ = champ
        self.string = ""

    def get_rat(self):
        weight_r = bs(r.text, 'html.parser').findAll("div", class_="col-xs-12 col-md-6 col-lg-4 org-single")[self.nomer].findAll(
            "div", class_="fighter-name")
        n = 1
        for i in weight_r:
            if re.sub(pattern, "", i.text) == self.champ and self.nomer is not 0:
                self.string += "Champion " + re.sub(pattern, "", i.text) + '\n'
            else:
                self.string += f"{n}. " + re.sub(pattern, "", i.text) + '\n'
                n += 1
        return self.string

def news():
    r = requests.get("https://fight.ru/news/ufc-news/")
    new = bs(r.text, "html.parser").findAll("div", class_="post-title news-title")
    hr = bs(r.text, "html.parser").findAll("a", class_="position-absolute h-100 w-100 top-0")
    string = ""
    n = 0
    for i in new:
        string += re.sub(pattern, "", i.text) + hr[n].get("href") + "\n....." + "\n"
        n += 1
        if n == 4:
            break

    return string

def new():
    r = requests.get("https://fight.ru/news/ufc-news/")
    img = bs(r.text, "html.parser").find("div", class_="post-gallery").find("img").get("src")
    new = bs(r.text, "html.parser").find("div", class_="post-title news-title")
    hr = bs(r.text, "html.parser").find("a", class_="position-absolute h-100 w-100 top-0").get("href")
    string = ""

    string += img
    string += re.sub(pattern, "", new.text) + hr + "\n" + "\n"

    return string

def prog():
    r = requests.get(
        "https://fight.ru/tips/ufc/kori-sjendhagen-protiv-marlona-vera-26-marta-na-ufc-fight-night-kto-stanet-sleduyushhim-pretendentom-na-poyas-chempiona-v-legchajshem-vese/")
    new = bs(r.text, "html.parser").findAll("p")

    string = ""

    for i in range(8, len(new) - 2):
        string += new[i].text

    return string


light = Weight_r(4, "Ислам Махачев")
feather = Weight_r(3, "Александр Волкановски")
bantam = Weight_r(2, "Алджамейн Стерлинг")
fly = Weight_r(1, "Брэндон Морено")
p4pm = Weight_r(0, "Джон Джонс")
welter = Weight_r(5, "Леон Эдвардс")
midle = Weight_r(6, "Алекс Перейра")
lightheavy = Weight_r(7, "Джамал Хилл")
heavy = Weight_r(8, "Джон Джонс")
p4pw = Weight_r(9, "Аманда Нунес")
straw = Weight_r(10, "Вейли Жанг")
flyw = Weight_r(11, "Алекса Грассо")
bantamw = Weight_r(12, "Аманда Нунес")
featherw = Weight_r(13, "Аманда Нунес")

news()

video = open('untitled.mp4', 'rb')

# Bot cod

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def send_wel(message):
    bot.send_message(message.chat.id, "Я бот по юфс. Здесь вы можете узнать рейтинги (/ratings), последние новости (/news),"
                                      " последнюю новость (/new), узнать прогноз на текущий мейн ивент (/prog) и скачать записи мэйн и ко-мейн ивентов номерных турниров этого года", reply_markup=keyboard)

@bot.message_handler(commands=["news"])
def send_wel(message):
    bot.send_message(message.chat.id, news())

@bot.message_handler(commands=["prog"])
def send_wel(message):
    bot.send_message(message.chat.id, prog())

@bot.message_handler(commands=["new"])
def send_wel(message):
    bot.send_message(message.chat.id, new())

# @bot.message_handler(commands=["286"])
# def send_wele(message):
#     video = open('untitled.mp4', 'rb')
#     bot.send_video(message.chat.id, video)



@bot.message_handler(commands=['ratings'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item = types.InlineKeyboardButton('ЛЕГКИЙ ВЕС', callback_data='ЛЕГКИЙ ВЕС')
    item2 = types.InlineKeyboardButton('ПОЛУЛЕГКИЙ ВЕС', callback_data='ПОЛУЛЕГКИЙ ВЕС')
    item3 = types.InlineKeyboardButton('P4P', callback_data='P4P')
    item4 = types.InlineKeyboardButton('НАИЛЕГЧАЙШИЙ ВЕС', callback_data='НАИЛЕГЧАЙШИЙ ВЕС')
    item5 = types.InlineKeyboardButton('ЛЕГЧАЙШИЙ ВЕС', callback_data='ЛЕГЧАЙШИЙ ВЕС')
    item6 = types.InlineKeyboardButton('ПОЛУСРЕДНИЙ ВЕС', callback_data='ПОЛУСРЕДНИЙ ВЕС')
    item7 = types.InlineKeyboardButton('СРЕДНИЙ ВЕС', callback_data='СРЕДНИЙ ВЕС')
    item8 = types.InlineKeyboardButton('ПОЛУТЯЖЁЛЫЙ ВЕС', callback_data='ПОЛУТЯЖЁЛЫЙ ВЕС')
    item9 = types.InlineKeyboardButton('ТЯЖЕЛЫЙ ВЕС', callback_data='ТЯЖЕЛЫЙ ВЕС')
    item10 = types.InlineKeyboardButton('P4P (ЖЕН)', callback_data='P4P (ЖЕН)')
    item11 = types.InlineKeyboardButton('ЖЕНСКИЙ МИНИМАЛЬНЫЙ ВЕС', callback_data='ЖЕНСКИЙ МИНИМАЛЬНЫЙ ВЕС')
    item12 = types.InlineKeyboardButton('ЖЕНСКИЙ НАИЛЕГЧАЙШИЙ ВЕС', callback_data='ЖЕНСКИЙ НАИЛЕГЧАЙШИЙ ВЕС')
    item13 = types.InlineKeyboardButton('ЖЕНСКИЙ ЛЕГЧАЙШИЙ ВЕС', callback_data='ЖЕНСКИЙ ЛЕГЧАЙШИЙ ВЕС')
    item14 = types.InlineKeyboardButton('ЖЕНСКИЙ ПОЛУЛЕГКИЙ ВЕС', callback_data='ЖЕНСКИЙ ПОЛУЛЕГКИЙ ВЕС')

    markup.add(item, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14)

    bot.send_message(message.chat.id, 'Какие рейтинги вас интересуют?', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'ЛЕГКИЙ ВЕС':
            light.get_rat()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=light.string)
        elif call.data == 'ПОЛУЛЕГКИЙ ВЕС':
            feather.get_rat()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=feather.string)
        elif call.data == 'P4P':
            p4pm.get_rat()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=p4pm.string)
        elif call.data == 'НАИЛЕГЧАЙШИЙ ВЕС':
            fly.get_rat()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=fly.string)
        elif call.data == 'ЛЕГЧАЙШИЙ ВЕС':
            bantam.get_rat()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=bantam.string)
        elif call.data == 'ПОЛУСРЕДНИЙ ВЕС':
            welter.get_rat()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=welter.string)
        elif call.data == 'СРЕДНИЙ ВЕС':
            midle.get_rat()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=midle.string)
        elif call.data == 'Полулёгкий вес':
            feather.get_rat()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=feather.string)
        elif call.data == 'ПОЛУТЯЖЁЛЫЙ ВЕС':
            lightheavy.get_rat()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=lightheavy.string)
        elif call.data == 'ТЯЖЕЛЫЙ ВЕС':
            heavy.get_rat()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=heavy.string)
        elif call.data == 'P4P (ЖЕН)':
            p4pw.get_rat()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=p4pw.string)
        elif call.data == 'ЖЕНСКИЙ МИНИМАЛЬНЫЙ ВЕС':
            straw.get_rat()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=straw.string)
        elif call.data == 'ЖЕНСКИЙ НАИЛЕГЧАЙШИЙ ВЕС':
            flyw.get_rat()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=flyw.string)
        elif call.data == 'ЖЕНСКИЙ ЛЕГЧАЙШИЙ ВЕС':
            bantamw.get_rat()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=bantamw.string)
        elif call.data == 'ЖЕНСКИЙ ПОЛУЛЕГКИЙ ВЕС':
            featherw.get_rat()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=featherw.string)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("/news"))
keyboard.add(KeyboardButton("/new"))
keyboard.add(KeyboardButton("/ratings"))
keyboard.add(KeyboardButton("/prog"))

bot.infinity_polling()