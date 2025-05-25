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
