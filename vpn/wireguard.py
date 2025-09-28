import logging

from utils.userdata import get_user_info
from utils.plans import get_plan_limit


async def generate_peer(user_id: int) -> str:
    """Return sample WireGuard config and store peer count."""

    info = await get_user_info(user_id)
    limit = info.get("device_limit") or get_plan_limit(info.get("plan"))
    peers = info.get("peers", len(info.get("devices", {})))
    if peers >= limit:
        raise RuntimeError(f"Maximum number of peers reached ({limit})")
    logging.info("Generating WireGuard config for %s", user_id)
    config = (
        "[Interface]\n"
        "PrivateKey = YJDzHTVQiU543YR+maWnbFeMlMEScr2T+hJrcAKCoVY=\n"
        "Jc = 1\n"
        "Jmin = 1\n"
        "Jmax = 2\n"
        "S1 = 95\n"
        "S2 = 56\n"
        "H1 = 1385116869\n"
        "H2 = 890833814\n"
        "H3 = 1658880836\n"
        "H4 = 1873597302\n"
        "Address = 11.0.0.19/32\n"
        "DNS = 1.1.1.1, 8.8.8.8\n"
        "MTU = 1420\n\n"
        "[Peer]\n"
        "PublicKey = VoK6Fq0gd6nDKZ4XFwjs0YxOpMNlIoR/RFClzQBC4Dg=\n"
        "AllowedIPs = 0.0.0.0/0\n"
        "Endpoint = 188.253.24.141:51822"
    )
    return config
