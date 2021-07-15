# bot.py
import os

import discord
import textgenerator
#import chat

TOKEN = "Nzk0NjY1MDk4MTE4NjkyODY0.X--Hiw.I34kcWny2NAQx2OJEyH9fIz3_js"

client = discord.Client()

seed = ""

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Game('mk. 3'))

processing = False

#bot = chat.ChatBot()

channel1 = 864591154376867840
channel2 = 865267982098497547

channels = [channel1, channel2]

context = {}
last_input = ""

error_count = 0

context[channel1] = []
context[channel2] = []

@client.event
async def on_message(message):
    global processing
    global seed
    global context
    global last_input
    global error_count
    if message.author == client.user:
        return
    if message.channel.id in channels:
        channel = message.channel
        if not processing:
            try:
                processing = True
                if message.channel == channel:
                    print("recieved input " + "\"" + message.content + "\"")
                    bot_input = textgenerator.generate(context[channel.id], message.content)
                    if bot_input == last_input:
                        context[channel.id] = []
                        bot_input = textgenerator.generate(context[channel.id], message.content)
                    else:
                        last_input = bot_input
                    context[channel.id].append(message.content)
                    context[channel.id].append(bot_input)
                    if len(context[channel.id]) > 50:
                        del(context[channel.id][0])
                    await channel.send(bot_input)
                else:
                    print("recieved input " + "\"" + message.content + "\"")
            except:
                error_count += 1
                if error_count > 3:
                    context[channel.id] = []
                    await channel.send("critical error. resetting memory.")
                    error_count = 0
                else:
                    await channel.send("sorry, I don't know how to respond.")
            processing = False
        else:
            await channel.send("I'm busy, try again in a moment.")
    
    
    #response = message.content
    #seed += (response)
    #seedLen = len(seed)
    #if len(seed) > 200:
    #    print("Tokens full, resetting seed.")
    #    seed = response
    #async with message.channel.typing():
    #    text = textgenerator.generate_text(seed)
    #    index = 0
    #    newText = ""
    #    for i in text:
    #        index += 1
    #        if index > seedLen:
    #            newText += i
    #await message.channel.send(newText)


client.run(TOKEN)
