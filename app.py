import os
from flask import Flask, request, jsonify

app = Flask(__name__)
# Database voor spelers en chat
wereld = {"spelers": {}, "chat": []}

@app.route('/update', methods=['POST'])
def update():
    data = request.json
    naam = data.get("naam")
    if naam:
        # Sla alle stats van de speler op
        wereld["spelers"][naam] = {
            "x": data.get("x"),
            "y": data.get("y"),
            "geld": data.get("geld"),
            "honger": data.get("honger"),
            "locatie": data.get("locatie")
        }
    return jsonify(wereld)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
