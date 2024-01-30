from flask import Flask, send_from_directory, render_template

app = Flask(__name__)
application = app


@app.route("/<path:path>")
def home(path):
    return send_from_directory("../frontend/dist", path)


@app.route("/")
def base():
    return send_from_directory('../frontend/dist', 'index.html')


if __name__ == "__main__":
    app.run()
    