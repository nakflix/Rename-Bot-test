import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", "14298205"))
API_HASH = os.environ.get("API_HASH", "28df6d84da76d8606bf5f0e71ecfb62c")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7148807362:AAHsmCw_cfrgGvaKeR7VYgLwmaA1uKsLugA")
ADMIN = int(os.environ.get("ADMIN", "1458235021"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "-1002271917654")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001870385542"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://alphakiti:alpha3720@renamerbot.9ux2j.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "renamerbot")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/ada3f739fed7efdbe7b08.jpg")
