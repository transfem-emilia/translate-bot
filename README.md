# translate-bot

A Discord bot that translates messages based on user reactions.

## Requirements

- Python 3.8 or later  
- A Discord bot (see [Creating a Bot Account](https://discordpy.readthedocs.io/en/stable/discord.html) for setup instructions)  
- A Discord bot token  
- The `discord.py` Python package  
  [https://pypi.org/project/discord.py/](https://pypi.org/project/discord.py/)  
- The `translators` Python package  
  [https://pypi.org/project/translators/](https://pypi.org/project/translators/)

## How It Works

After a message is sent in a channel, users can react to it using a supported flag emoji (such as 🇫🇷 for French). The bot detects the reaction and replies with a translated version of the message in the corresponding language.

> You can customize the list of supported languages and emoji in the source code.
