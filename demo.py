from TelegramVideoDownloader import TelegramVideoDownloader
from time import time

API_ID = None
API_HASH = None
PHONE_NUMBER = None

CHAT_LINK = None
SAVE_DIRECTORY = 'videos'
PROGRESS_FILE = 'download_progress.json'

start = time()
TelegramVideoDownloader = TelegramVideoDownloader(API_ID, API_HASH, PHONE_NUMBER, CHAT_LINK, SAVE_DIRECTORY, PROGRESS_FILE)
TelegramVideoDownloader.init_client()
with TelegramVideoDownloader.client:
    compact_map = {
        "Deep Learning parte 1 Introdução com Keras": ["#F001", "#F002", "#F003", "#F004", "#F005", "#F006", "#F007", "#F008", "#F009", "#F010",
            "#F011", "#F012", "#F013", "#F014", "#F015", "#F016", "#F017", "#F018", "#F019", "#F020"],
        "Machine Learning Intro a sistemas de recomendação em Python": ["#F021", "#F022", "#F023", "#F024", "#F025", "#F026", "#F027", "#F028", 
            "#F029", "#F030", "#F031", "#F032", "#F033", "#F034"],
        "Linguagem Natural parte 1 Introdução a NLP com análise de sentimento": ["#F035", "#F036", "#F037", "#F038", "#F039", 
            "#F040", "#F041", "#F042", "#F043", "#F044", 
            "#F045", "#F046", "#F047", "#F048", "#F049", 
            "#F050", "#F051"],
        "Linguagem Natural parte 2 Continuando com a análise de sentimento": ["#F052", "#F053", "#F054", "#F055", "#F056", 
            "#F057", "#F058", "#F059", "#F060", "#F061", 
            "#F062", "#F063", "#F064", "#F065"],
        "Machine Learning Introdução a algoritmos não supervisionados": ["#F066", "#F067", "#F068", "#F069", "#F070", 
            "#F071", "#F072", "#F073", "#F074", "#F075", 
            "#F076", "#F077", "#F078", "#F079"],
        "Machine Learning Introdução a classificação com SKLearn": ["#F080", "#F081", "#F082", "#F083", "#F084", 
            "#F085", "#F086", "#F087", "#F088", "#F089", 
            "#F090", "#F091", "#F092"],
        "Machine Learning Otimização com exploração aleatória parte 2": ["#F093", "#F094", "#F095", "#F096", "#F097", 
            "#F098", "#F099", "#F100"],
        "Machine Learning Otimização de modelos através de hiperparâmetros parte 1": ["#F101", "#F102", "#F103", "#F104", "#F105", 
            "#F106", "#F107", "#F108", "#F109", "#F110", 
            "#F111", "#F112"],
        "Machine Learning Validação de modelos": ["#F113", "#F114", "#F115", "#F116", "#F117", 
            "#F118", "#F119", "#F120", "#F121", "#F122", 
            "#F123"]
        
    }
    TelegramVideoDownloader.client.loop.run_until_complete(TelegramVideoDownloader.download_videos(compact=True, compact_quantity=3, compact_map=compact_map))
    
print("Download Finished")
print(start - time())