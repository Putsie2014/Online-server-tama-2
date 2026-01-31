import os
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Dit zijn de 'lijsten' waar de server alles in onthoudt
all_chats = []
players_online = {}

# Een simpele 'test' pagina zodat je ziet dat hij werkt
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Tamagotchi Server</title>
    <style>
        body { background: #1a1a2e; color: white; font-family: sans-serif; text-align: center; padding-top: 50px; }
        .status { color: #4ee44e; font-weight: bold; }
    </style>
</head>
<body>
    <h1>🚀 Je Tamagotchi Server is LIVE!</h1>
    <p>Status: <span class="status">Verbonden</span></p>
    <p>Je kunt nu je game verbinden met deze URL.</p>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

# Dit deel zorgt voor de chat en de spelers
@app.route('/update', methods=['POST'])
def update():
    data = request.json
    # Hier kun je later logica toevoegen om chats op te slaan
    return jsonify({
        "status": "ok",
        "message": "Data ontvangen door de server!"
    })

if __name__ == "__main__":
    # DIT IS HET BELANGRIJKSTE DEEL VOOR RENDER:
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
