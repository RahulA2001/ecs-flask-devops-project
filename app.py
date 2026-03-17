from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Rahul! ECS Farget App is working\n"

@app.route("/health")
def health():
    return "ok\n"

if __name__== "__main__":
    app.run(host="0.0.0.0", port=80)

