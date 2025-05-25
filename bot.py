import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import random

REPLICI_PAUL = [
    "Ce-ai bă, iar ai scăpat de la spitalul de nebuni?",
    "Ești atât de prost încât dacă tăceai, tot nu păreai deștept.",
    "Te-a făcut mă-ta din greșeală când s-a împiedicat de prostie.",
    "Tu ai fost la școală doar ca să-ți iei pauza de masă, așa-i?",
    "Când vorbești, parcă dau cu capul de perete. Și peretele râde de mine.",
    "Dacă tăceai, filozof rămâneai. Dar n-ai avut noroc, ai deschis gura.",
    "Ai creierul în vacanță și gura în grevă de bun simț.",
    "Dacă te-ai fi născut în epoca de piatră, te-ar fi respins și pietrele.",
    "Când mă uit la tine, îmi vine să-mi scot siguranțele din tabloul electric.",
    "Ai față de panou gol și minte de bec ars.",
    "Băi, ești definiția vie a unei greșeli genetice cu cont de Telegram.",
    "Ai fost creat când Dumnezeu era în pauză și Satana la butoane.",
    "Când ai idei, e ca și cum un Windows vechi încearcă să booteze pe un stick rupt.",
    "Te uiți în oglindă și oglinda încearcă să se închidă singură.",
    "Tu nu ești prost, ești un proiect eșuat cu copyright pe dezastru."
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
