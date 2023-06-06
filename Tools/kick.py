import discord


async def kick_user(user: discord.Member, guild: discord.Guild, reason=None):
    """
    Kick a user from a Discord server.
    """
    try:
        await user.kick(reason=reason)
        return f'{user.name}#{user.discriminator} has been kicked from the server.'
    except discord.errors.Forbidden:
        return 'I do not have the necessary permissions to kick this user.'
