from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", title="Home")

@app.route("/result", methods=["POST"])
def result():
    username = request.form.get("username")
    email = request.form.get("email")
    return render_template("result.html", username=username, email=email, title="Result")

if __name__ == "__main__":
    app.run(debug=True)
