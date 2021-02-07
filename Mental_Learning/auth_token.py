import secrets

def auth_token_generator():
    return secrets.token_hex(20)