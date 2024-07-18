import spacy
from flask import Flask, jsonify, request, abort
import logging
import os

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_significant_keyword(text):
    # Process the input text
    doc = nlp(text)
    
    # Extract keywords
    keywords = []
    for token in doc:
        # Consider only nouns and proper nouns
        if token.pos_ in ['NOUN', 'PROPN'] and not token.is_stop:
            keywords.append(token.text)
    
    # Return the most significant keyword (e.g., the first one)
    return keywords[0] if keywords else None

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route("/", methods=["POST"])
def three():
    try:
        request_data = request.get_json()
        if not request_data or 'text' not in request_data:
            abort(400, description="Bad Request: 'text' field is required.")
        
        s = request_data["text"]
        r = extract_significant_keyword(s)
        result = {"result": r}
        return jsonify(result)
    except Exception as e:
        logging.error(f"Error processing request: {e}")
        abort(500, description="Internal Server Error")

@app.route("/", methods=["GET"])
def two():
    return "App running on port 5000"

if __name__ == "__main__":
    # Use environment variable for port
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)