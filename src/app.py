# Imports
from dotenv import load_dotenv
from flask import Flask, request, make_response, jsonify
from embed import get_embedding
from knowledge import search_docs

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


@app.route("/knowledge", methods=["OPTIONS", "POST"])
def get_knowledge():
    if request.method == "OPTIONS":
        return make_response("", 204, headers_cors)

    if not request.is_json:
        return make_response("Request should be in JSON format", 400)
    
    query = extract_data(request.json, "query")
    if not query:
        return jsonify({"error": "Query is required"}), 400
    
    # Get embedding
    vector = get_embedding(query)
    
    # Search for similar documents
    results = search_docs(vector)

    return make_response(jsonify(results), 200, headers_cors)


if __name__ == "__main__":    
    app.run(host="0.0.0.0", port=int("8080"), debug=False)
