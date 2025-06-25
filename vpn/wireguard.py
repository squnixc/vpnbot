import logging


def generate_peer(user_id: int) -> str:
    """Generate mock WireGuard config for given user."""
    logging.info("Generating WireGuard config for %s", user_id)
    config = (
        "[Interface]\n"
        f"PrivateKey = PRIVATE_KEY_{user_id}\n"
        "Address = 10.0.0.2/32\n\n"
        "[Peer]\n"
        "PublicKey = SERVER_PUBLIC_KEY\n"
        "Endpoint = vpn.example.com:51820\n"
        "AllowedIPs = 0.0.0.0/0"
    )
    return config
