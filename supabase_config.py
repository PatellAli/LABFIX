import os
from dotenv import load_dotenv, dotenv_values
from supabase import create_client, Client

config = dotenv_values(".env")


url: str = config['URL']
key: str = config['KEY']
supabase: Client = create_client(url, key)