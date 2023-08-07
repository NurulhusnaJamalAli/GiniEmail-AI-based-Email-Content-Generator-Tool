#%%
# Import packages
import streamlit as st
import openai
from googletrans import Translator

#%%
# Set your OpenAI API key
import os
openai.api_key = os.environ['OPENAI_API_KEY']

#%%
# Initialize the Google Translator
translator = Translator()

#%%
def get_language_code(selected_language):
    language_mapping = {
        "English": "en",
        "German": "de",
        "Malay": "ms",
        "Spanish": "es",
        "French": "fr",
        "Portuguese": "pt",
        "Italian": "it",
        "Japanese": "ja",
        "Korean": "ko",
        "Russian": "ru",
        "Arabic": "ar",
        "Dutch": "nl",
        "Swedish": "sv",
        "Turkish": "tr",
        "Hindi": "hi"
    }
    return language_mapping.get(selected_language, "en")  # Default to English if language not found

#%%
def generate_email(recipient_name, email_subject, desired_tone, keywords, selected_language):
    # Prepare the prompt for the model
    prompt = f"Dear {recipient_name},\n\nSubject: {email_subject}\n\n"
    if desired_tone == "Formal":
        prompt += "I hope this email finds you well. "
    else:
        prompt += "Hey! "

    if keywords:
        prompt += f"I am writing regarding {keywords}. "

    language_code = get_language_code(selected_language)
    model = "gpt-3.5-turbo"

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": f"You are writing an email to {recipient_name}. The email is about {email_subject}."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.71,
        max_tokens=2000  # Set a higher value for max_tokens to get longer responses
    )

    generated_email = response["choices"][0]["message"]["content"].strip()

    # Translate the generated email to the selected language if it's not in English
    if language_code != "en":
        translated_email = translator.translate(generated_email, src='en', dest=language_code).text
        generated_email = translated_email

    # Translate the 'start' variable to the selected language if it's not in English
    if language_code != "en":
        translated_start = translator.translate(f"Hi {recipient_name},", src='en', dest=language_code).text
    else:
        translated_start = f"Hi {recipient_name},"

    generated_email_with_intro = translated_start + " " + generated_email

    return generated_email_with_intro

#%%
def main():
    st.title("GiniEmail - AI-based Email Content Generator Tool")

    recipient_name = st.text_input("Recipient's Name:")
    email_subject = st.text_input("Email Subject:")
    desired_tone = st.selectbox("Desired Tone:", ["Formal", "Casual"])
    keywords = st.text_area("Keywords (comma-separated):")

    selected_language = st.selectbox(
        "Select Language:",
        ["English", "German", "Malay", "Spanish", "French", "Portuguese",
         "Italian", "Japanese", "Korean", "Russian", "Arabic", "Dutch", "Swedish", "Turkish", "Hindi"]
    )

    if st.button("Generate Email"):
        generated_email = generate_email(recipient_name, email_subject, desired_tone, keywords, selected_language)
        st.subheader("Generated Email:")
        st.write(generated_email)

if __name__ == "__main__":
    main()

