# GiniEmail - AI-based Email Content Generator Tool

## Overview

GiniEmail is an AI-based Email Content Generator Tool that allows users to quickly generate personalized email content for various purposes. It uses OpenAI's GPT-3.5 language model to generate high-quality email drafts based on user input.

## Live Demo

Visit the live demo of GiniEmail at [GiniEmail - AI-based Email Content Generator Tool](https://giniemail-ai-based-email-content-generator-tool-6fcgi9i4cyplnt.streamlit.app/)

<img width="596" alt="image" src="https://github.com/NurulhusnaJamalAli/GiniEmail-AI-based-Email-Content-Generator-Tool/assets/141206939/459014d1-50ee-407f-923e-6b6804a4ded3">

<img width="596" alt="image" src="https://github.com/NurulhusnaJamalAli/GiniEmail-AI-based-Email-Content-Generator-Tool/assets/141206939/09fb81e4-7d04-4582-b73c-a1e50d166d6f">

<img width="599" alt="image" src="https://github.com/NurulhusnaJamalAli/GiniEmail-AI-based-Email-Content-Generator-Tool/assets/141206939/66101883-2ba4-48f7-a88f-14f5bc70608b">

## Installation

To set up and install GiniEmail, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies using pip: `pip install -r requirements.txt`
3. Set up your OpenAI API key by creating a `.env` file and adding the following line:
   ```
   OPENAI_API_KEY="your_actual_openai_api_key_here"
   ```

## Usage

To use GiniEmail, run the `runapp.py` script and access the web application through your browser. Enter the recipient's name, email subject, desired tone, and any keywords related to the email's content. Select the desired language and the maximum email length, then click on the "Generate Email" button to get the AI-generated email draft.

## Configuration

GiniEmail requires an OpenAI API key for language model access. The API key should be kept private and not shared publicly. To set up the API key, create a `.env` file at the root of the project and store the key in the following format:
```
OPENAI_API_KEY="your_actual_openai_api_key_here"
```

## Features

- Generate personalized email drafts for various purposes.
- Support for both formal and casual email tones.
- Option to include keywords related to the email's content.
- Multiple language support for email generation.
- Set maximum email length to fit specific requirements.

## Deployment

To deploy GiniEmail to production, you can use Streamlit Cloud or other hosting platforms. Ensure that your API key is securely stored, and follow the platform-specific deployment instructions.

## License

GiniEmail is distributed under the MIT License. For the full license details, please refer to the [LICENSE](LICENSE) file.

## Acknowledgments

We would like to acknowledge the contributions of various open-source libraries and tools that make GiniEmail possible.

## Contact

For any questions or feedback, feel free to contact me at [jnurulhusna@gmail.com](mailto:jnurulhusna@gmail.com).

## Troubleshooting

If you encounter any issues while using GiniEmail, try the following troubleshooting tips:

- Double-check that you have set up the OpenAI API key correctly.
- Ensure that all required dependencies are installed.
- If you experience unexpected behavior, report the issue on the project's GitHub repository.

## FAQ

**Q: Can I use GiniEmail for commercial purposes?**
A: Yes, GiniEmail is open-source and distributed under the MIT License, allowing commercial use.

**Q: What is the maximum email length that can be generated?**
A: The maximum email length can be set by the user during email generation, ranging from 50 to 2000 characters.

**Q: Is my API key secure?**
A: Your API key should be kept confidential and not shared publicly to prevent unauthorized access to your OpenAI resources. Store it securely in the `.env` file.
