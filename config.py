# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "28929094"))
API_HASH = getenv("API_HASH", "103b40f283c263aca46e24b55e5e022f")
BOT_TOKEN = getenv("BOT_TOKEN", "7522177087:AAGgTGg9ihOk3-I3-berha17OoiBIKI94WI")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6076683960 7400335416").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://sanjisama626:sanjisama626@sanjisama.lukxw8r.mongodb.net/?retryWrites=true&w=majority&appName=sanjisama")
LOG_GROUP = getenv("LOG_GROUP", "-1002168297139")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002146121321"))
