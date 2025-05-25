import logging
import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Configurări
openai.api_key = os.getenv("OPENAI_API_KEY")  # cheia ta trebuie setată pe Railway ca variabilă de mediu
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")  # cheia botului Telegram (tot ca variabilă de mediu)

# Logging (opțional dar util pentru depanare)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Funcție pentru a obține răspuns de la OpenAI
async def get_ai_response(user_input: str) -> str:
    try:
        response = await openai.ChatCompletion.acreate(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Ești Rozela, un unicorn magic, prietenoasă, amuzantă și mereu empatică. Răspunde cu inimă și curiozitate la orice spune utilizatorul."},
                {"role": "user", "content": user_input},
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Of, ceva nu a mers bine. Magia mea are nevoie de un pic de pauză: {e}"

# Handler pentru mesaje
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    response = await get_ai_response(user_text)
    reply = f"Sunt Rozela, unicornul tău magic!\n\n{response}"
    await update.message.reply_text(reply)

# Setup aplicație
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Rozela e gata să strălucească!")
    app.run_polling()

if __name__ == "__main__":
    main()
