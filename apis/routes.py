from flask import Blueprint, request, jsonify, current_app
from utils.load_model import load_model_and_tokenizer
from utils.validators import validate_input
from flasgger.utils import swag_from
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
@swag_from({
    'consumes': ['application/json'],
    'parameters': [
        {
            'in': 'body',
            'name': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'review': {
                        'type': 'string',
                        'example': 'the food was good'
                    }
                },
                'required': ['review']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Prediction result',
            'examples': {
                'application/json': {
                    'sentiment': 'positive',
                    'confidence': 98.7
                }
            }
        }
    }
})
def predict():
    try:
        data = request.get_json()
        error = validate_input(data)

        if error:
            return jsonify({'error': error}), 400

        text = data['review']
        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)

        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
            probabilities = torch.nn.functional.softmax(logits, dim=1)
            confidence = torch.max(probabilities).item() * 100
            predicted_class = torch.argmax(probabilities, dim=-1).item()
            review = "Positive" if predicted_class == 1 else "Negative"

        current_app.logger.info(f"Review: {text}, Sentiment: {review}, Confidence: {confidence:.2f}%")

        return jsonify({
            'sentiment': review,
            'confidence': round(confidence, 2)
        })

    except Exception as e:
        current_app.logger.error(f"Error occurred: {str(e)}")
        return jsonify({"error": "An error occurred while processing the request."}), 500
