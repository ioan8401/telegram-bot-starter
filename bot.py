import logging
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Cheile tale
TELEGRAM_TOKEN = "7384086918:AAH8mJLsd62XsH0EQf9NPfL71NzfTJ81srU"
TOGETHER_API_KEY = "06bc5731d88d7b7cb2aef1dc1ad058650e57ebaed386dcb1d41cf228ac66122d"

# Setare client OpenAI pentru Together.ai
client = openai.OpenAI(
    base_url="https://api.together.xyz/v1",
    api_key=TOGETHER_API_KEY
)

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Funcția care trimite mesajul la Together și primește răspuns
async def ask_openai(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="mistralai/Mistral-7B-Instruct-v0.1",  # sau deepseek-ai/deepseek-coder
            messages=[
                {"role": "system", "content": "Răspunde ca un prieten cu inteligență artificială pe nume Rozela. Ești caldă, amuzantă, dar empatică."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Eroare AI: {e}"

# Handler pentru mesaje
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    ai_response = await ask_openai(user_message)
    await update.message.reply_text(ai_response)

# Start bot
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Botul rulează...")
    app.run_polling()

if __name__ == "__main__":
    main()
