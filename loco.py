import discord
from discord.ext import commands
# from itertools import cycle
import asyncio
import time
prefix = ""
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')
BOT_OWNER_ROLE="🔥RUNNER🔥" #change which role you need
BOT_OWNER_ROLE_ID= "617694958882914305"



@bot.event
async def on_ready():
    print('Online')
    print(bot.user.name)
    print("Everything's all ready to go~")
    while True:
    	await bot.change_presence(activity=discord.Activity(type=1,name="with 🔥FIRE TRIVIA🔥"))
    	await asyncio.sleep(1)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with PUBG FAN#6219"))
    	await asyncio.sleep(1)
        
      

                
                


                 
                
                

                
@bot.command(name=".q1",hidden=True)
async def suggestion(ctx):
                await ctx.send("@everyone Question 1️⃣ Coming on your Mobile 📱")
        
@bot.command(name=".q2",hidden=True)
async def suggestion(ctx):
                await ctx.send("@everyone Question 2️⃣ Coming on your Mobile 📱")
        
@bot.command(name=".q3",hidden=True)
async def suggestion(ctx):
                await ctx.send("@everyone Question 3️⃣ Coming on your Mobile 📱")
        
@bot.command(name=".q4",hidden=True)
async def suggestion(ctx):
                await ctx.send("@everyone Question 4️⃣ Coming on your Mobile 📱")
        
@bot.command(name=".q5",hiddn=True)
async def suggestion(ctx):
                await ctx.send("@everyone Question 5️⃣ Coming on your Mobile 📱")
        
@bot.command(name=".q6",hidden=True)
async def suggestion(ctx):
                await ctx.send("@everyone Question 6️⃣ Coming on your Mobile 📱")
        
@bot.command(name=".q7",hidden=True)
async def suggestion(ctx):
                await ctx.send("@everyone Question 7️⃣ Coming on your Mobile 📱")
        
@bot.command(name=".q8",hidden=True)
async def suggestion(ctx):
                await ctx.send("@everyone Question 8️⃣ Coming on your Mobile 📱")
        
@bot.command(name=".q9",hidden=True)
async def suggestion(ctx):
                await ctx.send("@everyone Question 9️⃣ Coming on your Mobile 📱")
        
@bot.command(name=".q10",hidden=True)
async def suggestion(ctx):
                await ctx.send("@everyone Question 🔟 Coming on your Mobile 📱")
        
@bot.command(name=".q11",hidden=True)
async def suggestion(ctx):
                await ctx.send("@everyone Question 11 Coming on your Mobile 📱")
        
@bot.command(name=".q12",hidden=True)
async def suggestion(ctx):
                await ctx.send("@everyone Question 12 Coming on your Mobile 📱")
                
                
bot.run('NzA0MjM2MDcxNzQ3MDU5Nzky.Xs5OKg.GjuWh9X40JOOAtrJAsX9LulsvYs',bot=False)          
                
                
