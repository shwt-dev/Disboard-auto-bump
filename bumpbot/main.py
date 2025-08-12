import os
import sys
import discord
import aiohttp
from dotenv import load_dotenv
from loguru import logger
from typing import Tuple
from datetime import datetime
from discord import Webhook

# === Logging Configuration ===
logger.remove()
logger.add(sys.stderr, level="INFO", format="<green>{time}</green> <level>{message}</level>")

log_folder = "logs"
os.makedirs(log_folder, exist_ok=True)
log_filename = datetime.now().strftime("bumpbot_%Y-%m-%d_%H-%M-%S.log")
log_path = os.path.join(log_folder, log_filename)
logger.add(log_path, rotation="1 MB", retention="7 days", level="DEBUG")

# === Environment Variable Keys ===
ENV_KEYS = ['BOT_TOKEN', 'CHANNEL_ID', 'LOGS_WEBHOOK', 'PREFIX']

def load_env_vars(required_keys: list[str]) -> dict[str, str]:
    load_dotenv()
    env = {}
    for key in required_keys:
        value = os.getenv(key)
        if not value:
            logger.error(f"❌ Environment variable '{key}' is not set.")
            sys.exit(1)
        env[key] = value
    return env

# === BumpBot Class ===
class BumpBot(discord.Client):
    def __init__(self, channel_id: int, webhook_url: str, prefix: str):
        super().__init__()
        self.channel_id = channel_id
        self.webhook_url = webhook_url
        self.prefix = prefix
        self.bump_channel = None
        self.webhook = None
        self.http_session = None  # Don't initialize here!

    async def on_ready(self):
        logger.info(f"✅ Logged in as {self.user}")
        self.bump_channel = self.get_channel(self.channel_id)

        self.http_session = aiohttp.ClientSession()
        self.webhook = Webhook.from_url(self.webhook_url, session=self.http_session)

    async def close(self):
        if self.http_session:
            await self.http_session.close()
        await super().close()

    async def on_message(self, message: discord.Message):
        if message.author.id == self.user.id:
            return

        if not message.content.startswith(self.prefix):
            return

        logger.info(f"📩 Command received: {message.content}")
        command_body = message.content[len(self.prefix):].strip()

        if not command_body:
            return

        parts = command_body.split()
        command = parts[0].lower()
        args = parts[1:]

        # Command routing
        if command == "ping":
            await self.handle_ping(message)
        elif command == "help":
            await self.handle_help(message)
        elif command == "stats":
            await self.handle_stats(message)
        else:
            await message.channel.send(f"❓ Unknown command: `{command}`")

    # === Command Handlers ===
    async def handle_ping(self, message: discord.Message):
        await message.channel.send("🏓 Pong!")

    async def handle_help(self, message: discord.Message):
        help_text = (
            "**🤖 BumpBot Commands**\n\n"
            f"🔹 `{self.prefix} help` - Shows this help message\n"
            f"🔹 `{self.prefix} ping` - Check if the bot is responsive\n"
            f"🔹 `{self.prefix} stats` - Displays bot/server statistics\n"
        )
        await message.channel.send(help_text)

    async def handle_stats(self, message: discord.Message):
        stats_text = (
            "**📊 BumpBot Stats**\n\n"
            f"Servers: {len(self.guilds)}\n"
            f"Users: {len(set(self.users))}\n"
        )
        await message.channel.send(stats_text)

    # === Webhook Logging ===
    async def send_webhook(self, title: str, description: str, color=0x3498db):
        embed = discord.Embed(title=title, description=description, color=color)
        embed.set_footer(text=f"BumpBot • {self.user}", icon_url=self.user.avatar.url if self.user.avatar else None)
        await self.webhook.send(embed=embed, username="BumpBot Logger", avatar_url=self.user.avatar.url if self.user.avatar else None)

# === Bot Creation ===
def create_bot() -> Tuple[discord.Client, str]:
    logger.info("🚀 Starting BumpBot...")
    env = load_env_vars(ENV_KEYS)
    bot = BumpBot(
        channel_id=int(env['CHANNEL_ID']),
        webhook_url=env['LOGS_WEBHOOK'],
        prefix=env['PREFIX']
    )
    return bot, env['BOT_TOKEN']
