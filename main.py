import discord
from discord.ext import commands
import os
import asyncio
from pytubefix import YouTube
import re

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='vn!', intents=intents)
bot.remove_command('help')

queues = {}
loop_mode = {}
current_url = {}

def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name)

def dl_source(url):
    try:
        yt = YouTube(url)
        ys = yt.streams.get_audio_only()
        safe_title = sanitize_filename(yt.title)
        filename = f"{safe_title}"
        ys.download(filename=filename)
        return filename
    except Exception as e:
        print(f"Lỗi: {e}")
        return None

def check_queue(ctx, last_file):
    if os.path.exists(last_file):
        try: os.remove(last_file)
        except: pass

    guild_id = ctx.guild.id
    mode = loop_mode.get(guild_id, 0)
    
    if mode == 1:
        bot.loop.create_task(play_music(ctx, current_url[guild_id]))
        return

    if mode == 2:
        queues[guild_id].append(current_url[guild_id])

    if guild_id in queues and queues[guild_id]:
        next_url = queues[guild_id].pop(0)
        bot.loop.create_task(play_music(ctx, next_url))

async def play_music(ctx, url):
    guild_id = ctx.guild.id
    current_url[guild_id] = url
    filename = await bot.loop.run_in_executor(None, dl_source, url)
    
    if not filename:
        await ctx.send("Lỗi không tải được nhạc!")
        return

    source = discord.FFmpegPCMAudio(source=filename, options='-vn')
    ctx.voice_client.play(source, after=lambda e: check_queue(ctx, filename))
    await ctx.send(f"Đang phát: **{filename}** 🎵")
    os.remove(filename)

@bot.event
async def on_ready():
    print(f'Đã đăng nhập: {bot.user}')

@bot.command()
async def choi(ctx, *, arg):
    if not ctx.author.voice:
        return await ctx.send("Mày vào cái voice nào đi!")

    if not ctx.voice_client:
        await ctx.author.voice.channel.connect()
    
    guild_id = ctx.guild.id
    if guild_id not in queues:
        queues[guild_id] = []
        loop_mode[guild_id] = 0

    if ctx.voice_client.is_playing() or ctx.voice_client.is_paused():
        queues[guild_id].append(arg)
        await ctx.send(f"Đã thêm vào hàng chờ (Vị trí: {len(queues[guild_id])})")
    else:
        await play_music(ctx, arg)

@bot.command()
async def laplai(ctx):
    guild_id = ctx.guild.id
    loop_mode[guild_id] = 1 if loop_mode.get(guild_id) != 1 else 0
    status = "BẬT" if loop_mode[guild_id] == 1 else "TẮT"
    await ctx.send(f"🔂 Lặp lại bài hiện tại: **{status}**")

@bot.command()
async def laplaihangcho(ctx):
    guild_id = ctx.guild.id
    loop_mode[guild_id] = 2 if loop_mode.get(guild_id) != 2 else 0
    status = "BẬT" if loop_mode[guild_id] == 2 else "TẮT"
    await ctx.send(f"🔁 Lặp lại hàng chờ: **{status}**")

@bot.command()
async def skip(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        guild_id = ctx.guild.id
        if loop_mode.get(guild_id) == 1:
            loop_mode[guild_id] = 0
            await ctx.send("Đã tắt lặp lại để skip.")
        ctx.voice_client.stop()
        await ctx.send("Đã bỏ qua bài hiện tại!")

@bot.command()
async def cut(ctx):
    if ctx.voice_client:
        queues[ctx.guild.id] = []
        loop_mode[ctx.guild.id] = 0
        await ctx.voice_client.disconnect()
        await ctx.send("Cút đây! Ok?")

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="🎵 HƯỚNG DẪN SỬ DỤNG MUSIC VŨ NƯƠNG!",
        description="Chào mừng mày đến với hệ thống Music Vũ Nương! Dưới đây là danh sách các lệnh mày có thể dùng.",
        color=discord.Color.from_rgb(255, 105, 180) # Màu hồng cánh sen cực cháy
    )

    img_url = 'https://cdn.wallpapersafari.com/34/37/7df3XK.jpg'
    embed.set_thumbnail(url=img_url)

    embed.add_field(
        name="🚀 Lệnh Chính",
        value=(
            "`vn!choi [Link]` - Thêm bài vào hàng chờ hoặc phát ngay.\n"
            "`vn!skip` - Bỏ qua bài hiện tại.\n"
            "`vn!cut` - Đuổi bot khỏi Voice và xóa sạch hàng chờ."
        ),
        inline=False
    )

    embed.add_field(
        name="🔄 Chế Độ Lặp",
        value=(
            "`vn!laplai` - Lặp lại duy nhất 1 bài đang phát.\n"
            "`vn!laplaihangcho` - Hát hết danh sách rồi quay lại từ đầu."
        ),
        inline=False
    )

    embed.add_field(
        name="🛠️ Khác",
        value="`vn!help` - Hiện cái bảng này chứ gì nữa.",
        inline=False
    )

    embed.set_footer(text=f"Yêu cầu bởi {ctx.author.display_name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
    
    await ctx.send(embed=embed)
bot.run('Token')
