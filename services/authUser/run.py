from app import auth_service

app = auth_service()

if __name__ == '__main__':
    app.run(host='localhost', port=5001, debug=True)
