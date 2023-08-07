# GiniEmail AI based Email Content Generator Tool
GiniEmail is an AI-powered email content generator tool built using Streamlit and OpenAI's GPT-3.5-turbo model. This tool allows users to quickly generate personalized email drafts by providing the recipient's name, email subject, desired tone, and keywords (optional). The generated emails can be translated into multiple languages using Google Translate.

## Features

- Input recipient's name, email subject, desired tone, and optional keywords to generate personalized email drafts.
- Supports both formal and casual email tones.
- Choose from multiple languages for email generation and translation.
- Set the maximum email length to control the output size.

## How to Run the App

1. Ensure you have set up the `.env` file with your OpenAI API key.

2. Run the app using `runapp.py`:

   ```
   streamlit run runapp.py
   ```

3. The app will launch in your default web browser. Enter the recipient's name, email subject, desired tone, keywords (if any), select the language, and set the maximum email length. Then, click the "Generate Email" button to receive the AI-generated email.

## Note

- This project uses Streamlit and OpenAI API. Ensure you have set up your OpenAI API key.

## Disclaimer

This project is for educational and demonstration purposes only. The AI-generated content may not always be accurate or contextually appropriate. Use the generated emails responsibly and review the content before sending.
