import telepot
from datetime import datetime

# Define the function to handle the /start command
def start(chat_id):
    message = "Hello! Welcome to my bot. Here are the available commands:\n/start - Start the bot\n/help - Show this help message\n/info - Show information about the bot\n/status - Show the current status of the bot\n/time - Show the current time"
    bot.sendMessage(chat_id, message, parse_mode='Markdown')

    # Send a welcome image with a greeting message
    image_url = 'image.png' # replace with your image url
    caption = 'Welcome to my bot! I hope you enjoy using it.'
    bot.sendPhoto(chat_id, image_url, caption)

# Define the function to handle the /help command
def help(chat_id):
    message = "These are the available commands:\n/start - Start the bot\n/help - Show this help message\n/info - Show information about the bot\n/status - Show the current status of the bot\n/time - Show the current time"
    bot.sendMessage(chat_id, message, parse_mode='Markdown')

# Define the function to handle the /info command
def info(chat_id):
    message = "I am chat bot created by wubtBot. It can respond to several commands."
    bot.sendMessage(chat_id, message)

# Define the function to handle the /status command
def status(chat_id):
    bot.sendMessage(chat_id, "The bot is currently running.")

# Define the function to handle the /time command
def show_time(chat_id):
    now = datetime.now()
    message = f"The current time is {now.strftime('%H:%M:%S')}"
    bot.sendMessage(chat_id, message)

# Define the function to handle incoming messages
def handle(msg):
    try:
        content_type, chat_type, chat_id = telepot.glance(msg)
    except Exception as e:
        print(f"Error occurred while trying to handle incoming message: {e}")
        return

    if content_type == 'text':
        command = msg['text'].strip().lower()

        if command == '/start':
            start(chat_id)
        elif command == '/help':
            help(chat_id)
        elif command == '/info':
            info(chat_id)
        elif command == '/status':
            status(chat_id)
        elif command == '/time':
            show_time(chat_id)
        else:
            bot.sendMessage(chat_id, "Sorry, I don't understand that command.")


# Define the token for your bot obtained from BotFather
TOKEN = '5700079324:AAEAHNBR2FQ4yaU4S4oDBy8k-yC5jFcszNw'

# Create an instance of the bot
bot = telepot.Bot(TOKEN)

# Start listening for incoming messages
bot.message_loop(handle)

# Keep the program running
while True:
    pass

