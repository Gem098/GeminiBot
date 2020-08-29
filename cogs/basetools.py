import asyncio
import json
import discord
from discord.ext import commands


class BaseTools(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # listener Commands
    # packaged Events
    # Event handlers for member join/leave.

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined a server.')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left a server.')

    # Commands start here:
    ##
    # Specify Bot Owner ID

    def is_it_user(ctx):
        return ctx.author.id == 693254186061529129

    # restricts load permissions to everyone except the true bot owner

    @commands.command()
    @commands.check(is_it_user)
    async def pkgload(self, ctx, extension):
        """ can only be used by bot owner! """
        self.bot.load_extension(f'cogs.{extension}')
        await ctx.send('Module loaded!')

    @commands.command()
    @commands.check(is_it_user)
    async def pkgunload(self, ctx, extension):
        """ can only be used by bot owner! """
        self.bot.unload_extension(f'cogs.{extension}')
        await ctx.send('Module unloaded!')

    @commands.command()
    @commands.cooldown(rate=1, per=5.0, type=commands.BucketType.user)
    async def ping(self, ctx):
        """ Get a response with latency from the bot! Cool-down of 3 secs. """
        await ctx.send(f'Pong! Bot latency: {round(self.bot.latency * 1000)}ms')



    @commands.command()
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def basetools(self, ctx):
        """ BaseTools Package Information Command. """
        await ctx.send('``Package: BaseTools Version:1.0.1 is loaded!``')
        await ctx.send('``About PKG: Supplies GeminiBot users Base Functionality for the Bot.``')
        await ctx.send('``This package is required to enable basic functionality!``')
        await ctx.send('``This package hosts (2) of the audit event listeners. ``')
        await ctx.send('``This package hosts (7) commands.``')
        await ctx.send('``Package Author: Gemini#0324``')

    @commands.command(aliases=['changeprefix'])
    @commands.has_permissions(administrator=True)
    async def setprefix(self, ctx, prefix):
        """ Change GeminiBot's Prefix for your server. """
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)
        await ctx.send(f'server bot prefix changed to {prefix}')

    @setprefix.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specify all required arguments!')

    @commands.command()
    async def botinfo(self, ctx):
        """ Get information on GeminiBot's Version and Edition. """
        await ctx.send(' ```Hi There! GeminiBot is currently in version (1.0.1)``` ')
        await ctx.send(' ```Package support is currently enabled!``` ')
        await ctx.send(' ```GeminiBot Version:(1.0.1).``` ')


def setup(bot):
    bot.add_cog(BaseTools(bot))

