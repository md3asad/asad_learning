from flask import Flask

app = Flask(__name__)

@app.route('/')
def sample_function():
    return "Welcome to the application"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)