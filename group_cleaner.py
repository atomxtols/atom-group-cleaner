import asyncio
import sys
import time
import os
from telethon import TelegramClient, errors
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

def print_banner():
    banner = """
\\033[1;36m
█████╗ ████████╗ ██████╗ ███╗   ███╗     ██████╗██╗     ███████╗ █████╗ ███╗   ██╗███████╗██████╗ 
██╔══██╗╚══██╔══╝██╔═══██╗████╗ ████║    ██╔════╝██║     ██╔════╝██╔══██╗████╗  ██║██╔════╝██╔══██╗
███████║   ██║   ██║   ██║██╔████╔██║    ██║     ██║     █████╗  ███████║██╔██╗ ██║█████╗  ██████╔╝
██╔══██║   ██║   ██║   ██║██║╚██╔╝██║    ██║     ██║     ██╔══╝  ██╔══██║██║╚██╗██║██╔══╝  ██╔══██╗
██║  ██║   ██║   ╚██████╔╝██║ ╚═╝ ██║    ╚██████╗███████╗███████╗██║  ██║██║ ╚████║███████╗██║  ██║
╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝     ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
\\033[1;32m      🥛🛡️ ATOM Group Cleaner - التصفير الفائق وصفر تدخل 🥛🛡️
\\033[0m"""
    print(banner)

def play_bomb_animation():
    banner = """
\\033[1;36m
█████╗ ████████╗ ██████╗ ███╗   ███╗     ██████╗██╗     ███████╗ █████╗ ███╗   ██╗███████╗██████╗ 
██╔══██╗╚══██╔══╝██╔═══██╗████╗ ████║    ██╔════╝██║     ██╔════╝██╔══██╗████╗  ██║██╔════╝██╔══██╗
███████║   ██║   ██║   ██║██╔████╔██║    ██║     ██║     █████╗  ███████║██╔██╗ ██║█████╗  ██████╔╝
██╔══██║   ██║   ██║   ██║██║╚██╔╝██║    ██║     ██║     ██╔══╝  ██╔══██║██║╚██╗██║██╔══╝  ██╔══██╗
██║  ██║   ██║   ╚██████╔╝██║ ╚═╝ ██║    ╚██████╗███████╗███████╗██║  ██║██║ ╚████║███████╗██║  ██║
╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝     ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
\\033[0m"""
    frames = [
        # Frame 1: Bomb with lit fuse
        """
\\033[1;33m           *
          \\\\ 
         [💣]\\033[0m
        """,
        # Frame 2: Lit fuse closer
        """
\\033[1;33m          * 
         [💣]\\033[0m
        """,
        # Frame 3: Explosion start
        """
\\033[1;31m          . * .
         * 💥 *
          ' * '\\033[0m
        """,
        # Frame 4: Explosion expanding
        """
\\033[1;31m       .  *  .  *  .
     *   💥   💥   *
       '  *  .  *  '\\033[0m
        """
    ]
    for frame in frames:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(banner)
        print(frame)
        time.sleep(0.4)

def snake_eat_animation(member_name):
    # Inline snake eating animation: "🐍 ───> *" -> "🐍 😋 (Gulp!)"
    for i in range(5):
        spaces = " " * (i * 2)
        dots = "." * (8 - i * 2)
        sys.stdout.write(f"\\r\\033[1;32m[ 🐍 {spaces}===~> {dots}* ]\\033[0m ⚙️ Kicking: {member_name}")
        sys.stdout.flush()
        time.sleep(0.12)
    sys.stdout.write(f"\\r\\033[1;32m[ 🐍 {" " * 10}😋 (Gulp!) ]\\033[0m ✅ Kicked: {member_name}\\n")
    sys.stdout.flush()

def snake_delete_animation(msg_id):
    # Inline tank shooting animation: "🚜💨 ══💣 [Msg]" -> "🚜💨 💥"
    for i in range(4):
        spaces = " " * (i * 3)
        sys.stdout.write(f"\\r\\033[1;33m[ 🚜💨 {spaces}══💣   [Msg ID: {msg_id}] ]\\033[0m ⚙️ Deleting...")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write(f"\\r\\033[1;33m[ 🚜💨 {" " * 12}💥 (Boom!)               ]\\033[0m ✅ Deleted Msg: {msg_id}\\n")
    sys.stdout.flush()

async def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()

    print("\\n\\033[1;35m--- 🔒 إعدادات الأمان والاتصال بالفيديو المشفّر ---\\033[0m")
    api_id_str = input("📥 أدخل API ID الخاص بك (من my.telegram.org): ").strip()
    api_hash = input("📥 أدخل API Hash الخاص بك: ").strip()
    bot_token = input("📥 أدخل توكن البوت (Bot Token): ").strip()
    target_group = input("📥 أدخل يوزر القروب (مثال: @mygroup) أو الآيدي (مثل: -100xxxxxx): ").strip()

    try:
        api_id = int(api_id_str)
    except ValueError:
        print("\\033[1;31m❌ خطأ: الـ API ID يجب أن يكون رقماً فقط!\\033[0m")
        return

    # إنشاء جلسة البوت
    print("\\n🔄 جاري تسجيل الدخول بالبوت والاتصال بخوادم تليجرام المشفّرة...")
    bot = TelegramClient('atom_cleaner_session', api_id, api_hash)
    
    try:
        await bot.start(bot_token=bot_token)
        print("\\033[1;32m🟢 تم الاتصال بنجاح وسجل البوت نشط الآن!\\033[0m")
    except Exception as e:
        print(f"\\033[1;31m❌ فشل الاتصال بتليجرام. تأكد من صحة الـ API ID والـ API Hash وتوكن البوت: {e}\\033[0m")
        return

    try:
        group_entity = await bot.get_entity(target_group)
        print(f"\\033[1;32m🔎 تم العثور على القروب المستهدف: {group_entity.title}\\033[0m")
    except Exception as e:
        print(f"\\033[1;31m❌ لم يتم العثور على القروب. تأكد من إدخال المعرف الصحيح وأن البوت مشرف فيه: {e}\\033[0m")
        await bot.disconnect()
        return

    print("\\n\\033[1;36m--- اختر عملية التصفير المطلوبة ---\\033[0m")
    print("1. طرد جميع الأعضاء (Kick out everyone except admins)")
    print("2. مسح جميع الرسائل (Purge all messages)")
    print("3. تصفير كامل وشامل (أعضاء + رسائل)")
    
    choice = input("\\n👉 اختر رقم العملية (1/2/3): ").strip()

    if choice in ['1', '3']:
        await clean_members(bot, group_entity)
    if choice in ['2', '3']:
        await clean_messages(bot, group_entity)

    # تشغيل أنميشن القنبلة عند الانتهاء بنجاح
    play_bomb_animation()
    
    print("\\n\\033[1;32m🎉 تمت عملية التصفير بنجاح باهر وصفر تدخل! 🎉\\033[0m")
    await bot.disconnect()

async def clean_members(client, group):
    print("\\n\\033[1;32m🎬 بدء عملية طرد الأعضاء (أنميشن الثعبان نشط الآن):\\033[0m\\n")
    
    ban_rights = ChatBannedRights(
        until_date=None,
        view_messages=True,
        send_messages=True,
        send_media=True,
        send_stickers=True,
        send_gifs=True,
        send_games=True,
        send_inline=True,
        embed_links=True
    )
    
    me = await client.get_me()
    count = 0

    try:
        async for user in client.iter_participants(group):
            # تجنب طرد البوت لنفسه
            if user.id == me.id:
                continue
            
            try:
                # تشغيل الأنميشن
                snake_eat_animation(f"{user.first_name or ''} {user.last_name or ''} ({user.id})")
                
                # حظر المستخدم وطرد
                await client(EditBannedRequest(group, user.id, ban_rights))
                # إلغاء الحظر فوراً لكي يتمكن من العودة مستقبلاً (Kick وليس permanent ban)
                await client(EditBannedRequest(group, user.id, ChatBannedRights(until_date=None, view_messages=False)))
                
                count += 1
                await asyncio.sleep(1.0) # فاصل زمني آمن
                
            except errors.FloodWaitError as e:
                print(f"\\n\\033[1;31m⚠️ تقييد مؤقت! يجب الانتظار لـ {e.seconds} ثانية...\\033[0m")
                await asyncio.sleep(e.seconds)
            except errors.UserAdminInvalidError:
                # الحساب مشرف
                pass
            except Exception as e:
                print(f"\\n❌ فشل طرد العضو {user.id}: {e}")
                
    except Exception as e:
        print(f"\\n❌ خطأ في سحب قائمة الأعضاء: {e}")

async def clean_messages(client, group):
    print("\\n\\033[1;33m🎬 بدء عملية مسح الرسائل (أنميشن الدبابة نشط الآن):\\033[0m\\n")
    count = 0
    try:
        async for message in client.iter_messages(group):
            try:
                # تشغيل الأنميشن
                snake_delete_animation(message.id)
                
                # حذف الرسالة
                await client.delete_messages(group, message.id)
                count += 1
                await asyncio.sleep(0.5) # فاصل زمني آمن
            except errors.FloodWaitError as e:
                print(f"\\n\\033[1;31m⚠️ تقييد مؤقت! الانتظار لـ {e.seconds} ثانية...\\033[0m")
                await asyncio.sleep(e.seconds)
            except Exception as e:
                pass
    except Exception as e:
        print(f"\\n❌ خطأ في جلب الرسائل: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\\n\\033[1;31m🔌 تم إيقاف السكربت بواسطة المستخدم.\\033[0m")
