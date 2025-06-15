# SentimentAnalysis

A sentiment analysis project developed for the **T-Wars** competition. This application processes restaurant reviews to determine their sentiment polarity (positive or negative) using Natural Language Processing (NLP) techniques and machine learning models.

## 📁 Project Structure

- `SentimentAnalysisModel.ipynb`: Jupyter Notebook for training and evaluating the sentiment analysis model.
- `app.py`: Flask application to serve the model and provide an API endpoint for predictions.
- `Restaurant_Reviews.tsv`: Dataset containing restaurant reviews used for training the model.
- `environment.yml`: Conda environment configuration file listing all dependencies.
- `requirements.txt`: Python package dependencies.
- `utils/`: Directory containing utility scripts.
- `apis/`: Directory for API-related code.
- `logs/`: Directory for storing logs.
- `Procfile`: Configuration file for deploying the app on platforms like Heroku.
- `Evalution.md`: Documentation for model evaluation metrics.

## 🚀 Getting Started

### Prerequisites

- [Anaconda](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) installed on your system.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/riwazudas/SentimentAnalysis.git
   cd SentimentAnalysis
   ```
2. Create and activate the Conda environment:

```bash
conda env create -f environment.yml
conda activate sentimentanalysis
```

3. Install additional dependencies (if any):

```bash
pip install -r requirements.txt
```

### Running the Application

1. Start the Flask server:
```bash
python app.py
```

2.Access the API:

Send a POST request to the /predict endpoint with the review text to get the sentiment prediction.
Example using curl:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"review": "The food was amazing!"}' http://localhost:5000/predict
```


## 🧠 Training the Model
To train or retrain the sentiment analysis model:

Open the SentimentAnalysisModel.ipynb notebook using Jupyter Notebook or Google Colab.

Run the cells sequentially to:

Load and preprocess the dataset.

Train the machine learning model.

Evaluate the model's performance.

Save the trained model for deployment.

Note: Ensure that the Restaurant_Reviews.tsv dataset is present in the project directory before running the notebook.

## 📊 Evaluation
Detailed evaluation metrics and model performance can be found in the Evalution.md file.


