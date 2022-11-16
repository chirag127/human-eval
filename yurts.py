"""
This module contains the code for the code generation model codex.
"""

import requests
from f import get_samples, write_jsonl_in_folder


def generate_one_completion(prompt):

    response = requests.post(
        "https://lb.yurts.ai/models/7b36cc5a-d6e9-4241-aee8-b299fc1280c7-12/prediction",
        headers={
            "authority": "lb.yurts.ai",
            "accept": "application/json, text/plain, */*, application/json",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "origin": "https://playground.yurts.ai",
            "referer": "https://playground.yurts.ai/",
            "sec-ch-ua": '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetcher-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42",
        },
        json={"text": prompt},
    )
    response = response.json()
    code = response["text"]

    # remove prompt from code and only one time
    code = code.replace(prompt, "", 1)

    print(code)
    return code


NUM_SAMPLES_PER_TASK = 3


def main() -> None:
    """
    This function is the main function for the code generation model codegeex.
    """
    samples = get_samples(
        num_samples_per_task=NUM_SAMPLES_PER_TASK,
        _get_code_from_api=generate_one_completion,
    )
    print(samples)
    write_jsonl_in_folder("yurt", samples)


if __name__ == "__main__":
    main()
