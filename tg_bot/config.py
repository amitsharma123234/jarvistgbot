from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 1365686472  # my telegram ID
    OWNER_USERNAME = "ramshouriesh"  # my telegram username
    API_KEY = "1334628285:AAHt_HbyiJv4y0ftPwJZL_tqjuCK1kKFUnU"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'mongodb+srv://securitybot:securitybot@cluster0.tmdok.mongodb.net/SecurityBot?retryWrites=true&w=majority'  # sample db credentials
    MESSAGE_DUMP = '-1234567890' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [1318486004, 1203294851]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
    SUPPORT_USERS = 1365686472
    WORKERS = 8
    ENV = "ANYTHING"
