import argparse
import os

from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("Could not load gemini api key")

    parser = argparse.ArgumentParser("Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    client = genai.Client(api_key=api_key)

    content = client.models.generate_content(
        model="gemini-2.5-flash", contents=args.user_prompt
    )

    if content.usage_metadata is None:
        raise RuntimeError("Possible failed API request due to no usage_metadata")
    print(f"Prompt tokens: {content.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {content.usage_metadata.candidates_token_count}")
    print(content.text)


if __name__ == "__main__":
    main()
