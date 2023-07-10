from twitchio.ext import commands
import pyautogui
import asyncio
import pyperclip


bot = commands.Bot(
    token='oauth:glakxo2aomnw5ze7e1nnvxgtnz3vca',
    client_id='kvhvcuajb6clf2d6gm0a9wlc4pjtbz',
    nick='Mortseb',
    prefix='!',
    initial_channels=['Domingo']
)

clip_in_progress = False

async def create_clip(ctx):
    global clip_in_progress
    pyautogui.moveTo(2710, 1444)
    await asyncio.sleep(0.5)
    pyautogui.click()
    await asyncio.sleep(3)
    while True:
        if pyautogui.locateOnScreen('clipbar.png') is not None: 
            break  
        await asyncio.sleep(1)
    await asyncio.sleep(0.5)
    pyautogui.moveTo(974, 1481)
    pyautogui.click()
    channel_name = "Domingo"
    user_name = ctx.author.name
    pyautogui.typewrite(f"{channel_name} clip par {user_name}")
    await asyncio.sleep(0.5)

    pyautogui.moveTo(2190, 1312)
    pyautogui.mouseDown()
    await asyncio.sleep(0.5)
    pyautogui.moveTo(1690, 1312)
    pyautogui.mouseUp()
    await asyncio.sleep(0.5)
    pyautogui.moveTo(1728, 1312)
    await asyncio.sleep(0.5)
    pyautogui.mouseDown()
    await asyncio.sleep(0.5)
    pyautogui.moveTo(2314, 1312)
    pyautogui.mouseUp()
    pyautogui.moveTo(2139, 1580)
    pyautogui.click()
    while True:
        if pyautogui.locateOnScreen('cliplink.png') is not None: 
            break  
        await asyncio.sleep(1)
    pyautogui.moveTo(1239, 1175)
    pyautogui.click()
    await asyncio.sleep(0.5)
    pyautogui.moveTo(940, 33)
    pyautogui.click()
    await asyncio.sleep(1)
    clip_link = pyperclip.paste()
    message = f"Clip demandé par {ctx.author.name}: {clip_link}"
    await ctx.send(message)
    clip_in_progress = False
    
    

@bot.command(name='clip')
async def clip(ctx):
    global clip_in_progress
    if clip_in_progress:
        await asyncio.sleep(0.5)
    else:
        clip_in_progress = True
        bot.loop.create_task(create_clip(ctx))

if __name__ == "__main__":
    bot.run()
