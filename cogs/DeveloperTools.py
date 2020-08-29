import time
import discord
from discord.ext import commands


class DevUtils(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def is_it_user(ctx):
        return ctx.author.id == 693254186061529129

    @commands.command()
    @commands.check(is_it_user)
    async def probenet(self, ctx):
        """ Displays issuing user with advanced network conditions. """
        before = time.monotonic()
        before_ws = int(round(self.bot.latency * 1000, 1))
        message = await ctx.send("🏓 Pong")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"🏓 WebSocket: {before_ws}ms  |  REST (ping): {int(ping)}ms")

    @commands.command()
    @commands.check(is_it_user)
    async def probeguilds(self, ctx):
        """ Generates a list of all joined guilds by the bot. """
        avgmembers = round(len(self.bot.users) / len(self.bot.guilds))
        await ctx.send(f"Total Servers: {len(ctx.bot.guilds)} ( avg member count: {avgmembers} users/server) ")

    @commands.command()
    @commands.check(is_it_user)
    async def probejoin(self, ctx):
        """ Generates an OAuth Invite link for the current bot. """
        await ctx.send(
            f"**{ctx.author.name}**, use this URL to invite me\n<{discord.utils.oauth_url(self.bot.user.id)}>")


def setup(bot):
    bot.add_cog(DevUtils(bot))

