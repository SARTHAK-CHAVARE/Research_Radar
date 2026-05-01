from dotenv import load_dotenv
import os
import requests

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

print("TOKEN:", TOKEN)
print("CHAT_ID:", CHAT_ID)

def send_message(message):
    url = f"https://api.telegram.org/bot8501689777:AAGQfPYHFbcWuBwgagN-_7qZWdGAHW_iJUI/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    response = requests.post(url, data=data)
    print(response.json())

if __name__ == "__main__":
    send_message("Final working test 🚀")