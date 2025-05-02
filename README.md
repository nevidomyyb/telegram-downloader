### Telegram Downloader
- This app provides a API interface to download content (videos) from a telegram chat automatically and save it in folders.


##### How to run it

- You can use the `demo.py` as a example of how to use it.
- Remember to set the following variables:
  - API_ID: An API id from telegram
  - API_HASH: An API hash from telegram
  - PHONE_NUMBER: An phone number to the bot connect to the chat and telegram API
  - CHAT_LINK: the ID of the chat
  - SAVE_DIRECTORY: The directory to save the content
  - PROGRESS_FILE: a JSON where the app will track the progress
- By default the app uses the message of the video to identify that content as a file to be downloaded, if you want to check and modify the method of identify a content you need to check the function `TelegramVideoDownloader.extractName()` and `TelegramVideoDownloader.getFolderToCompactMap()`
- Calling the `TelegramVideoDownloader.download_videos()` with compact=True need to pass compact_map which you can check in the `demo.py`
