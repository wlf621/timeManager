import os.path

DEBUG = True

# 防止中文乱码
JSON_AS_ASCII = False

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_URL_PATH = ''
STATIC_FOLDER = '../static'
