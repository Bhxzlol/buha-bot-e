import discord
import asyncio

client = discord.Client()

token = "ODc4MDYyMTA4MTQ5OTQ0Mzky.YR7tEA.lw6pz2rs_LoMESnZQXymgzlh_Ww"

@client.event
async def on_ready():
   print(client.user.name)
   print('성공적으로 봇이 시작되었습니다.')
   game = discord.Game('파랑이 하이')
   await client.change_presence(status=discord.Status.online, activity=game)
      

@client.event
async def on_message(message):
    if message.content == "부하야":
        await message.channel.send("넵 부르셨습니까")
    if message.content == "선풍기 깨워":
        await message.channel.send("알겠습니다")
        await message.channel.send("@선풍기")
        await message.channel.send("@선풍기")
        await message.channel.send("@선풍기")
        await message.channel.send("@선풍기")
        await message.channel.send("@선풍기")
    if message.content == "안녕 부하":
        await message.channel.send("안녕하세요")
    if message.content == "오늘 기분이 어때?":
        await message.channel.send("좋아요! :D")
    if message.content == "나 이제 끌게":
        await message.channel.send("안녕히 가세요 ^^")
    if message.content == "나 밥 먹고 올게":
        await message.channel.send("맛있게 드세요")
    if message.content == "!타자 시작":
        await message.channel.send("주인님 파이팅")



client.run(token)
