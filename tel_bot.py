import telebot

token = ''
bot = telebot.TeleBot(token)
chat = ''

@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(message.chat.id, text="Приветствую тебя!")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.send_message(message.chat.id, text=message.text)

bot.polling()