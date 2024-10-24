from flask import Blueprint, request, jsonify, current_app
from utils.load_model import load_model_and_tokenizer
from utils.validators import validate_input
import torch

# Initialize blueprint
api_blueprint = Blueprint('api', __name__)

# Load model and tokenizer at app startup
model, tokenizer = load_model_and_tokenizer()

# Custom error handler
@api_blueprint.errorhandler(400)
def bad_request_error(error):
    return jsonify({"error": "Bad Request", "message": str(error)}), 400

@api_blueprint.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal Server Error", "message": str(error)}), 500

# Predict api for sentiment analysis
@api_blueprint.route('/predict', methods=['POST'])
def predict():
    try:
        # Validate input
        data = request.get_json()
        error = validate_input(data)

        if error:
            return jsonify({'error': error}), 400

        text = data['review']

        # Tokenize the input
        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)

        # Make predictions
        review = "Negative"
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
            predicted_class = torch.argmax(logits, dim=-1).item()
            if predicted_class == 1:
                review = "Positive"

        # Log the request and response
        current_app.logger.info(f"Review: {text}, Sentiment: {review}")

        # Return the result
        return jsonify({'sentiment': review})

    except Exception as e:
        # Log error
        current_app.logger.error(f"Error occurred: {str(e)}")
        return jsonify({"error": "An error occurred while processing the request."}), 500