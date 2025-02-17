from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

SCORING_URI = "http://387b4c4d-f0d0-4b0a-a677-42b7089bd248.centralindia.azurecontainer.io/score"
API_KEY = "tDc6Qe8J9UpZfUmwRqYCXxApvoa33S7f"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        json_input = request.form.get("json_input")
        try:
            payload = json.loads(json_input)
        except Exception as e:
            result = {"error": f"Invalid JSON input: {str(e)}"}
            return render_template("index.html", result=result)
        
        response = requests.post(SCORING_URI, headers=headers, data=json.dumps(payload))
        try:
            result = response.json()
        except Exception as e:
            result = {"error": "Failed to parse response", "raw_response": response.text}
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
