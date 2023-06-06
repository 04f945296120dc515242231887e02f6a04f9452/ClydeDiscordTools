import discord


async def ban_user(user: discord.User, guild: discord.Guild, reason=None):
    """
    Ban a user from a Discord server.
    """
    try:
        await guild.ban(user, reason=reason)
        return f'{user.name}#{user.discriminator} has been banned from the server.'
    except discord.errors.Forbidden:
        return 'I do not have the necessary permissions to ban this user.'
