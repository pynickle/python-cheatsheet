from flask import Flask, render_template

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile("config.py")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=5555)