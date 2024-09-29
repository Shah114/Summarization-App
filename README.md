# Summarization-App
This project is a web-based text summarization application built using the Flask framework and the pipeline module from Hugging Face's transformers library. The app allows users to input large blocks of text, and it generates concise summaries using a state-of-the-art pre-trained model.

The web interface is designed with HTML, CSS (styled with a light blue and white color scheme), and includes basic animations to enhance user experience. <br/>
<br/>

## Features
* Summarization: Input long-form text, and the app will return a concise summary using a pre-trained transformer model.
* User-Friendly Interface: The web interface is minimalist, featuring a clean design with animations to make interactions smooth and appealing.
* Real-Time Processing: The app processes text in real-time and quickly returns summaries for various text lengths. <br/>
<br/>

## Project Structure
```graphql
.
├── app.py                # The main Flask app
├── requirements.txt      # Python dependencies
├── static/
│   └── style.css         # Custom CSS for styling
└── templates/
    └── index.html        # HTML template for the web interface
```
<br/>

1. app.py
This is the main Python script where the Flask app is defined. It uses the transformers library to load the summarization pipeline and provides routes to handle user requests.

2. templates/index.html
The HTML template defines the front-end structure for the app. It includes a text area for input and displays the generated summary on the same page.

3. static/style.css
This file contains the CSS styling for the app. It includes a light blue and white color scheme with animations for better user experience. <br/>
<br/>

## How to Run the App
1. Clone the repository:

   ```bash
   git clone https://github.com/Shah114/Summarization-App.git
   ```

2. Navigate to the project directory:

   ```bash
   cd summarization-app
   ```

3. Start the Flask server:

   ```bash
   python app.py
   ```
<br/>

## Usage
1. Enter a block of text in the provided text area.
2. Click the "Summarize" button.
3. The summarized text will be displayed on the same page. <br/>
<br/>

## Example
Input:

```vbnet
The transformers library from Hugging Face is a popular library for natural language processing. It provides pre-trained models for tasks such as text classification, question answering, and summarization, among others. The library is easy to use and has a large community contributing models and improvements.
```
