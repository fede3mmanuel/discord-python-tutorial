from typing import  Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

#Step 0: Load our token from somewhere safe
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
print(TOKEN)