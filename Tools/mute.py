import discord


async def mute_user(user: discord.Member, guild: discord.Guild, mute_role_name: str, reason=None):
    """
    Mute a user in a Discord server by assigning the mute role.
    """
    # Get the mute role from the server
    mute_role = discord.utils.get(guild.roles, name=mute_role_name)

    # Check if the mute role exists
    if mute_role is None:
        return f'{mute_role_name} role not found on the server.'

    # Assign the mute role to the user
    try:
        await user.add_roles(mute_role, reason=reason)
        return f'{user.name}#{user.discriminator} has been muted on the server.'
    except discord.errors.Forbidden:
        return 'I do not have the necessary permissions to mute this user.'
