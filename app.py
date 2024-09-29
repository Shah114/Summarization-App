# Importing Modules
from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load summarization pipeline
summarizer = pipeline("summarization")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['input_text']
    if text:
        # Use the summarization model
        summary = summarizer(text, max_length=300, min_length=30, do_sample=False)[0]['summary_text']
        return render_template('index.html', summary=summary, input_text=text)
    return render_template('index.html', error="Please provide input text for summarization.")

# Main Part
if __name__ == '__main__':
    app.run(debug=True)
