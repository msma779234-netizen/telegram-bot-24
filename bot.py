import telebot
TOKEN = os.getenv("8730614198:AAF7LRGrpBOOjuvPlpt6cayBwHOb4JQqFGQ") 
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "اهلا! البوت شغال ✅")
	
bot.polling()
