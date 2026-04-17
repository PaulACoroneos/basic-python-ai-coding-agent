from google.genai import types

from input_handler import get_user_args
from model_service import setup_and_invoke_model
from response_formatter import format_response


def main() -> None:
    user_args = get_user_args()
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_args.user_prompt)])
    ]
    content = setup_and_invoke_model(messages)
    print(format_response(user_args.user_prompt, content, user_args.verbose))


if __name__ == "__main__":
    main()
