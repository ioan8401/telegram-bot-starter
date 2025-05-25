import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import random

REPLICI_UNICORN = [
    "Hei, mică prințesă! Vrei să vorbim despre curcubeie?",
    "Știai că astăzi unicornul Rozalia a zburat peste pădurea de vată de zahăr?",
    "Zâmbetul tău face stelele să danseze!",
    "Unicornella te îmbrățișează strâns cu sclipici!",
    "Ți-ai pus azi coronița de curaj? Te stă minunat!",
    "Vrei o poveste cu zâne, stele și un unicorn mov?",
    "Astăzi e o zi perfectă pentru joacă și magie!",
]

POVESTE = """
A fost odată ca niciodată un unicorn pe nume Rozalia, care locuia pe un nor pufos roz. Într-o zi, a descoperit un curcubeu magic care ducea spre tărâmul înghețatei. Acolo a întâlnit o fetiță curajoasă care zâmbea mereu — se numea exact ca tine!
"""

GLUME = [
    "Ce face un unicorn la școală? Învățătură de poveste!",
    "Ce mănâncă unicornul la micul dejun? Fulgi de curcubeu!",
    "Cum se joacă unicornul? Sare peste stele!",
]

STICKERE = [
    "CAACAgIAAxkBAAEEDWxmVuOVh2Z6MHmpOWqMeNZB4DiHRAACXgADVp29CqgoqbgkQ9TgMAQ",  # Unicorn sticker
    "CAACAgUAAxkBAAEEEVZmVxXeZIgLUzYo88a8I2V6A3whgAACFQMAAvcCyFbSKC4lST7uwDAE",  # Cute unicorn
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bunăăă! Eu sunt Unicornella, prietena ta magică! Scrie-mi orice sau încearcă /poveste, /gluma sau /curcubeu")

async def raspuns(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mesaj = random.choice(REPLICI_UNICORN)
    await update.message.reply_text(mesaj)

async def poveste(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(POVESTE)

async def gluma(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(GLUME))

async def curcubeu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_sticker(random.choice(STICKERE))
    await update.message.reply_text("Uuuu! Un curcubeu magic a apărut pentru tine!")

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.environ["TELEGRAM_BOT_TOKEN"]).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("poveste", poveste))
    application.add_handler(CommandHandler("gluma", gluma))
    application.add_handler(CommandHandler("curcubeu", curcubeu))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, raspuns))

    application.run_polling()
