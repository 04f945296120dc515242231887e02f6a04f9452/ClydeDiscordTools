import discord


class User:
    """
    A class representing a Discord user.
    """
    def __init__(self, user_id, username, discriminator, avatar_url=None):
        self.id = user_id
        self.username = username
        self.discriminator = discriminator
        self.avatar_url = avatar_url

    @classmethod
    async def from_member(cls, member: discord.Member):
        """
        Create a User object from a Discord Member object.
        """
        return cls(
            member.id,
            member.name,
            member.discriminator,
            str(member.avatar_url_as(format='png'))
        )

    @classmethod
    async def from_user(cls, user: discord.User):
        """
        Create a User object from a Discord User object.
        """
        return cls(
            user.id,
            user.name,
            user.discriminator,
            str(user.avatar_url_as(format='png'))
        )

    def __str__(self):
        """
        Get a string representation of the User object.
        """
        return f'{self.username}#{self.discriminator} ({self.id})'
