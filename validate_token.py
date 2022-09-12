from requests import get, post
from random import randint

def validate(tokens: list) -> list:
    """Validate a list of tokens (user or bot)"""
    if len(tokens):  # Only a single token is being checked
        res = get('https://discord.com/api/v9/auth/login', headers={"Authorization": tokens[0]})  # Bad for mass token check due to the rate limit
        return tokens if res.status_code == 200 else []  # If login request succeed just return the passed list
    valid_tokens = []
    for token in tokens:
        res = post(f'https://discord.com/api/v9/invite/{randint(1,1000)}', headers={'Authorization': token})  # Just try to create an invite
        if "401: Unauthorized" in str(res.content) : pass  # Doesn't check for a "verify account" error
        else                                       : valid_tokens.append(token)
    return valid_tokens

print(validate(["TOKEN1", "1234"]))
