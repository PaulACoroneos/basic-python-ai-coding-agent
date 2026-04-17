from google.genai import types

from input_handler import get_user_prompt
from model_service import setup_and_invoke_model
from response_formatter import format_response


def main() -> None:
    user_prompt = get_user_prompt()
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]
    content = setup_and_invoke_model(messages)
    print(format_response(user_prompt, content))


if __name__ == "__main__":
    main()
