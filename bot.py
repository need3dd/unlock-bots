import telebot

# Токен, который выдал BotFather
TOKEN = '9287494200:AAF-1vWvmfaGAsdPxQLpl1G-QW4Rw16W7hQ'
bot = telebot.TeleBot(TOKEN)

# Реакция на команду /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой бот. Пока я умею только повторять текст, но скоро научусь делать нужные вещи.")

# Реакция на любой другой текст
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Ты написал: {message.text}")

print("Бот запущен и готов к работе...")
# Запуск постоянного опроса серверов Telegram
bot.infinity_polling()