from typing import Text
import discord
from discord import message
from discord.colour import Color
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands.converter import Converter, Greedy
import random



settings = { 'token': 'NzA0NjM4OTUwODM2NDA0MjI0.XqgEKQ.NLVGDAq3AKNbuHjR2vi3E-RcL1w','bot': 'SCP - 173','id': 704638950836404224 ,'prefix': '.'}

loopEnabled = False
MessageForLoop = ""

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def hello(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'Hello, {author.mention}!') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.



@bot.command()
async def say(ctx, arg1, *therest):
     message = ""
   
     message = arg1 + " "
   
     Table = list(therest)
     for word in Table:
        message = message + (" " + str(word))

     await ctx.send(message)

@bot.command()
async def math(ctx, number1, symbol, number2):
        author = ctx.author
        result = 0
        number1 = float(number1)
        number2 = float(number2)
        if symbol == "+":
            result = number1 + number2
        elif symbol == "-":
         result = number1 - number2
        elif symbol == "*":
          result = number1 * number2
        elif symbol == "/":
           result = number1 / number2
        elif symbol == "^":
          result = number1 ^ number2
        data = int(result)
        
        if result - 0.01 < data:
            result = data
        else:
            result = result 
    
        await ctx.send(result)

@bot.command()
async def snap(ctx):
        author = ctx.message.author
        message1 = f"{author.mention} Snap! Snap!"
        message2 = f"{author.mention} was snapped..."
        messageEnd = ""
        chance = random.randint(1,10)
        if chance <= 5:
             messageEnd = message1
        else:
            messageEnd = message2
        await ctx.send(messageEnd)

  
@bot.command()
async def StartLoop(ctx, *therest):
    message = ""
    Table = list(therest)
    for word in Table:
        if message == "":
            message = message + str(word)
        else:
          message = message + (" " + str(word))
    
    loopEnabled = True
    while loopEnabled:
        await ctx.send(message)
    

@bot.command()
async def DisableLoop(ctx):
    loopEnabled = False
    loopEnabled = loopEnabled
    await ctx.send(f"{ctx.message.author}, spam disabled!")


bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения токена