import re


def clean_text(text: str) -> str:
    """
    Cleans the input text by removing special characters and extra spaces.

    Args:
        text (str): The input text to be cleaned.

    Returns:
        str: The cleaned text."""

    # Remove non-printable characters
    text = re.sub(r"[^\x20-\x7E]", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


def split_sentences(text: str) -> list:
    """
    Splits the input text into sentences based on punctuation.

    Args:
        text (str): The input text to be split.

    Returns:
        list: A list of sentences.
    """

    # Split text by sentence-ending punctuation
    sentences = re.split(r"(?<=[.!?]) +", text)

    return [s.strip() for s in sentences if len(s.strip()) > 0]
