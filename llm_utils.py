import os
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY"

def get_gemini_model():
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7)
    return llm