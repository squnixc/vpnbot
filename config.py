import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    bot_token: str
    provider_token: str
    webhook_url: str
    admin_id: int
    admin_key: str


config = Config(
    bot_token=os.getenv("BOT_TOKEN", ""),
    provider_token=os.getenv("PROVIDER_TOKEN", ""),
    webhook_url=os.getenv("WEBHOOK_URL", ""),
    admin_id=int(os.getenv("ADMIN_ID", "0")),
    admin_key=os.getenv("ADMIN_KEY", "secret"),
)
