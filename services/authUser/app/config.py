import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = '37ddfcef84750d775b5b62e9a9c925548e42de37f5f00a' \
                 'beca1b22f5745a3c32b16106021e2eeb1dd9d527' \
                 '4cd86d9d6761384dd2e98ad6b4cb23e62df60b37e4'
    # Use environment variable for database URI with SQLite as fallback
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///BanjaraBackpacker.db') # 
    print('The Postgres URI : ', os.getenv('DATABASE_URL'))
    print('SQLALCHEMY_DATABASE_URI ', SQLALCHEMY_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
