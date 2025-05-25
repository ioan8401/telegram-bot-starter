import os
import random
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Inițializare API OpenAI
openai.api_key = os.environ["OPENAI_API_KEY"]

# Răspunsuri predefinite
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
    "CAACAgIAAxkBAAEEDWxmVuOVh2Z6MHmpOWqMeNZB4DiHRAACXgADVp29CqgoqbgkQ9TgMAQ",
    "CAACAgUAAxkBAAEEEVZmVxXeZIgLUzYo88a8I2V6A3whgAACFQMAAvcCyFbSKC4lST7uwDAE",
]

# Integrare GPT
async def chatgpt_raspuns(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ești Unicornella, un unicorn magic, prietenos și iubitor de curcubeie. Răspunzi cu imaginație, glume și bucurie copiilor."},
                {"role": "user", "content": text},
            ],
            max_tokens=150,
            temperature=0.9,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return "Ups! Magia s-a întrerupt. Mai încearcă puțin mai târziu!"

# Comenzi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bunăăă! Eu sunt Unicornella, prietena ta magică! Scrie-mi orice sau încearcă /poveste, /gluma sau /curcubeu")

async def poveste(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(POVESTE)

async def gluma(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(GLUME))

async def curcubeu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_sticker(random.choice(STICKERE))
    await update.message.reply_text("Uuuu! Un curcubeu magic a apărut pentru tine!")

async def raspuns(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    mesaj = await chatgpt_raspuns(user_text)
    await update.message.reply_text(mesaj)

# Pornire aplicație
if __name__ == '__main__':
    application = ApplicationBuilder().token(os.environ["TELEGRAM_BOT_TOKEN"]).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("poveste", poveste))
    application.add_handler(CommandHandler("gluma", gluma))
    application.add_handler(CommandHandler("curcubeu", curcubeu))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, raspuns))

    application.run_polling()
