from app import auth_service

app = auth_service()

if __name__ == '__main__':
    app.run(debug=True, port=5001)
