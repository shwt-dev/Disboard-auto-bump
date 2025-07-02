import os
import sys
import asyncio
import discord
import logging
from dotenv import load_dotenv
from loguru import logger

env_table = {
    'TOKEN': os.getenv('BOT_TOKEN'),
    'CHANNEL_ID': os.getenv('CHANNEL_ID'),
    "LOG_CHANNEL_ID": os.getenv('LOG_CHANNEL_ID')
}

# Load enviroment variables
load_dotenv()

class BumpBot(discord.Client): 
    def __init__(self):
        super().__init__()

    async def on_ready(self):
        logger.info(f"✅ Logged in as {self.user}")
        self.bump_channel = self.get_channel(int(os.getenv('CHANNEL_ID')))
        self.log_channel = self.get_channel(int(os.getenv('LOG_CHANNEL_ID')))

def create_bot():
    logger.info("Starting BumpBot...")
    for name, value in env_table.items():
        if not value:
            logger.error(f"{name} is not initialized")
            sys.exit(1)
    return BumpBot(), TOKEN
