# Imports
from dotenv import load_dotenv
from flask import Flask, request, make_response
from embed import get_embedding

# Setup
load_dotenv()
app = Flask(__name__)

# CORS headers
headers_cors = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "POST",
    "Access-Control-Allow-Headers": "API-Key, Content-Type",
    "Access-Control-Max-Age": "3600",
}


# Helper function to extract data from JSON request
def extract_data(json_request, field):
    return json_request.get(field, "").strip()


@app.route("/knowledge", methods=["OPTIONS", "GET"])
def get_knowledge():
    if request.method == "OPTIONS":
        return make_response("", 204, headers_cors)

    return make_response('{"Fieldname":"Value"}', 200, headers_cors)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("8080"), debug=False)
