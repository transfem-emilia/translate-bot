import discord
from discord.ext import commands
import translators as ts

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)


flag_to_language = {
    '🇬🇧': 'en',  # English
    '🇮🇹': 'it',  # Italian
    '🇺🇸': 'en',  # English (US)
    '🇨🇦': 'en',  # English (Canada)
    '🇦🇺': 'en',  # English (Australia)
    '🇫🇷': 'fr',  # French
    '🇪🇸': 'es',  # Spanish
    '🇩🇪': 'de',  # German
    '🇵🇹': 'pt',  # Portuguese
    '🇧🇷': 'pt',  # Portuguese (Brazil)
    '🇷🇺': 'ru',  # Russian
    '🇯🇵': 'ja',  # Japanese
    '🇨🇳': 'zh',  # Chinese (Simplified)
    '🇹🇼': 'zh-TW',  # Chinese (Traditional)
    '🇰🇷': 'ko',  # Korean
    '🇳🇱': 'nl',  # Dutch
    '🇸🇪': 'sv',  # Swedish
    '🇳🇴': 'no',  # Norwegian
    '🇩🇰': 'da',  # Danish
    '🇫🇮': 'fi',  # Finnish
    '🇮🇱': 'he',  # Hebrew
    '🇦🇪': 'ar',  # Arabic
    '🇮🇳': 'hi',  # Hindi
    '🇵🇰': 'ur',  # Urdu
    '🇧🇩': 'bn',  # Bengali
    '🇵🇱': 'pl',  # Polish
    '🇹🇷': 'tr',  # Turkish
    '🇬🇷': 'el',  # Greek
    '🇷🇴': 'ro',  # Romanian
    '🇨🇿': 'cs',  # Czech
    '🇭🇺': 'hu',  # Hungarian
    '🇺🇦': 'uk',  # Ukrainian
    '🇻🇳': 'vi',  # Vietnamese
    '🇹🇭': 'th',  # Thai
    '🇲🇾': 'ms',  # Malay
    '🇮🇩': 'id',  # Indonesian
}


@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user.name}')

@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return
    
    if reaction.emoji in flag_to_language:
        lang = flag_to_language[reaction.emoji]
        original_message = reaction.message.content
        translated_text = ts.translate_text(original_message, to_language=lang, translator='google')

        await reaction.message.channel.send(f'Translated to {lang}: {translated_text}')

# Replace 'BOT_TOKEN' with your actual bot token
bot.run('BOT_TOKEN')
