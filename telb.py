from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["پلن 1 ماهه", "پلن 3 ماهه"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "سلام 😎\nیه پلن انتخاب کن:",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "پلن" in text:
        await update.message.reply_text("عالی 👌\nآیدی یا اسمتو بفرست")
    else:
        await update.message.reply_text("سفارشت ثبت شد ✅")

app = ApplicationBuilder().token("8945011991:AAEDDI-_jwMTI5MK2pFjDVtSSeQFDeCM0uM").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()