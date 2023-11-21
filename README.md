# Language Predictor Web App

This repository contains a simple web application built with Streamlit for language prediction using a pre-trained model. The model predicts the language of the input text among a set of supported languages.

## Requirements
Make sure you have the following dependencies installed before running the application:

- `numpy`
- `pandas`
- `streamlit`
- `nltk`

You can install them using the following command:
```bash
pip install numpy pandas streamlit nltk
```

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Just-NK14/language-detection.git
   cd language-detection
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

3. Open your browser and navigate to the local host.

4. Enter the text in the provided textarea and click the "Predict" button to see the predicted language.

## Functions

### Preprocessing
The `preprocess` function is responsible for cleaning and preprocessing the input text. It converts the text to lowercase, tokenizes it, removes duplicates, and filters out numeric values and punctuation.

### Prediction
The `prediction` function uses the preprocessed text to predict the language using the trained model (`langpredict.pkl`).

### Language Dictionary
The `lang_dict` dictionary provides key-value pairs for different languages and their corresponding numeric codes.

### Web App
The Streamlit web app allows users to input text and predicts the language using the trained model. The result is displayed below the input, and the input text along with the predicted language is appended to an "input.txt" file.
