from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Testing Sucessful"

@app.l1('/l1')
def l1():
    return "How about one more 'Hello World!'"

if __name__ == '__main__':
    app.run(debug=True)
