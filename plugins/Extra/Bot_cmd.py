from pyrogram import Client, filters
from pyrogram.types import BotCommand
from info import ADMINS

@Client.on_message(filters.command("commands") & filters.user(ADMINS))
async def set_commands(client, message):
    commands = [
        BotCommand("alive", "ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ ɪꜱ ᴀʟɪᴠᴇ"),
        BotCommand("start", "ᴛᴏ ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ"),
        BotCommand("group_rule", "ᴛᴏ ᴋɴᴏᴡ ᴛʜᴇ ɢʀᴏᴜᴘ ʀᴜʟᴇꜱ"),
        BotCommand("connect", "ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ"),
        BotCommand("request", "sᴇɴᴅ ᴀ Mᴏᴠɪᴇ/Sᴇʀɪᴇs ʀᴇᴏ‌ᴜᴇsᴛ ᴛᴏ ʙᴏᴛ ᴀᴅᴍɪɴs. ( ᴏɴʟʏ ᴡᴏʀᴋs ᴏɴ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ )"),
        BotCommand("broadcast", "ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ."),
        BotCommand("grp_broadcast", "ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs."),
        BotCommand("imdb", "ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ɪᴍᴅʙ ꜱᴏᴜʀᴄᴇ"),
        BotCommand("plan", "ᴄʜᴇᴄᴋ ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀꜱʜɪᴘ ᴘʟᴀɴꜱ"),
        BotCommand("most", "ᴛᴏ ɢᴇᴛ ᴍᴏꜱᴛ ꜱᴇᴀʀᴄʜᴇꜱ ʙᴜᴛᴛᴏɴ ʟɪꜱᴛ"),
        BotCommand("trend", "ᴛᴏ ɢᴇᴛ ᴛᴏᴘ ᴛʀᴇɴᴅɪɴɢ ʙᴜᴛᴛᴏɴ ʟɪꜱᴛ"),
        BotCommand("mostlist", "ᴛᴏ ꜱʜᴏᴡ ᴍᴏꜱᴛ ꜱᴇᴀʀᴄʜᴇꜱ ʟɪꜱᴛ"),
        BotCommand("trendlist", "ᴛᴏ ɢᴇᴛ ᴛᴏᴘ ᴛʀᴇɴᴅɪɴɢ ꜱᴇᴀʀᴄʜᴇꜱ ʟɪꜱᴛ"),
        BotCommand("myplan", "ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴜʀʀᴜɴᴛ ᴘʟᴀɴ"),
        BotCommand("redeem", "𝑇𝑜 𝑅𝑒𝑑𝑒𝑒𝑚 𝑃𝑟𝑒𝑚𝑖𝑢𝑚 𝐶𝑜𝑑𝑒"),
        BotCommand("refer", "ᴛᴏ ʀᴇꜰᴇʀ ʏᴏᴜʀ ꜰʀɪᴇɴᴅ ᴀɴᴅ ɢᴇᴛ ᴘʀᴇᴍɪᴜᴍ"),
        BotCommand("play", "ɢᴇᴛ ꜰʀᴇᴇ ᴘʀᴇᴍɪᴜᴍ..."),
        BotCommand("stats", "ᴄʜᴇᴄᴋ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ"),
        BotCommand("id", "ɢᴇᴛ ᴛᴇʟᴇɢʀᴀᴍ ɪᴅ"),
        BotCommand("info", "ɢᴇᴛ ᴜꜱᴇʀ ɪɴꜰᴏ"),
        BotCommand("font", "ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴄᴏᴏʟ ꜰᴏɴᴛꜱ"),
        BotCommand("settings", "ᴄʜᴀɴɢᴇ ʙᴏᴛ ꜱᴇᴛᴛɪɴɢꜱ"),
        BotCommand("admin_cmd", "ʙᴏᴛ ᴀᴅᴍɪɴ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅꜱ")
    ]
    await client.set_bot_commands(commands)
    await message.reply("Set command successfully✅ ")
