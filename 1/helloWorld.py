from flask import Flask , request

app = Flask(__name__)

@app.route("/")
def display():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0" , port=5000)


