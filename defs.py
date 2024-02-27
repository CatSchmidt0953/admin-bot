import telebot
from configs import bot
import time
import random

def kick(message):
 if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status
        if user_status in ['administrator', 'creator']:
            bot.reply_to(message, "Невозможно кикнуть администратора.")
        else:
            bot.kick_chat_member(chat_id, user_id)
            bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.first_name} был кикнут.")
 else:
         bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите кикнуть.")


def ban(message):
    if message.reply_to_message:
         chat_id = message.chat.id
         user_id = message.reply_to_message.from_user.id
         user_status = bot.get_chat_member(chat_id, user_id).status
         if user_status in ['administrator', 'creator']:
            bot.reply_to(message, "Невозможно забанить администратора.")
         else:
            bot.ban_chat_member(chat_id, user_id)
            bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.first_name} был забанен.")
    else:
          bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите кикнуть.")
   

def mute(message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно замутить администратора.")
        else:
            duration = 60 
            args = message.text.split()[1:]
            if args:
                try:
                    duration = int(args[0])
                except ValueError:
                    bot.reply_to(message, "Неправильный формат времени.")
                    return
                if duration < 1:
                    bot.reply_to(message, "Время должно быть положительным числом.")
                    return
                if duration > 1440:
                    bot.reply_to(message, "Максимальное время - 1 день.")
                    return
            bot.restrict_chat_member(chat_id, user_id, until_date=time.time()+duration*60)
            bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.first_name} замучен на {duration} минут.")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите замутить.")


def unmute(message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        bot.restrict_chat_member(chat_id, user_id, can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True, can_add_web_page_previews=True)
        bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.first_name} размучен.")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите размутить.")

def unban(message):
    pass

def pin(message):
     chat_id = message.chat.id
     message_id = message.reply_to_message.message_id
     bot.pin_chat_message(chat_id, message_id)


def idk(message):
    chat_id = message.chat.id
    chat_members = bot.get_chat_members(chat_id)  # Получаем всех участников чата
    usernames = [member.user.username for member in chat_members if member.user.username is not None]
    
    if usernames:
        random_user_name = random.choice(usernames)
        bot.send_message(chat_id, f'Я думаю, что это {random_user_name}')
    else:
        bot.send_message(chat_id, "В чате нет пользователей с юзернеймами.")