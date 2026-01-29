"""
DATE
    22.06.25

DESCRIPTION
    This module contains functional/tooling binds for wikipedia.

    For use with the LLM, most functions will be heavily described
    in an easy-to-grasp vocabulary, so that the LLM can understand it
    properly.
"""

import wikipedia

def return_summary(topic: str) -> str:
    """
    Returns a summary of the topic provided by getting data from
    wikipedia.

    Args:
        topic: The topic given as an str, example: "Barack Obama"

    Returns:
        str: The summary of the topic; example: "Barack Obama was a president of the United States of America."
    """
    return wikipedia.summary(topic)

if __name__ == "__main__":
    print(return_summary("Barack Obama"))
