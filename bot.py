import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bună, eu sunt Unicornul prietenos! Întreabă-mă orice vrei!")

async def get_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text(f"Chat ID-ul tău este: {chat_id}")

async def unicorn_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()
    response = f"Sunt Unicornul tău magic! Ai spus: „{user_message}” și mie îmi pare foarte interesant! Spune-mi mai multe!"

    await update.message.reply_text(response)

if __name__ == '__main__':
    app = ApplicationBuilder().token("7384086918:AAHespaanBn6eHKRbeJQlLhxezHFngXyNI8").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("chatid", get_chat_id))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unicorn_chat))

    print("Botul rulează...")
    app.run_polling()
