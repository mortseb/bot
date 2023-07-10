from twitchio.ext import commands
import random
import asyncio
import pyautogui

# Création d'une liste pour stocker les commandes en attente
command_queue = []
priority_queue = []

bot = commands.Bot(
    token='oauth:XXXXXXXXXXXXXXXXXXXXXXXXX',
    client_id='XXXXXXXXXXXXXXXXX',
    nick='XXXXXXXXXXXX',
    prefix='!',
    initial_channels=['XXXXXXXXX']
)



async def subscriber_action(club_name):
    pyautogui.moveTo(1057, 64)
    pyautogui.click()
    await asyncio.sleep(2)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.typewrite(club_name)
    await asyncio.sleep(5)
    pyautogui.moveTo(923, 179)
    pyautogui.click()
    await asyncio.sleep(2)
    pyautogui.moveTo(2022, 62)
    pyautogui.click()
    await asyncio.sleep(2)
    pyautogui.moveTo(2059, 142)
    pyautogui.click()
    await asyncio.sleep(2)
    pyautogui.moveTo(806, 435)
    pyautogui.click()
    await asyncio.sleep(2)
    pyautogui.moveTo(798, 508)
    pyautogui.click()
    await asyncio.sleep(2)
    pyautogui.moveTo(888, 1348)
    pyautogui.click()
    await asyncio.sleep(2)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.typewrite("5000000")
    pyautogui.moveTo(876, 694)
    pyautogui.click()
    await asyncio.sleep(2)
    pass

async def cheer_action(club_name, bits):
    money_earned = bits * 30000
    pyautogui.moveTo(1057, 64)
    pyautogui.click()
    await asyncio.sleep(2)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.typewrite(club_name)
    await asyncio.sleep(5)
    pyautogui.moveTo(923, 179)
    pyautogui.click()
    await asyncio.sleep(2)
    pyautogui.moveTo(2022, 62)
    pyautogui.click()
    await asyncio.sleep(2)
    pyautogui.moveTo(2059, 142)
    pyautogui.click()
    await asyncio.sleep(2)
    pyautogui.moveTo(806, 435)
    pyautogui.click()
    await asyncio.sleep(2)
    pyautogui.moveTo(798, 508)
    pyautogui.click()
    await asyncio.sleep(2)
    pyautogui.moveTo(888, 1348)
    pyautogui.click()
    await asyncio.sleep(2)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.typewrite(str(money_earned))
    pyautogui.moveTo(876, 694)
    pyautogui.click()
    await asyncio.sleep(2)
    pass

@bot.event
async def event_subscription(ctx):
    club_name = ctx.content
    priority_queue.append((subscriber_action, [club_name]))
    await ctx.send(f"Thank You ! You just earned € 5.000.000 for '{club_name}'.")

@bot.event
async def event_cheer(ctx):
    club_name = ctx.content
    bits = ctx.bits
    priority_queue.append((cheer_action, [club_name, bits]))
    await ctx.send(f"Thank you for your donation of {bits} bits! You just earned €{bits * 30000} for '{club_name}'.")

async def execute_create(first_name:str, last_name:str, country:str):
        print("Starting create command execution.")
        pyautogui.moveTo(139, 192)
        pyautogui.click()
        await asyncio.sleep(2)
        pyautogui.moveTo(708, 716)
        pyautogui.click(button='right')
        await asyncio.sleep(2)
        pyautogui.moveTo(832, 813)
        await asyncio.sleep(2)
        pyautogui.moveTo(1170, 829)
        pyautogui.click()
        await asyncio.sleep(2)
        pyautogui.moveTo(708, 716)
        pyautogui.click()
        await asyncio.sleep(2)
        pyautogui.moveTo(2023, 67)
        pyautogui.click()
        await asyncio.sleep(2)
        pyautogui.moveTo(2158, 612)
        pyautogui.click()
        await asyncio.sleep(2)
        pyautogui.moveTo(1400, 604)
        pyautogui.click()
        await asyncio.sleep(2)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        random_number = random.randint(150, 200)  # Générer un nombre aléatoire entre 150 et 200
        pyautogui.write(str(random_number))  # Convertir le nombre aléatoire en string et écrire
        pyautogui.moveTo(2245, 1417)
        pyautogui.click()
        await asyncio.sleep(2)
        pyautogui.moveTo(2018, 57)
        pyautogui.click()
        await asyncio.sleep(2)
        pyautogui.moveTo(2214, 667)
        pyautogui.click()
        await asyncio.sleep(2)
        pyautogui.moveTo(1489, 499)
        pyautogui.click()
        await asyncio.sleep(2)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        pyautogui.typewrite(first_name)
        pyautogui.moveTo(1395, 561)
        pyautogui.click()
        await asyncio.sleep(2)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        pyautogui.typewrite(last_name)
        pyautogui.moveTo(1403, 630)
        pyautogui.click()
        await asyncio.sleep(2)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        pyautogui.typewrite(first_name + ' ' + last_name) 
        pyautogui.moveTo(2249, 1422)
        pyautogui.click()
        await asyncio.sleep(2)
        pyautogui.moveTo(2023, 73)
        pyautogui.click()
        await asyncio.sleep(2)
        pyautogui.moveTo(2051, 144)
        pyautogui.click()
        await asyncio.sleep(2)
        pyautogui.moveTo(778, 261)
        pyautogui.click()
        await asyncio.sleep(2)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        pyautogui.typewrite(country)
        pyautogui.press('enter')
        await asyncio.sleep(2)
        pyautogui.moveTo(1831, 1305)
        pyautogui.click()
        await asyncio.sleep(2)
        pyautogui.moveTo(2021, 59)
        pyautogui.click()
        await asyncio.sleep(2)
        pyautogui.moveTo(2052, 137)
        pyautogui.click()
        await asyncio.sleep(2)
        print("Create command execution completed.")
        pyautogui.moveTo(139, 192)
        pyautogui.click()
        await asyncio.sleep(2)
        pyautogui.moveTo(826, 155)
        pyautogui.click()
        await asyncio.sleep(5)

async def execute_save():
    print("Starting save command execution.")
    pyautogui.moveTo(2226, 61)
    pyautogui.click()
    await asyncio.sleep(2)
    pyautogui.moveTo(2261, 139)
    pyautogui.click()
    await asyncio.sleep(2)
    print("Save command execution completed.")
    await asyncio.sleep(3)
    while True:
        if pyautogui.locateOnScreen('save.png') is None:  # L'image n'est plus trouvée
            break  # Si l'image n'est plus trouvée, sortez de la boucle
        await asyncio.sleep(2)  # Utilisez asyncio.sleep au lieu de time.sleep dans une coroutine
    await asyncio.sleep(2)

async def execute_shortlist():
    pyautogui.moveTo(173, 186)
    pyautogui.click()
    await asyncio.sleep(2)
    pyautogui.moveTo(832, 157)
    pyautogui.click()
    await asyncio.sleep(2)

@bot.command(name='shortlist')
async def shortlist(ctx):
        command_queue.append((execute_shortlist, []))
        await ctx.send("Command 'shortlist' has been added to the queue.")
@bot.command(name='save')
async def save(ctx):
    command_queue.append((execute_save, []))
    await ctx.send(f"Command 'save' has been added to the queue.")


async def execute_search(text:str):
        print("Starting search command execution.")
        pyautogui.moveTo(1057, 64)
        pyautogui.click()
        await asyncio.sleep(2)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        pyautogui.typewrite(text)
        await asyncio.sleep(2)
        pyautogui.press('enter')
        await asyncio.sleep(2)
        pyautogui.moveTo(466, 466)
        pyautogui.click()
        await asyncio.sleep(15)
        print("Search command execution completed.")        

async def execute_continue():
    pyautogui.moveTo(114, 43)
    pyautogui.click()
    await asyncio.sleep(2)
    pyautogui.moveTo(575, 170)
    await asyncio.sleep(0.5)
    pyautogui.moveTo(575, 349)
    pyautogui.click()
    await asyncio.sleep(2)
    pyautogui.moveTo(927, 1263)
    pyautogui.click()
    await asyncio.sleep(2)
    pyautogui.moveTo(1679, 1256)
    pyautogui.click()
    await asyncio.sleep(2)
    pyautogui.moveTo(1623, 1327)
    pyautogui.click()
    await asyncio.sleep(2)
    pyautogui.moveTo(1715, 1402)
    pyautogui.click()
    pyautogui.moveTo(113, 33)
    await asyncio.sleep(3)
    while True:
        if pyautogui.locateOnScreen('element.png') is None:  # L'image n'est plus trouvée
            break  # Si l'image n'est plus trouvée, sortez de la boucle
        await asyncio.sleep(2)  # Utilisez asyncio.sleep au lieu de time.sleep dans une coroutine
    await asyncio.sleep(2)

@bot.command(name='create')
async def create(ctx, first_name:str, last_name:str, country:str):
    command_queue.append((execute_create, [first_name, last_name, country]))
    await ctx.send(f"Command 'create' has been added to the queue.")

@bot.command(name='search')
async def search(ctx, *, text:str):
    command_queue.append((execute_search, [text]))
    await ctx.send(f"Command 'search' has been added to the queue.")

@bot.command(name='continue')
async def continue_cmd(ctx):
    command_queue.append((execute_continue, []))
    await ctx.send(f"Command 'continue' has been added to the queue.")

# Variable globale pour indiquer si le bot doit être arrêté
stop_bot = False

@bot.command(name='stop')
async def stop(ctx):
    allowed_users = ["Mortseb", "Mortsebkha"]  # Remplacez par vos véritables noms d'utilisateur Twitch
    if str(ctx.author.name.lower()) in map(str.lower, allowed_users):
        global stop_bot
        stop_bot = True
        await ctx.send("Bot is shutting down...")
    else:
        await ctx.send("You do not have permission to stop the bot.")

async def check_queue():
    global stop_bot
    while not stop_bot:
        if priority_queue:
            cmd, args = priority_queue.pop(0)
            await cmd(*args)
        elif command_queue:
            cmd_args_pair = random.choice(command_queue)
            await cmd_args_pair[0](*cmd_args_pair[1])
            command_queue.remove(cmd_args_pair)
        else:
            await asyncio.sleep(10)
    if stop_bot:
        await bot.close()  # Stop the bot

bot.loop.create_task(check_queue())
bot.run()
