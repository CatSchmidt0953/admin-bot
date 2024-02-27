import telebot 
from telebot import types
import time
from configs import bot
from defs import kick,ban,mute,unmute,pin,idk


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_invite = telebot.types.InlineKeyboardButton(text="Пригласить бота в группу", url="http://t.me/Laris_RD_Bot?startgroup=iris&admin=change_info+restrict_members+delete_messages+pin_messages+invite_users")
    button2 = types.InlineKeyboardButton(text="Помощь", callback_data="help")
    keyboard.add(button_invite,button2)
    bot.send_message(message.chat.id, "Добро пожаловать в админ бота", reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text.lower() == 'бот':
        bot.send_message(message.chat.id, "✅ На месте")
    elif message.text.lower() == 'мут':
        mute(message)
    elif message.text.lower() == 'кик':
        kick()
    elif message.text.lower() == 'бан':
        ban(message)
    elif message.text.lower() =='размут':
        unmute(message)
    elif message.text.lower() =='кто я':
          pass
    elif message.text.lower() == 'пин':
       pin(message)
    elif message.text.lower() == '':
    
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "help":
        bot.send_message(call.message.chat.id, "Команды: бан,мут,кик,размут")




bot.polling()










