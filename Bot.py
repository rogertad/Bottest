
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = "8636449302:AAEEjquvZqP4L1yRCo-pJMfbm947za8oNGM"

async def start(update, context):
    await update.message.reply_text("Hello World!")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
