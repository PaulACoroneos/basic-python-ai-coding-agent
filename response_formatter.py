from google.genai import types


def format_response(user_prompt: str, content: types.GenerateContentResponse) -> str:
    """Format model output and token usage for display in the terminal."""
    if content.usage_metadata is None:
        raise RuntimeError("Possible failed API request due to no usage_metadata")

    return "\n".join(
        [
            f'role="user": {user_prompt}',
            f'role="model": {content.text or ""}',
            f"Prompt tokens: {content.usage_metadata.prompt_token_count}",
            f"Response tokens: {content.usage_metadata.candidates_token_count}",
        ]
    )
