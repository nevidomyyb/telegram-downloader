import os
import time
import json
from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterVideo

class TelegramVideoDownloader:
    def __init__(self, api_id: str, api_hash:str , phone_number:str , chat_link:str , save_directory:str , progress_file:str ):
        self.api_id = api_id
        self.api_hash = api_hash
        self.phone_number =phone_number
        self.chat_link = chat_link
        self.save_directory = save_directory
        self.progress_file = progress_file
        
    def init_client(self):
        self.client = TelegramClient('client', self.api_id, self.api_hash)
        self.client.start(self.phone_number)
        
    def load_progress(self) -> set:
        if os.path.exists(self.progress_file):
            with open(self.progress_file, 'r') as f:
                return set(json.load(f))
        return set()

    def save_progress(self, progress: set):
        with open(self.progress_file, 'w') as f:
            json.dump(list(progress), f)
    
    async def download_videos(self, ):
        
        downloaded_ids = self.load_progress()
        entity = await self.client.get_entity(self.chat_link)
        async for message in self.client.iter_messages(entity, filter=InputMessagesFilterVideo):
            print(message)
            if message.video and message.id not in downloaded_ids:
                file_name = os.path.join(self.save_directory, f"{message.id}.mp4")
                try:
                    print(f"Downloading: {file_name}")
                    # await self.client.download_media(message, file=file_name)
                    downloaded_ids.add(message.id)
                    self.save_progress(downloaded_ids)
                    time.sleep(2)
                except Exception as e:
                    print(f"Erro ao baixar {file_name}: {e}")
                    break
                
    async def list_chats(self):
        async for dialog in self.client.iter_dialogs():
            print(f"Chat title: {dialog.title} | Chat ID: {dialog.id}")
            
        