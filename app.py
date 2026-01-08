from flask import Flask, render_template
import os
import time

app = Flask(__name__)
start_time = time.time()

@app.route("/")
def dashboard():
    uptime = round(time.time() - start_time, 2)
    return render_template(
        "index.html",
        environment=os.getenv("ENVIRONMENT", "development"),
        version=os.getenv("APP_VERSION", "1.0.0"),
        uptime=uptime
    )

@app.route("/health")
def health():
    return {"status": "UP"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

