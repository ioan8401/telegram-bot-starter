import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import random

REPLICI_PAUL = [
    "Ce vrei bă, iar tu? Te-ai plictisit de viață?",
    "Du-te și fă ceva util, nu mai freca menta pe Telegram!",
    "Serios acum, cum de n-ai fost selectat pentru un test psihologic?",
    "Mă faci să îmi pierd neuronul ăla rămas, omule.",
    "Dacă inteligența ta era electricitate, n-ai aprinde nici becul de la frigider.",
    "Ai venit aici ca să mă faci să-mi pierd timpul? Bravo, ai reușit!",
    "Cum ai reușit să supraviețuiești atâta timp fără o hartă și un GPS în cap?",
"Știi că sunt boți mai inteligenți ca tine? Și eu sunt unul din ei.",
    "Când te privesc, chiar îmi pare bine că sunt doar o grămadă de cod.",
    "Taci și meditează la alegerile tale proaste. Eu aștept aici, ca un psihopat calm."
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salut. Eu sunt Paul. Nu mă enerva.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mesaj = random.choice(REPLICI_PAUL)
    await update.message.reply_text(mesaj)

if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()

    token = os.environ["TELEGRAM_BOT_TOKEN"]

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("PaulBot rulează...")
    app.run_polling()
