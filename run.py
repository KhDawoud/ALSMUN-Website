from flask import Flask, send_from_directory, render_template

app = Flask(__name__)
application = app

# Serve static files (like CSS, JS, images) from the 'static' folder
@app.route('/assets/<path:filename>')
def serve_static(filename):
    return send_from_directory('frontend/dist/assets', filename)

# Serve the index.html file for all routes, except those starting with '/static/'
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def base(path):
    if path.startswith("assets/"):
        # Allow Flask to serve static files
        return send_from_directory('frontend/dist', path)
    # For all other routes, serve the index.html file
    return send_from_directory('frontend/dist', 'index.html')

if __name__ == "__main__":
    app.run()
