from dataclasses import dataclass


@dataclass(frozen=True)
class PlanConfig:
    title_key: str
    device_limit: int


_PLAN_DEFAULT_KEY = "trial"
_PLAN_CONFIGS: dict[str, PlanConfig] = {
    "trial": PlanConfig(title_key="plan_title_trial", device_limit=2),
    "device2": PlanConfig(title_key="plan_title_device2", device_limit=2),
    "device5": PlanConfig(title_key="plan_title_device5", device_limit=5),
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


def get_plan_title_key(plan: str | None) -> str:
    return get_plan_config(plan).title_key


def get_plan_title(plan: str | None, locale: str | None = None) -> str:
    from utils.texts import t

    return t(get_plan_title_key(plan), locale)


def get_plan_limit(plan: str | None) -> int:
    return get_plan_config(plan).device_limit
