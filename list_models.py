from dotenv import load_dotenv
from google import genai

load_dotenv()                 # puts GOOGLE_API_KEY from .env into the environment
client = genai.Client()       # the Google SDK reads the key automatically

for model in client.models.list():
    # only show models that can generate text/chat
    if "generateContent" in (model.supported_actions or []):
        print(model.name)