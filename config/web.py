import os

APP_NAME = "Web Makeover"
SECRET_KEY = "key"
ENVIRONMENT = "web"
DISPLAY_DEBUG_INFO = False
TEMPLATES_AUTO_RELOAD = True
FB_APP_ID = os.getenv("FB_APP_ID", "")
FB_APP_SECRET = os.getenv("FB_APP_SECRET", "")
SERVER_NAME="web.evanshi.me"
CHECK_IMAGES = False
