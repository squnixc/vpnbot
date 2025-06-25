import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    bot_token: str
    provider_token: str
    webhook_url: str


config = Config(
    bot_token=os.getenv("BOT_TOKEN", ""),
    provider_token=os.getenv("PROVIDER_TOKEN", ""),
    webhook_url=os.getenv("WEBHOOK_URL", ""),
)
