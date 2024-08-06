from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", title="Home")

@app.route("/user/<username>")
def user(username):
    return render_template("user.html", username=username, title=f"User: {username}")

if __name__ == "__main__":
    app.run(debug=True)
