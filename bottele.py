import telebot
import mysql.connector

bot = telebot.TeleBot("1292746490:AAFRmwdk5Vlh3Te0tDRogfh3zIIaFI9nGQc")
myDb = mysql.connector.connect(host='localhost', user='root', database='bottele', password='')
sql = myDb.cursor()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['datasiswa'])
def menu_bottele(message):
	data_result = ''
	sql.execute(
		"SELECT * FROM `tabel_siswa`"
	)
	data = sql.fetchall()
	row = sql.rowcount
	if row > 0:
		numbering = 0
		for x in data:
			numbering += 1
			data_result = data_result + str(numbering) + ". " + str(x) + '\n'
			data_result = data_result.replace('(', '')
			data_result = data_result.replace('(', '')
			data_result = data_result.replace('(', '')
			data_result = data_result.replace('(', '')
		bot.reply_to(message, str(data_result))
bot.polling()
