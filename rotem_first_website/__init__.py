from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()

