
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = "SEU_TOKEN_AQUI"

async def start(update, context):
    await update.message.reply_text("Hello World!")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
