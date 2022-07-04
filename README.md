# discord-translator-bot
A Discord translator bot originally created for the [UAH ACM Hackathon 2022](https://github.com/nlive65/ACM-Hackathon-2022).<br>

Dependencies: [discord.py](https://pypi.org/project/discord.py/), json, os, [translators](https://pypi.org/project/translators/)<br>

The bot is not publicly available, but it can be run locally by cloning this repository and running the bot.py file.<br>
You must create your own app in the Discord Developer Portal and insert the API key into the config.json file.

### Features <br>
note: source and target languages must be called in abbreviated form as found in languages.txt<br>
**translate** <br>
$[tl | tr] [source language] [target language] [message]<br>
**text-to-speech** <br>
$tltts [source language] [target language] [message]<br>
**language guide** <br>
$lg <br>
**language abbrevation search** <br>
$ls [target language]<br>
**translate message by replying**<br>
$tm [target language]<br>
**translate to english by message reaction** <br>
react to message with 📥 (inbox_tray)
