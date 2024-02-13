import telebot , random
from telebot import types

# تذكر مصدري شايفك جالس تنسخ المهم 
''' 
قناتي @Crrazy_8
مبرمج الملف @BRoK8
'''

names = ['الله', 'الرحمن', 'الرحيم', 'الملك', 'القدوس', 'السلام', 'المؤمن', 'المهيمن', 'العزيز', 'الجبار', 'المتكبر', 'الخالق', 'البارئ', 'المصور', 'الغفار', 'القهار', 'الوهاب', 'الرزاق', 'الفتاح', 'العليم', 'القابض', 'الباسط', 'الخافض', 'الرافع', 'المعز', 'المذل', 'السميع', 'البصير', 'الحكم', 'العدل', 'اللطيف', 'الخبير', 'الحليم', 'العظيم', 'الغفور', 'الشكور', 'العلى', 'الكبير', 'الحفيظ', 'المقيت', 'الحسيب', 'الجليل', 'الكريم', 'الرقيب', 'المجيب', 'الواسع', 'الحكيم', 'الودود', 'المجيد', 'الباعث', 'الشهيد', 'الحق', 'الوكيل', 'القوى', 'المتين', 'الولى', 'الحميد', 'المحصى', 'المبدئ', 'المعيد', 'المحيى', 'المميت', 'الحي', 'القيوم', 'الواجد', 'الماجد', 'الواحد', 'الصمد', 'القادر', 'المقتدر', 'المقدم', 'المؤخر', 'الأول', 'الآخر', 'الظاهر', 'الباطن', 'الوالي', 'المتعالي', 'البر', 'التواب', 'المنتقم', 'العفو', 'الرؤوف', 'مالك الملك', 'ذو الجلال والإكرام', 'المقسط', 'الجامع', 'الغنى', 'المغنى', 'المانع', 'الضار', 'النافع', 'النور', 'الهادئ', 'البديع', 'الباقي', 'الوارث', 'الرشيد', 'الصبور']

count = 0

token = "6483903431:AAELNN4Lz2YUvaMcItQYhQ_dA0IrxOdQklQ"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):
    name = message.from_user.first_name
    global count
    count = 0
    markup = types.InlineKeyboardMarkup()
    
    markup.add(types.InlineKeyboardButton("تسبيح", callback_data="tasbeeh"))
    bot.send_message(message.chat.id,"مرحبا بك {} في بوت التسبيح اضغط اسفل على زر *تسبيح* للبدأ".format(name),parse_mode="markdown", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def all(call):
    global count

    if call.data == "tasbeeh":
        count += 1
 
    elif call.data == "reset":
        count = 0

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("• {} •".format(count), callback_data="tasbeeh"))
    markup.add(types.InlineKeyboardButton("تسبيح", callback_data="tasbeeh"))
    markup.add(types.InlineKeyboardButton("تصفير التسبيح", callback_data="reset"))
    
    tz = random.choice(names)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"*هو الله الذي لا اله الا هو \n( {tz} )*",parse_mode='markdown', reply_markup=markup)

print('run')
bot.infinity_polling()
# تذكر مصدري شايفك جالس تنسخ المهم 
''' 
قناتي @Crrazy_8
مبرمج الملف @BRoK8
'''