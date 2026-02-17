from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    openai_api_key: str = os.getenv("OPENAI_API_KEY")
    redis_url: str = os.getenv("REDIS_URL")

settings = Settings()