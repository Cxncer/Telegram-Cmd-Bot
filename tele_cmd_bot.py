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
    # Send a message with the buttons
    await update.message.reply_text("How can I help?", reply_markup=reply_markup)

# Cancel command handler
async def cancel(update: Update, context: CallbackContext):
    # You can handle any cleanup or state reset here if needed
    await update.message.reply_text("Canceling the operation.")

# Restart command handler
async def restart(update: Update, context: CallbackContext):
    # Handle the restart logic here (it could reset states, reload configuration, etc.)
    await update.message.reply_text("Restarting the bot...")

# Define command handlers
application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('cancel', cancel))
application.add_handler(CommandHandler('restart', restart))

# Run the bot with polling
if __name__ == '__main__':
    application.run_polling()
