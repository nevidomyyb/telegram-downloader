import os
import time
import json
from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterVideo, Message

class TelegramVideoDownloader:
    def __init__(self, api_id: str, api_hash:str , phone_number:str , chat_link:str , save_directory:str , progress_file:str ):
        self.api_id = api_id
        self.api_hash = api_hash
        self.phone_number =phone_number
        self.chat_link = chat_link
        self.save_directory = save_directory
        self.progress_file = progress_file
        
    def init_client(self) -> None:
        self.client = TelegramClient('client', self.api_id, self.api_hash)
        self.client.start(self.phone_number)
        
    def load_progress(self) -> set:
        if os.path.exists(self.progress_file):
            with open(self.progress_file, 'r') as f:
                return set(json.load(f))
        return set()

    def save_progress(self, progress: set) -> None:
        with open(self.progress_file, 'w') as f:
            json.dump(list(progress), f)
    
    def extract_name(self, message: Message) -> str:
        #Use this to modify the way the script will extract the filename from the Message.
        #This impacts how the app will compact using module function too.
        #Return a string.
        title_list = message.message.split("\n")
        for title in title_list:
            if "#F" in title:
                return title.replace(" ","-")
            else:
                print("The name was not found using 'extract_name' function. Using ID of the message.")
                return message.id
            
    def getFolderToCompactMap(self, title: str, compact_map: dict) -> None:
        #Modify this function to change the way the script will use the compact_map to identify the folder to save the file,
        #Using the title of the file
        folder_name = None
        for folder in compact_map:
            if title[0:5] in compact_map[folder]:
                folder_name = folder        
                break
        return folder_name
    
    async def download_videos(self, compact: bool = False, compact_quantity:int = None, compact_map:dict = None) -> None:
        if compact_quantity != None and compact_map != None:
            raise Exception("You only can use compacting by video quantity or mapping by modules.")
        if compact and (compact_quantity == None and compact_map == None):
            raise Exception("You should provide a compact quantity or compacty map when using compact function.")
        
        downloaded_ids = self.load_progress()
        entity = await self.client.get_entity(self.chat_link)
        async for message in self.client.iter_messages(entity, filter=InputMessagesFilterVideo):
            if message.video and message.id not in downloaded_ids:
                video_name = self.extract_name(message)
                folder = self.getFolderToCompactMap(video_name, compact_map)
                if compact_map and compact:
                    folder_complete = os.path.join(self.save_directory, folder)
                else:
                    folder_complete = self.save_directory
                try:
                    print(f"Downloading: {video_name}")
                    os.makedirs(folder_complete, exist_ok=True)
                    await self.client.download_media(message, file=folder_complete)
                    downloaded_ids.add(message.id)
                    self.save_progress(downloaded_ids)
                    time.sleep(2)
                except Exception as e:
                    print(f"Erro ao baixar {folder_complete}: {e}")
                    break
        if compact:
            if compact_map:
                ...
                
    async def list_chats(self):
        async for dialog in self.client.iter_dialogs():
            print(f"Chat title: {dialog.title} | Chat ID: {dialog.id}")
            
        