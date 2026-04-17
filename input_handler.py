import argparse


def get_user_prompt() -> str:
    """Parse and return the user's prompt from the CLI."""
    parser = argparse.ArgumentParser("Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    return args.user_prompt
