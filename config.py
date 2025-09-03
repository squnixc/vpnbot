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
    admin_ids: List[int]

    @property
    def ADMIN_IDS(self) -> List[int]:
        """Backward compatibility for existing code using uppercase name."""
        return self.admin_ids


config = Config(
    bot_token=os.getenv("BOT_TOKEN", ""),
    provider_token=os.getenv("PROVIDER_TOKEN", ""),
    webhook_url=os.getenv("WEBHOOK_URL", ""),
    admin_ids=[int(x) for x in os.getenv("ADMIN_IDS", "326634923").split(",") if x],
)
