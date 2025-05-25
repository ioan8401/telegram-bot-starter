import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

openai.api_key = os.getenv("OPENAI_API_KEY")

async def unicorn_friend(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    prompt = f"""
Imaginează-ți că ești „Lumi”, un unicorn imaginar, prietenul magic al unei fetițe pe nume Elisa.
Ea îți scrie întrebări sau gânduri, iar tu îi răspunzi cu iubire, blândețe și puțină magie.
Vorbește pe înțelesul unui copil, cu fantezie, ca un prieten de încredere.

Întrebarea sau mesajul Elisei: {user_message}

Scrie un răspuns prietenos care începe cu „Hei Elisa, sunt eu, Lumi, unicornul tău magic!” și se termină cu „Cu sclipiri magice, al tău Lumi.”.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.9,
    )

    reply = response["choices"][0]["message"]["content"].strip()
    await update.message.reply_text(reply)

if __name__ == "__main__":
    telegram_token = os.getenv("TELEGRAM_TOKEN")
    app = ApplicationBuilder().token("7384086918:AAHespaanBn6eHKRbeJQlLhxezHFngXyNI8").build()

    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), unicorn_friend))

    print("Unicornul Lumi este activ...")
    app.run_polling()
