from flask import Flask
from apis.routes import api_blueprint 
import logging
from logging.handlers import RotatingFileHandler
import os
from flasgger import Swagger
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

swagger = Swagger(app, template={
    "swagger": "2.0",
    "info": {
        "title": "Sentiment Analysis API",
        "description": "API for predicting sentiment using BERT",
        "version": "1.0.0"
    }
})

# Register blueprints
app.register_blueprint(api_blueprint, url_prefix='/api')

if not os.path.exists('logs'):
    os.makedirs('logs')

# Setup logging
handler = RotatingFileHandler('logs/app.log', maxBytes=10000, backupCount=3)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

# Setup default page
@app.route('/', methods=['GET'])
def home():
    """
    Welcome Route
    ---
    responses:
      200:
        description: Sentiment Analysis API is up and running!
    """
    return {"message": "Sentiment Analysis API is up and running!"}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
