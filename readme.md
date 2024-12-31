# Cycord - A High-Performance Cython Wrapper for the Discord API
> [!NOTE]
> This library is currently unfinished and is not yet production ready. Join the [discord](https://discord.gg/xbZMHJjrTR) for updates.
## Overview
Cycord is a high-performance library built with Cython that provides an easy and efficient interface to the Discord API.

Designed to be a drop-in replacement for [discord.py](https://github.com/Rapptz/discord.py), Cycord allows you to effortlessly boost the performance of your existing bots.

## Example
look familiar? The library was designed this way :)
```python
import cycord
from cycord.ext import commands

intents = cycord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix = "!",
    intents=intents
)

@bot.command(name="ping")
async def ping(ctx: commands.Context):
    await ctx.reply("pong!")

bot.run("BOT_TOKEN")
```

## Key Features
- **Optimized for Performance**: Cycord is designed to be much faster and more efficient than traditional Python libraries, making it ideal for high-performance Discord bots. By using Cython, it reduces overhead and speeds up execution.

- **Efficient Data Compression with Zstd**: Cycord uses zstd for streaming compression. This reduces the amount of memory used and speeds up the handling of large amounts of data, especially useful for bots handling many messages or events.

- **Cython-Powered**: The core of Cycord is written in Cython, which compiles Python code to C for significant speed improvements. This allows Cycord to perform faster than pure Python libraries, without sacrificing the ease of use.

- **Fast JSON Parsing with orjson**: Cycord utilizes orjson for fast and efficient JSON parsing. This helps speed up the processing of data from Discord, allowing your bot to handle requests and responses more quickly.

## Installation
```
git clone https://github.com/cycord-lib/cycord && cd cycord
python -m pip install -r requirements.txt
python build.py
```
Running `build.py` will automatically compile the source code into a `.so` file and place it in your site-packages directory, along with the stub files for Python type hinting. (In other words you can just use the module normally with `import cycord` after running build.py)