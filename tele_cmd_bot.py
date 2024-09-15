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
    keyboard = [[KeyboardButton('/start'), KeyboardButton('/cancel')]]  # Create start/cancel buttons
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)   # Add buttons to the markup

# Cancel command handler
async def cancel(update: Update, context: CallbackContext):
    await update.message.reply_text("Operation cancelled.")

# Define command handlers
application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('cancel', cancel))

# Run the bot with polling
if __name__ == '__main__':
    application.run_polling()
    