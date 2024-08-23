import os
import shutil
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from transformers import T5ForConditionalGeneration, T5Tokenizer
import requests
from bs4 import BeautifulSoup
import gdown

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Google Drive file ID (consider moving to environment variable if needed)
file_id = '1_be2xgPVIxFn_btf73CWBLC_kwFyfVQ-'
output = 'model.safetensors'
output_dir = './trained_model'

# Check if model exists locally; if not, download it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

if not os.path.exists(os.path.join(output_dir, output)):
    gdown.download(f'https://drive.google.com/uc?id={file_id}', output, quiet=False)
    shutil.move(output, os.path.join(output_dir, output))

# Load the model and tokenizer
model = T5ForConditionalGeneration.from_pretrained(output_dir)
tokenizer = T5Tokenizer.from_pretrained("t5-small")  # Adjust this if using a custom tokenizer

# Function to summarize text
def summarize_text(text):
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = model.generate(inputs, max_length=250, min_length=60, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Function to extract and summarize content from a URL
def summarize_from_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the main content text (you can adjust this as needed)
        paragraphs = soup.find_all('p')
        text = ' '.join([para.get_text() for para in paragraphs])

        if text:
            return summarize_text(text)
        else:
            return "Couldn't extract any content from the provided URL."
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data.get('text')
    url = data.get('url')

    if url:
        summary = summarize_from_url(url)
    elif text:
        summary = summarize_text(text)
    else:
        return jsonify({'error': 'No text or URL provided'}), 400

    return jsonify({'summary': summary})

# Serve the frontend HTML file
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

# Serve other static files (CSS, JS, images, etc.)
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    # Use PORT environment variable if available (Render sets this)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
