import telebot

from users.models import User

API_TOKEN = '6361840046:AAHn-0lEGAfkEUAu7aJal647j1XMb-biMDc'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


@bot.message_handler(commands=["users"])
def get_users_handler(message):
    users = User.objects.values("id", "name", "phone_number")  # [{"first_name": "A", "last_name": "B"}]
    msg = ""
    for i, user in enumerate(users):
        msg += f"{i + 1}. {user.get('name')} {user.get('phone_number')} | ID: {user.get('id')}\n"
    bot.send_message(message.chat.id, text=msg)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.set_my_commands(
    commands=[
        telebot.types.BotCommand("start", "Boshlash"),
        telebot.types.BotCommand("users", "Foydalanuvchilar")
    ],
)
