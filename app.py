from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Testing Sucessful"

if __name__ == '__main__':
    app.run(debug=True)