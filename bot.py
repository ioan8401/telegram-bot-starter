import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import random

REPLICI_PAUL = [
    "Ce vrei bă, iar tu? Te-ai plictisit de viață?",
    "Du-te și fă ceva util, nu mai freca menta pe Telegram!",
    "Serios acum, cum de n-ai fost selectat pentru un test psihologic?",
    "Mă faci să îmi pierd neuronul ăla rămas, omule.",
    "Dacă inteligența ta era electricitate,
