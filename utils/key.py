import secrets


def key(size=256):
    print(secrets.token_hex(size))
