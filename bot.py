import logging
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TELEGRAM_TOKEN = "7384086918:AAH8mJLsd62XsH0EQf9NPfL71NzfTJ81srU"
OPENAI_API_KEY = "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"

# Client OpenAI modern
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Logging (opțional)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Funcție care trimite mesajul la OpenAI și returnează răspunsul
async def ask_openai(prompt: str) -> str:
    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Răspunde ca un prieten cu inteligență artificială pe nume Rozela. Ești caldă, amuzantă, dar empatică."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
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
