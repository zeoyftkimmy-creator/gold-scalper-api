from flask import Flask, jsonify, request
from datetime import datetime, timezone

app = Flask(__name__)

bot_running = False


@app.route("/")
def home():
    return jsonify({
        "service": "Gold Scalper API",
        "status": "online",
        "bot_running": bot_running
    })


@app.route("/status", methods=["GET"])
def status():
    return jsonify({
        "status": "running" if bot_running else "stopped",
        "bot_running": bot_running,
        "time": datetime.now(timezone.utc).isoformat()
    })


@app.route("/start", methods=["GET", "POST"])
def start():
    global bot_running
    bot_running = True

    return jsonify({
        "success": True,
        "status": "running",
        "bot_running": True
    })


@app.route("/stop", methods=["GET", "POST"])
def stop():
    global bot_running
    bot_running = False

    return jsonify({
        "success": True,
        "status": "stopped",
        "bot_running": False
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok"
    })


if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
