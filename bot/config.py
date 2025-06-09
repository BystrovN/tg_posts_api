import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN: str = os.getenv('BOT_TOKEN')
API_URL: str = f'{os.getenv("API_URL", "http://localhost:8000")}/api/posts/'
POST_TG_COMMAND: str = 'posts'
