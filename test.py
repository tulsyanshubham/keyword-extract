import spacy

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

# if __name__ == "__main__":
#     # Take input from the user
#     user_input = input("Enter a statement: ")
    
#     # Extract and print keywords
#     keywords = extract_significant_keyword(user_input)
#     print("Keywords:", keywords)



from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
# now data can be send in body
def three():
    request_data = request.get_json()
    s = request_data["text"]
    r = extract_significant_keyword(s)
    result = {"result": r}
    return jsonify(result)

@app.route("/", methods=["GET"])
# now data can be send in body
def two():
    return "App running on port 5000"

if __name__ == "__main__":
    app.run(debug=False)