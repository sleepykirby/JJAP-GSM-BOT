import asyncio
import discord
import json
import operator
import os
import re
import time
#import youtube_dl
from datetime import datetime
from functools import partial
from discord import User
from discord.ext import commands

token = "NTU4MTEzMzQ5NDczNDAyODgz.XKvVqQ.zpxrsvOYSzvoMShFSv49Ya92QU4"



def mapping_state_to_message(status):
    if status == discord.Status.online:
        return "온라인"
    elif status == discord.Status.offline:
        return "오프라인"
    elif status == discord.Status.idle:
        return "자리비움"
    elif status == discord.Status.do_not_disturb:
        return "다른 용무중"

class JGB(discord.Client):
    def __init__(self):

        if not os.path.exists("keyword"):
            os.makedirs("keyword")

        self.commands = [i.split("command_")[-1] for i in list(
            filter(lambda param: param.startswith("command_"), dir(self)))]
        
        self.commandDocs = "".join(["***%s***\n%s\n" %
            (i.split("_")[-1], (getattr(self, "command_%s" % i).__doc__).strip()) for i in self.commands])
        
        self.prefix="cmd"

        self.DESCRIPTION_MESSAGE='JJAP GSM BOT'
        super().__init__()
    
    async def on_ready(self):
        print("Logged in as ")
        print(self.user.name)
        print(self.user.id)
        print("===========")
        await self.change_presence(activity=discord.Game("!help"),status=discord.Status.idle,afk=False)

    async def on_message(self,message):
        await self.wait_until_ready

        if not message.author.bot:
            command=message.content.lower()
            if not command.startswith(self.prefix):
                if command.startswith('!help'):
                    await message.channel
                else:
                    return


    async def command_list(self,message):
        # await self.send_typing(message.channel)
        box=discord.Embed(title="JJAP GSM BOT",description=self.DESCRIPTION_MESSAGE,colour=0x7ACDF4)
        box.add_field(name="명령어 목록",value=self.commandDocs)
        box.set_thumbnail(url="https://i.imgur.com/AGW0xxV.png")
        #await self.send_message(message.channel,embed=box)
        await message.channel.send(embed=box)







JGB.run(token)