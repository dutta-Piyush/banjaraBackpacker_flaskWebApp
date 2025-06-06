from app import auth_service
from config import get_config

app = auth_service()
config = get_config()

if __name__ == '__main__':
    app.run(
        host=config.HOST,
        port=config.PORT,
        debug=config.DEBUG
    )
