# Q&A Chatbot with OpenAI

This repository contains a simple Q&A chatbot built using Streamlit and OpenAI's GPT models. The chatbot allows users to ask questions and receive AI-generated responses based on OpenAI's large language models.

## Features
- Interactive chatbot using OpenAI's GPT models.
- Customizable model selection (GPT-4o, GPT-4-turbo, GPT-4).
- Adjustable temperature and max token settings for response control.
- Secure API key input via Streamlit sidebar.
- User-friendly interface for seamless interaction.

## Installation
### Prerequisites
Ensure you have Python installed (>=3.7) and set up a virtual environment (optional but recommended).

### Clone the Repository
```sh
git clone https://github.com/your-username/qna-chatbot-openai.git
cd qna-chatbot-openai
```

### Install Dependencies
Run the following command to install the required dependencies:
```sh
pip install -r requirements.txt
```

## Configuration
1. Create a `.env` file in the project root directory and add your OpenAI API key:
```
langchain_api_key=your_openai_api_key_here
```
2. Alternatively, enter your API key directly in the Streamlit sidebar when running the application.

## Running the Application
To start the chatbot, run:
```sh
streamlit run app.py
```

## Usage
1. Enter your OpenAI API key in the sidebar.
2. Select an OpenAI model from the dropdown.
3. Adjust the temperature and max token values as needed.
4. Type a question in the text input box and receive an AI-generated response.

## Troubleshooting
- Ensure you have a valid OpenAI API key.
- Check your internet connection.
- If experiencing rate limits, review your OpenAI API usage.
