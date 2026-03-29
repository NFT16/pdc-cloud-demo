from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello from Cloud! 🚀</h1><p>Deployed by Noor & Maryam- PDC Lab</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)