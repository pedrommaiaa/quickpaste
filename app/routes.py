from app import app

@app.route('/')
def home():
    return "Hello, this is the home page."
