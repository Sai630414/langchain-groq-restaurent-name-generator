# Restaurant Name & Menu Generator

A Streamlit app that uses LangChain and Groq to generate a restaurant name and
ten menu items for a selected cuisine.

## Requirements

- Python 3.10 or later
- A Groq API key

## Setup

1. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

2. Install the dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3. Create `secretkey.py` in the project folder and add your Groq API key:

   ```python
   GROQ_API_KEY = "your-groq-api-key"
   ```

   Keep this file private; it is excluded from Git.

## Run

```powershell
streamlit run main.py
```

Choose a cuisine from the list and select **Generate** to create a restaurant
name and its menu.
