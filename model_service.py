import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


def setup_and_invoke_model(
    messages: list[types.Content],
) -> types.GenerateContentResponse:
    """Create the Gemini client and execute a single content generation request."""
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("Could not load gemini api key")

    client = genai.Client(api_key=api_key)
    return client.models.generate_content(model="gemini-2.5-flash", contents=messages)
