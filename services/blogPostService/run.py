from app import blog_services
from config import get_config

blog_service = blog_services()
config = get_config()

if __name__ == '__main__':
    blog_service.run(
        host=config.HOST,
        port=config.PORT,
        debug=config.DEBUG
    )
