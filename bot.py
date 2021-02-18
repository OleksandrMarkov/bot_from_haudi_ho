'''
BOT with Haudi Ho
'''

import telebot
import config

import random

from telebot import types


bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands = ['start'])
def welcome(message):
	sti = open('static/Welcome.tgs', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
	item1 = types.KeyboardButton("random number") 
	item2 = types.KeyboardButton("how are you?")

	markup.add(item1, item2)

	bot.send_message(message.chat.id,
"Welcome, {0.first_name}!\nI am <b>{1.first_name}</b>, glad to see you!!!"
.format(message.from_user,
bot.get_me()), parse_mode = 'html',
reply_markup = markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
	#bot.send_message(message.chat.id, message.text) 'bot-parrot'
	if message.chat.type == 'private':
		if message.text == 'random number':
			bot.send_message(message.chat.id, str(random.randint(0,50)))
		elif message.text == 'how are you?':

			markup = types.InlineKeyboardMarkup(row_width = 2)
			item1 = types.InlineKeyboardButton("Well enough", callback_data = 'good')
			item2 = types.InlineKeyboardButton("Badly...", callback_data = 'bad')

			markup.add(item1, item2)

			bot.send_message(message.chat.id, "I'm fine, thank you, and you?", reply_markup = markup)
		else:
			bot.send_message(message.chat.id, "I'm shocked")		

@bot.callback_query_handler(func = lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'good':
				bot.send_message(call.message.chat.id, "Oh, it's wonderful!")
			elif call.data == 'bad':
				bot.send_message(call.message.chat.id, "Oh, it's sad...")

			#remove inline buttons
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, reply_markup = None)
			# show alert
			bot.answer_callback_query(chat_id = call.message.chat.chat_id, show_alert = False, text = "It's text notification")			
	
	except Exception as e:
		print(repr(e))

#RUN
bot.polling(none_stop = True)
