import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# De 'database' in het geheugen van de server
wereld_status = {
    "spelers": {}, # Hier komt: {"Naam": {"x": 10, "y": 20, "honger": 50}}
    "chat": []     # Hier komen de laatste 10 berichtjes
}

@app.route('/')
def home():
    return "Tamagotchi Multiplayer Server is ONLINE! 🌍"

@app.route('/update', methods=['POST'])
def update():
    data = request.json
    naam = data.get("naam")
    actie = data.get("actie") # 'update' of 'chat'

    if actie == "update" and naam:
        # Update de positie en status van de speler
        wereld_status["spelers"][naam] = {
            "x": data.get("x"),
            "y": data.get("y"),
            "honger": data.get("honger"),
            "tijd": data.get("tijd")
        }
    
    elif actie == "chat" and naam:
        # Voeg bericht toe aan de lijst
        nieuw_bericht = f"{naam}: {data.get('bericht')}"
        wereld_status["chat"].append(nieuw_bericht)
        # Onthoud alleen de laatste 10 berichtjes
        wereld_status["chat"] = wereld_status["chat"][-10:]

    return jsonify(wereld_status)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
