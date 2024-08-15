# GeminiDecode: Multilanguage Document Extractor

## Overview
- **GeminiDecode** is a powerful application that leverages Google Gemini Pro AI to extract vital information from multilingual documents.
- This project breaks language barriers, making document extraction precise, efficient, and accessible across different languages.

## Features
- Upload images of documents (supports `.jpg`, `.jpeg`, `.png`).
- Extract and analyze textual information from invoices or other documents using AI.
- Display the uploaded image and extracted content for user review.
- Multilingual support: Process documents in various languages.
- Simple and intuitive user interface powered by Streamlit.

## Requirements
- Python 3.7 or higher
- Streamlit
- Pillow
- Google Generative AI Python SDK
- dotenv

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-repo/GeminiDecode.git
    cd GeminiDecode
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your Google API Key:**
    - Create a `.env` file in the root directory.
    - Add your API key to the `.env` file:
    ```env
    GOOGLE_API_KEY=your_google_api_key
    ```

## Usage

1. **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

2. **Upload an Image:**
    - Choose an image of the document you want to extract information from (supported formats: `.jpg`, `.jpeg`, `.png`).

3. **Process the Document:**
    - Click the "Tell me about the document" button to extract and view the information.

4. **Review Results:**
    - The extracted content will be displayed on the app.

## Project Structure

```bash
├── app.py                 # Main application script
├── .env                   # Environment variables (API key)
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .gitignore             # Files to ignore in version control
