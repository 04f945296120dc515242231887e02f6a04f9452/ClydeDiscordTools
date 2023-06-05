import discord


async def ignore_user(message: discord.Message, ignored_users: list):
    """
    Check if a user is in the ignored_users list and ignore their message if so.
    """
    if message.author.id in ignored_users:
        return True
    return False
