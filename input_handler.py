import argparse
from argparse import Namespace


def get_user_args() -> Namespace:
    """Parse and return the user's prompt from the CLI."""
    parser = argparse.ArgumentParser("Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    return parser.parse_args()
