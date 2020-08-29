import discord
import random
import secrets
from discord.ext import commands


class FunPack(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        # packaged Events
        # None

        # checks status of FunPack
    @commands.command()
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def funpack(self, ctx):
        """ FunPack Package Information Command. """
        await ctx.send('``Package: FunPack Version:1.0.0 is loaded!``')
        await ctx.send('``About PKG: supplies GeminiBot users with some fun commands.``')
        await ctx.send('``This package is not required. To have it removed, contact a GeminiBot Developer.``')
        await ctx.send('``This package hosts (0) event listeners.``')
        await ctx.send('``This package hosts (14) commands, each with 3 second cool-downs.``')
        await ctx.send('``Package Author: Gemini#0324``')

    # commands below.
    @commands.command(aliases=['8ball'])
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def eightball(self, ctx, *, question):
        """ Shakes an 8Ball. """
        responses = ["It is certain.",
                     "It is decidedly so.",
                     "Without a doubt.",
                     "Yes - definitely.",
                     "You may rely on it.",
                     "As I see it, yes.",
                     "Most likely.",
                     "Outlook good.",
                     "Yes.",
                     "Signs point to yes.",
                     "Reply hazy, try again.",
                     "Ask again later.",
                     "Better not tell you now.",
                     "Cannot predict now.",
                     "Concentrate and ask again.",
                     "Don't count on it.",
                     "My reply is no.",
                     "No",
                     "My sources say no.",
                     "Outlook not so good.",
                     "Stfu",
                     "Very doubtful."]

        await ctx.send(f'Question: {question}\n 🎱 Answer: {random.choice(responses)}')

    # goodnight
    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def goodnight(self, ctx):
        """ Tells you goodnight when nobody else does! """
        await ctx.channel.purge(limit=1)
        await ctx.send('Goodnight {0.display_name}!'.format(ctx.author))

    # good morning
    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def goodmorning(self, ctx):
        """ Tells you good morning when nobody else does! """
        await ctx.channel.purge(limit=1)
        await ctx.send('Good morning {0.display_name}!'.format(ctx.author))

    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def geminismentalstatus(self, ctx):
        """ Command for Gemini """
        await ctx.channel.purge(limit=0)
        await ctx.send('``He is on his way to commit suicide``!'.format(ctx.author))

    # didnt ask
    @commands.command(pass_context=True, aliases=['didnotask'])
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def didntask(self, ctx):
        """ But did i ask? """
        await ctx.channel.purge(limit=1)
        await ctx.send('Damn {0.display_name}, I didn\'t ask either.'.format(ctx.author))

    # nice
    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def nice(self, ctx):
        """ Prompts user with a pretty nice message. """
        await ctx.channel.purge(limit=1)
        await ctx.send('nice {0.display_name}'.format(ctx.author))
        await ctx.send('69 420')

    # dice
    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def dice(self, ctx):
        """ Rolls a 6 sided dice. """
        await ctx.channel.purge(limit=1)
        await ctx.send('Your dice roll {0.display_name}:'.format(ctx.author))
        await ctx.trigger_typing()
        await ctx.send((random.choice(["one", "two", "three", "four", "five", "six", ])))

    @commands.command(aliases=['flip', 'coin'])
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def coinflip(self, ctx):
        """ Flips a coin. """
        await ctx.channel.purge(limit=1)
        coinsides = ['Heads', 'Tails']
        await ctx.send(f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinsides)}**!")

    @commands.command()
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def f(self, ctx, *, text: commands.clean_content = None):
        """ Press F to pay respect. """
        hearts = ['❤', '💛', '💚', '💙', '💜']
        reason = f"for **{text}** " if text else ""
        await ctx.channel.purge(limit=1)
        await ctx.send(f"**{ctx.author.name}** has paid their respect {reason}{random.choice(hearts)}")

    @commands.command()
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def reverse(self, ctx, *, text: str):
        """ !ffuts esreveR
        Everything after the word reverse will be reversified!
        """
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        await ctx.send(f"🔁 {t_rev}")

    @commands.command()
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def password(self, ctx, nbytes: int = 18):
        """ Generates a random password string and sends to you via DM!
        This returns a random URL-safe text string, containing random bytes.
        The text is Base64 encoded, so on average each byte results in approximately 1.3 characters.
        """
        if nbytes not in range(3, 1401):
            return await ctx.send("I only accept any numbers between 3-1400")
        if hasattr(ctx, 'guild') and ctx.guild is not None:
            await ctx.send(f"Sending you a private message with your random generated password **{ctx.author.name}**")
        await ctx.author.send(f"🎁 **Here is your password:**\n{secrets.token_urlsafe(nbytes)}")

    @commands.command()
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def rate(self, ctx, *, thing: commands.clean_content):
        """ Rates whatever you desire to be rated. """
        rate_amount = random.uniform(0.0, 100.0)
        await ctx.send(f"I'd rate `{thing}` a **{round(rate_amount, 4)} / 100**")

    @commands.command(aliases=['howhot', 'hot'])
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def hotcalc(self, ctx, *, user: discord.Member = None):
        """ Returns a random percentage value for how hot a discord user is."""
        user = user or ctx.author

        random.seed(user.id)
        r = random.randint(1, 100)
        hot = r / 1.17

        emoji = "💔"
        if hot > 25:
            emoji = "❤"
        if hot > 50:
            emoji = "💖"
        if hot > 75:
            emoji = "💞"

        await ctx.send(f"**{user.name}** is **{hot:.2f}%** hot {emoji}")

    @commands.command(aliases=['slots', 'bet'])
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def slot(self, ctx):
        """ A discord slot machine!!! """
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

        if (a == b == c):
            await ctx.send(f"{slotmachine} All matching, you won! 🎉")
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(f"{slotmachine} 2 in a row, you won! 🎉")
        else:
            await ctx.send(f"{slotmachine} No match, you lost 😢")


def setup(bot):
    bot.add_cog(FunPack(bot))


