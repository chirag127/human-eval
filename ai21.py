"""
This module contains the code for the code generation model codex.
"""

import requests
from f import get_samples, write_jsonl_in_folder
from apikey import AI21_KEY


def generate_one_completion(prompt):
    """
    This function generates one completion for a given prompt.
    """
    response = requests.post(
        "https://api.ai21.com/studio/v1/j1-large/complete",
        timeout=60,
        headers={
            "authority": "api.ai21.com",
            "accept": "application/json",
            "accept-language": "en-US,en;q=0.9",
            "authorization": AI21_KEY,
            "content-type": "application/json",
            "dnt": "1",
            "origin": "https://studio.ai21.com",
            "referer": "https://studio.ai21.com/",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "sec-gpc": "1",
            "x-requested-with": "XMLHttpRequest",
        },
        json={
            "prompt": prompt,
            "model": "j1-large",
            "temperature": 0.2,
            "topP": 1,
            "maxTokens": 100,
            "numStopSequences": 1,
            "stopSequences": ["\ndef ", "\nclass ", "\n\n#", "\n\n\n\n"],
            "stream": False,
            "frequencyPenalty": {
                "scale": 0.01,
                "applyToWhitespaces": True,
                "applyToPunctuations": True,
                "applyToNumbers": True,
                "applyToStopwords": True,
                "applyToEmojis": True,
            },
            "presencePenalty": {
                "scale": 0.01,
                "applyToWhitespaces": True,
                "applyToPunctuations": True,
                "applyToNumbers": True,
                "applyToStopwords": True,
                "applyToEmojis": True,
            },
            "countPenalty": {
                "scale": 0.01,
                "applyToWhitespaces": True,
                "applyToPunctuations": True,
                "applyToNumbers": True,
                "applyToStopwords": True,
                "applyToEmojis": True,
            },
        },
    )

    response = response.json()

    completions = response["completions"][0]
    data = completions["data"]
    text = data["text"]
    print(text)
    return text


NUM_SAMPLES_PER_TASK = 11


def main() -> None:
    """
    This function is the main function for the code generation model codegeex.
    """
    samples = get_samples(
        num_samples_per_task=NUM_SAMPLES_PER_TASK,
        _get_code_from_api=generate_one_completion,
    )
    print(samples)
    write_jsonl_in_folder("ai21", samples)


if __name__ == "__main__":
    for _ in range(10):
        main()
