import asyncio
import sys
import time
import os
from telethon import TelegramClient, errors
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

# Configure stdout encoding to UTF-8 for emoji support on all platforms
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def print_banner():
    sys.stdout.write("\033[1;36m")
    print(r"""    ___  ______ ____  ___  ___
   /   |/_  __/ __ \/   |/   |
  / /| | / / / / / / /| / /| |
 / ___ |/ / / /_/ / ___ / ___ |
/_/  |_/_/  \____/_/  |_/_/  |_|""")
    print("\033[1;32m 🥛🛡️ ATOM - Clean Members & Messages 🥛🛡️\033[0m")

def play_bomb_animation():
    sys.stdout.write("\033[1;36m")
    banner = r"""    ___  ______ ____  ___  ___
   /   |/_  __/ __ \/   |/   |
  / /| | / / / / / / /| / /| |
 / ___ |/ / / /_/ / ___ / ___ |
/_/  |_/_/  \____/_/  |_/_/  |_|"""
    sys.stdout.write("\033[0m")
    frames = [
        # Frame 1: Bomb with lit fuse
        """\033[1;33m           *
          \\ 
         [💣]\033[0m""",
        # Frame 2: Lit fuse closer
        """\033[1;33m          * 
         [💣]\033[0m""",
        # Frame 3: Explosion start
        """\033[1;31m          . * .
         * 💥 *
          ' * '\033[0m""",
        # Frame 4: Explosion expanding
        """\033[1;31m       .  *  .  *  .
     *   💥   💥   *
       '  *  .  *  '\033[0m"""
    ]
    for frame in frames:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(banner)
        print(frame)
        time.sleep(0.4)

def snake_eat_animation(member_name):
    # Inline snake eating animation
    for i in range(5):
        spaces = " " * (i * 2)
        dots = "." * (8 - i * 2)
        sys.stdout.write(f"\r\033[1;32m[ 🐍 {spaces}===~> {dots}* ]\033[0m Kicking: {member_name}")
        sys.stdout.flush()
        time.sleep(0.12)
    sys.stdout.write(f"\r\033[1;32m[ 🐍 {' ' * 10}😋 (Gulp!) ]\033[0m Kicked: {member_name}\n")
    sys.stdout.flush()

def snake_delete_animation(msg_id):
    # Inline tank shooting animation
    for i in range(4):
        spaces = " " * (i * 3)
        sys.stdout.write(f"\r\033[1;33m[ 🚜💨 {spaces}══💣   [Msg ID: {msg_id}] ]\033[0m Deleting...")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write(f"\r\033[1;33m[ 🚜💨 {' ' * 12}💥 (Boom!)               ]\033[0m Deleted Msg: {msg_id}\n")
    sys.stdout.flush()

async def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()

    print("\n\033[1;35m--- 🔒 Connection & Security Settings ---\033[0m")
    api_id_str = input("📥 Enter API ID (from my.telegram.org): ").strip()
    api_hash = input("📥 Enter API Hash: ").strip()
    bot_token = input("📥 Enter Bot Token (from @BotFather): ").strip()
    target_group = input("📥 Enter Group Username (e.g. @mygroup) or ID (e.g. -100xxxxxx): ").strip()

    try:
        api_id = int(api_id_str)
    except ValueError:
        print("\033[1;31m❌ Error: API ID must be a numeric value!\033[0m")
        return

    # Connection initialization
    print("\n🔄 Connecting bot to Telegram secure servers...")
    bot = TelegramClient('atom_cleaner_session', api_id, api_hash)
    
    try:
        await bot.start(bot_token=bot_token)
        print("\033[1;32m🟢 Bot connected successfully!\033[0m")
    except Exception as e:
        print(f"\033[1;31m❌ Connection failed. Check your API ID, API Hash, or Bot Token: {e}\033[0m")
        return

    try:
        group_entity = await bot.get_entity(target_group)
        print(f"\033[1;32m🔎 Target group found: {group_entity.title}\033[0m")
    except Exception as e:
        print(f"\033[1;31m❌ Group not found. Make sure the ID/username is correct and the bot is an admin: {e}\033[0m")
        await bot.disconnect()
        return

    print("\n\033[1;36m--- Select Purge Option ---\033[0m")
    print("1. Kick all members (except administrators)")
    print("2. Delete all messages (Purge all)")
    print("3. Full Reset (Members + Messages)")
    
    choice = input("\n👉 Choose option (1/2/3): ").strip()

    if choice in ['1', '3']:
        await clean_members(bot, group_entity)
    if choice in ['2', '3']:
        await clean_messages(bot, group_entity)

    # Trigger bomb animation upon completion
    play_bomb_animation()
    
    print("\n\033[1;32m🎉 Group Cleaned Successfully! 🎉\033[0m")
    await bot.disconnect()

async def clean_members(client, group):
    print("\n\033[1;32m🎬 Starting member purge:\033[0m\n")
    
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
            if user.id == me.id:
                continue
            
            try:
                # Play inline animation
                snake_eat_animation(f"{user.first_name or ''} {user.last_name or ''} ({user.id})")
                
                await client(EditBannedRequest(group, user.id, ban_rights))
                await client(EditBannedRequest(group, user.id, ChatBannedRights(until_date=None, view_messages=False)))
                
                count += 1
                await asyncio.sleep(1.0)
                
            except errors.FloodWaitError as e:
                print(f"\n\033[1;31m⚠️ Rate limit hit! Waiting {e.seconds} seconds...\033[0m")
                await asyncio.sleep(e.seconds)
            except errors.UserAdminInvalidError:
                pass
            except Exception as e:
                print(f"\n❌ Failed to kick user {user.id}: {e}")
                
    except Exception as e:
        print(f"\n❌ Error fetching group members: {e}")

async def clean_messages(client, group):
    print("\n\033[1;33m🎬 Starting message purge:\033[0m\n")
    count = 0
    try:
        async for message in client.iter_messages(group):
            try:
                snake_delete_animation(message.id)
                await client.delete_messages(group, message.id)
                count += 1
                await asyncio.sleep(0.5)
            except errors.FloodWaitError as e:
                print(f"\n\033[1;31m⚠️ Rate limit hit! Waiting {e.seconds} seconds...\033[0m")
                await asyncio.sleep(e.seconds)
            except Exception as e:
                pass
    except Exception as e:
        print(f"\n❌ Error fetching group messages: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\033[1;31m🔌 Script stopped by user.\033[0m")
