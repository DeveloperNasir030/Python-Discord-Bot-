import discord
from discord.ext import commands
import json
import os

# Bot-Konfiguration
TOKEN = "DEIN_BOT_TOKEN"
INTENTS = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=INTENTS, help_command=None)

# Lade Blacklist (falls vorhanden)
BLACKLIST_FILE = "blacklist.json"
blacklist = []
if os.path.exists(BLACKLIST_FILE):
    with open(BLACKLIST_FILE, "r", encoding="utf-8") as file:
        blacklist = json.load(file)

# Event: Bot ist bereit
@bot.event
async def on_ready():
    print(f'✅ Bot ist online! Eingeloggt als {bot.user}')
    await bot.change_presence(activity=discord.Game(name="Moderation & Support"))

# Fehlerbehandlung für Befehle
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"❌ {ctx.author.mention}, du hast nicht die benötigten Rechte für diesen Befehl.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"⚠️ Fehlendes Argument! Verwende `!help` für eine Liste aller Befehle.")
    else:
        await ctx.send("❌ Ein unbekannter Fehler ist aufgetreten.")
        print(error)

# Moderationsbefehle
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="Kein Grund angegeben"):
    await member.kick(reason=reason)
    await ctx.send(f"✅ {member.name} wurde gekickt. Grund: {reason}")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="Kein Grund angegeben"):
    await member.ban(reason=reason)
    await ctx.send(f"✅ {member.name} wurde gebannt. Grund: {reason}")

@bot.command()
@commands.has_permissions(moderate_members=True)
async def timeout(ctx, member: discord.Member, duration: int, *, reason="Kein Grund angegeben"):
    await member.timeout_for(duration * 60, reason=reason)
    await ctx.send(f"⏳ {member.name} wurde für {duration} Minuten getimeoutet. Grund: {reason}")

# Ticket-System
TICKET_CATEGORY = "Tickets"

@bot.command()
async def ticket(ctx):
    guild = ctx.guild
    category = discord.utils.get(guild.categories, name=TICKET_CATEGORY)
    if category is None:
        category = await guild.create_category(TICKET_CATEGORY)
    
    ticket_channel = await guild.create_text_channel(f"ticket-{ctx.author.name}", category=category)
    await ticket_channel.set_permissions(ctx.author, read_messages=True, send_messages=True)
    await ticket_channel.send(f"{ctx.author.mention}, dein Ticket wurde erstellt. Bitte beschreibe dein Anliegen.")

@bot.command()
async def close(ctx):
    if ctx.channel.category and ctx.channel.category.name == TICKET_CATEGORY:
        await ctx.send("📁 Ticket wird geschlossen...")
        await ctx.channel.delete()

# Nachrichtenmoderation
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    for word in blacklist:
        if word in message.content.lower():
            await message.delete()
            await message.channel.send(f"⚠️ {message.author.mention}, deine Nachricht enthält unerlaubte Wörter!")
    
    await bot.process_commands(message)

# Starte den Bot
bot.run(TOKEN)
