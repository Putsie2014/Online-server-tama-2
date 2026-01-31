from flask import Flask, request, jsonify, render_template_string
import json, os, time

app = Flask(__name__)
all_chats = []
players_online = {}

HTML_GAME = """
<!DOCTYPE html>
<html>
<head><title>Tamagotchi Cloud</title></head>
<body style="background:#1a1a2e; color:white; text-align:center;">
    <h1>De game is ONLINE! 🚀</h1>
    <p>Als je dit ziet, werkt de server.</p>
    <canvas id="gameCanvas" width="500" height="300" style="background:#27ae60;"></canvas>
    <script>
        console.log("Game gestart!");
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_GAME)

@app.route('/update', methods=['POST'])
def update():
    return jsonify({"status": "ok", "chats": all_chats, "all_players": players_online})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
