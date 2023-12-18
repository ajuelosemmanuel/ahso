import discord, re

intents = discord.Intents.default()
intents.message_content = True

TOKEN = ""  # Replace this with your Discord token

REGEX_LINK = r"(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])"

class Ahso(discord.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}')

bot = Ahso(intents=intents)

@bot.slash_command(description="Be sorry")
async def ahsosorry(ctx):
    await ctx.respond(content = "ah! so sorry!", file = discord.File(fp = "media/ahsosorry.webp"))

@bot.slash_command(description="Be jolly")
async def ahsojolly(ctx):
    await ctx.respond(content = "ah! so jolly!", file = discord.File(fp = "media/ahsojolly.jpg"))

@bot.slash_command(description="Be happy")
async def ahsohappy(ctx):
    await ctx.respond(content = "ah! so happy!", file = discord.File(fp = "media/ahsohappy.jpg"))

@bot.event
async def on_message(message):
    msg = message.content
    dic = {
        "twitter.com":"fxtwitter.com",
        "www.twitter.com":"fxtwitter.com",
        "x.com":"fxtwitter.com",
        "www.x.com":"fxtwitter.com",
        "instagram.com":"ddinstagram.com",
        "www.instagram.com":"ddinstagram.com"
    }
    matches = re.findall(REGEX_LINK, msg)
    if len(matches) == 0:
        return
    for el in matches:
        if el[1] in dic and (("/p/" in el[2]) or ("/reel/" in el[2]) or ("/status/" in el[2])):
            await message.channel.send(content = f"{message.author.mention} sent the following link : {el[0]}://{dic[el[1]]}{el[2]}")
            if msg == el[0] + "://" + el[1] + el[2] :
                await message.delete()
    
bot.run(TOKEN)