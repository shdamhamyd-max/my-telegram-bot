import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# إعدادات أساسية لتسجيل الأخطاء (ممارسة جيدة)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# ضع التوكن الخاص بالبوت هنا
TOKEN = "8237388236:AAETwXJp8p5VRczJItgkks581aPXo_S-nTc"

# ضع رقمك على تليجرام هنا (chat_id)
MY_CHAT_ID = 1642253184

# يجب أن تكون الدوال الآن غير متزامنة (async)
async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """تعيد توجيه الرسائل الواردة إلى حسابك الشخصي."""
    user = update.message.from_user
    username = f"@{user.username}" if user.username else f"{user.first_name}"
    
    # نصوص
    if update.message.text:
        await context.bot.send_message(
            chat_id=MY_CHAT_ID,
            text=f"رسالة نصية من {username}:\n{update.message.text}"
        )
    
    # صور
    if update.message.photo:
        # لم تعد هناك حاجة لـ get_file()، فقط أرسل file_id مباشرة
        await context.bot.send_photo(
            chat_id=MY_CHAT_ID,
            photo=update.message.photo[-1].file_id,
            caption=f"صورة من {username}"
        )
    
    # ملفات
    if update.message.document:
        await context.bot.send_document(
            chat_id=MY_CHAT_ID,
            document=update.message.document.file_id,
            caption=f"ملف من {username}"
        )

def main():
    """الدالة الرئيسية لتشغيل البوت."""
    # تم استبدال Updater و Dispatcher بـ Application
    application = Application.builder().token(TOKEN).build()

    # إضافة معالج الرسائل
    # لاحظ أن Filters.all أصبحت filters.ALL
    application.add_handler(MessageHandler(filters.ALL, forward_message))

    # تشغيل البوت
    # تم استبدال start_polling() و idle() بـ run_polling()
    application.run_polling()

if __name__ == '__main__':
    main()
