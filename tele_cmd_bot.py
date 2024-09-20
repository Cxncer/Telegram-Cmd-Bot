import os
from dotenv import load_dotenv
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext, MessageHandler, filters

# Load environment variables
load_dotenv()
TOKEN = os.getenv('TOKEN')

if not TOKEN:
    raise ValueError("No TOKEN found in environment variables.")

# Initialize the bot application
application = Application.builder().token(TOKEN).build()

# Define a persistent keyboard that will always be shown
def get_custom_keyboard():
    keyboard = [
        [KeyboardButton('/start'), KeyboardButton('/cancel')],
        [KeyboardButton('/restart')]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Start command handler
async def start(update: Update, context: CallbackContext):
    user = update.effective_user
    chat_type = update.message.chat.type

    # Custom keyboard
    reply_markup = get_custom_keyboard()

    # Send a message with the keyboard, differentiating between private and group chats
    if chat_type == 'private':  # Private chat
        await update.message.reply_text(f"Hello {user.first_name}, the bot has started!", reply_markup=reply_markup)
    elif chat_type in ['group', 'supergroup']:  # Group chats
        # Respond to the group, making the keyboard persist
        if user.username:
            await update.message.reply_text(f"Hello @{user.username}, the bot has started!", reply_markup=reply_markup)
        else:
            await update.message.reply_text(f"Hello {user.first_name}, the bot has started!", reply_markup=reply_markup)

# Cancel command handler
async def cancel(update: Update, context: CallbackContext):
    user = update.effective_user
    reply_markup = get_custom_keyboard()  # Keep sending the custom keyboard with each response
    await update.message.reply_text(f"Action canceled, {user.first_name}. ❌", reply_markup=reply_markup)

# Restart command handler
async def restart(update: Update, context: CallbackContext):
    user = update.effective_user
    reply_markup = get_custom_keyboard()  # Send the keyboard again to keep it persistent
    await update.message.reply_text(f"Bot restarted for {user.first_name}. 🔄", reply_markup=reply_markup)

# Unknown command handler for unrecognized commands (optional)
async def unknown(update: Update, context: CallbackContext):
    reply_markup = get_custom_keyboard()  # Keep the keyboard present even for unknown commands
    await update.message.reply_text("Sorry, I didn't understand that command.", reply_markup=reply_markup)

# Define handlers
application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('cancel', cancel))
application.add_handler(CommandHandler('restart', restart))
application.add_handler(MessageHandler(filters.COMMAND, unknown))  # Handles unrecognized commands

# Run the bot with polling
if __name__ == '__main__':
    application.run_polling()
