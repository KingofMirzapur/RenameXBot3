from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "5662853174:AAGnoMNwqNGGNGVtC6Hka1yaWLwZZcm8tTo")

API_ID = int(os.environ.get("API_ID", "8481654"))

API_HASH = os.environ.get("API_HASH", "2f1a45429dd34aceb56cbd66f1516bbc")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "renamer",
        bot_token=TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    app.run()
