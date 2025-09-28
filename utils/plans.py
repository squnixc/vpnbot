"""Plan configuration helpers."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PlanConfig:
    title: str
    device_limit: int


_PLAN_DEFAULT_KEY = "trial"
_PLAN_CONFIGS: dict[str, PlanConfig] = {
    "trial": PlanConfig(title="Бесплатный период", device_limit=2),
    "device2": PlanConfig(title="2 устройств(-а)", device_limit=2),
    "device5": PlanConfig(title="5 устройств(-а)", device_limit=5),
}


def normalise_plan(plan: str | None) -> str:
    """Return a known plan key, falling back to default."""

    if plan and plan in _PLAN_CONFIGS:
        return plan
    return _PLAN_DEFAULT_KEY


def get_plan_config(plan: str | None) -> PlanConfig:
    """Return configuration for the given plan."""

    key = normalise_plan(plan)
    return _PLAN_CONFIGS[key]


def get_plan_title(plan: str | None) -> str:
    return get_plan_config(plan).title


def get_plan_limit(plan: str | None) -> int:
    return get_plan_config(plan).device_limit
