import os
from dataclasses import dataclass
from typing import List
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    bot_token: str
    provider_token: str
    webhook_url: str
    ADMIN_IDS: List[int]


config = Config(
    bot_token=os.getenv("BOT_TOKEN", ""),
    provider_token=os.getenv("PROVIDER_TOKEN", ""),
    webhook_url=os.getenv("WEBHOOK_URL", ""),
    ADMIN_IDS=[int(x) for x in os.getenv("ADMIN_IDS", "326634923").split(",") if x],
)
