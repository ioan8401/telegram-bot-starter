import logging
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TELEGRAM_TOKEN = "7384086918:AAFVmD71YTApwTjWUUqHoDciiM91X9mZgD4"
OPENAI_API_KEY = "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"

# Setare cheie OpenAI
openai.api_key = OPENAI_API_KEY

# Logging (opțional)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Funcție care trimite mesajul la OpenAI și returnează răspunsul
async def ask_openai(prompt: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Răspunde ca un prieten cu inteligență artificială pe nume Rozela. Ești caldă, amuzantă, dar empatică."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Eroare OpenAI: {e}"

# Handler pentru toate mesajele text
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    ai_response = await ask_openai(user_message)
    await update.message.reply_text(ai_response)

# Punct de pornire
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Răspunde la orice mesaj text
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Botul rulează...")
    app.run_polling()

if __name__ == '__main__':
    main()
