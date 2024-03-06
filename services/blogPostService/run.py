from app import blog_services


blog_service = blog_services()

if __name__ == '__main__':
    blog_service.run(debug=True, port=5002)