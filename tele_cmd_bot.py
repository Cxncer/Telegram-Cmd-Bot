import os
from dotenv import load_dotenv
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext

# Load environment variables
load_dotenv()
TOKEN = os.getenv('TOKEN')

if not TOKEN:
    raise ValueError("No TOKEN found in environment variables.")

# Initialize the bot application
application = Application.builder().token(TOKEN).build()

# Start command handler
async def start(update: Update, context: CallbackContext):
    # Create start, cancel, and restart buttons
    keyboard = [[KeyboardButton('/start'), KeyboardButton('/cancel'), KeyboardButton('/restart')]]  
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Started! Joch Joch mes jui.")

# Cancel command handler
async def cancel(update: Update, context: CallbackContext):
    # No reply, just handling the cancel command
    pass

# Restart command handler
async def restart(update: Update, context: CallbackContext):
    # No reply, just handling the restart command
    pass

# Define command handlers
application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('cancel', cancel))
application.add_handler(CommandHandler('restart', restart))

# Run the bot with polling
if __name__ == '__main__':
    application.run_polling()
