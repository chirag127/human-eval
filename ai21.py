"""
This module contains the code for the code generation model codex.
"""

import requests
from f import get_samples,write_jsonl_in_folder
from apikey import AI21_KEY

def generate_one_completion(prompt):
    response = requests.post(
        "https://api.ai21.com/studio/v1/j1-large/complete",
        headers={
            "authority": "api.ai21.com",
            "accept": "application/json",
            "accept-language": "en-US,en;q=0.9",
            "authorization": AI21_KEY,
            "content-type": "application/json",
            "dnt": "1",
            "origin": "https://studio.ai21.com",
            "referer": "https://studio.ai21.com/",
            "sec-ch-ua": "\"Microsoft Edge\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "sec-gpc": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42",
            "x-requested-with": "XMLHttpRequest",
        },
        json={
            "prompt": prompt,
            "model": "j1-large",
            "temperature": 0,
            "topP": 1,
            "maxTokens": 400,
            "numStopSequences": 1,
            "stopSequences": ["\r"],
            "stream": False,

            "frequencyPenalty": {
                "scale": 0,
                "applyToWhitespaces": False,
                "applyToPunctuations": False,
                "applyToNumbers": False,
                "applyToStopwords": False,
                "applyToEmojis": False,
            },
            "presencePenalty": {
                "scale": 0,
                "applyToWhitespaces": False,
                "applyToPunctuations": False,
                "applyToNumbers": False,
                "applyToStopwords": False,
                "applyToEmojis": False,
            },
            "countPenalty": {
                "scale": 0,
                "applyToWhitespaces": False,
                "applyToPunctuations": False,
                "applyToNumbers": False,
                "applyToStopwords": False,
                "applyToEmojis": False,
            },
        },
    )


    response = response.json()

    completions = response["completions"][0]
    data = completions["data"]
    text = data["text"]
    print(text)
    return text

NUM_SAMPLES_PER_TASK = 1


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
    main()


# if __name__ == "__main__":
#     response = generate_one_completion("""Q: Write a Python program that calculates the sum of all positive integers smaller than 8.
# A: sum(x for x in range(8))
# Q: Write a Python program that calculates the sum of squares of all positive integers between 2 and 13.
# A: sum(x**2 for x in range(2, 13))
# Q: print hello world""")
#     # print(response)

#     # sample response is
#     """{'id': '96fb075d-b6bb-48bc-a5a7-06d4caefe629', 'prompt': {'text': '# write a function that takes a list of numbers and returns the sum of the numbers in the list', 'tokens': [{'generatedToken': {'token': '▁#', 'logprob': -6.482117176055908}, 'topTokens': None, 'textRange': {'start': 0, 'end': 1}}, {'generatedToken': {'token': '▁write', 'logprob': -9.705727577209473}, 'topTokens': None, 'textRange': {'start': 1, 'end': 7}}, {'generatedToken': {'token': '▁a▁function▁that', 'logprob': -8.42574691772461}, 'topTokens': None, 'textRange': {'start': 7, 'end': 23}}, {'generatedToken': {'token': '▁takes', 'logprob': -3.4382405281066895}, 'topTokens': None, 'textRange': {'start': 23, 'end': 29}}, {'generatedToken': {'token': '▁a▁list▁of', 'logprob': -2.4793195724487305}, 'topTokens': None, 'textRange': {'start': 29, 'end': 39}}, {'generatedToken': {'token': '▁numbers', 'logprob': -2.932746648788452}, 'topTokens': None, 'textRange': {'start': 39, 'end': 47}}, {'generatedToken': {'token': '▁and▁returns', 'logprob': -1.5038846731185913}, 'topTokens': None, 'textRange': {'start': 47, 'end': 59}}, {'generatedToken': {'token': '▁the▁sum▁of▁the', 'logprob': -3.2473959922790527}, 'topTokens': None, 'textRange': {'start': 59, 'end': 74}}, {'generatedToken': {'token': '▁numbers', 'logprob': -1.275012731552124}, 'topTokens': None, 'textRange': {'start': 74, 'end': 82}}, {'generatedToken': {'token': '▁in▁the▁list', 'logprob': -1.6785207986831665}, 'topTokens': None, 'textRange': {'start': 82, 'end': 94}}]}, 'completions': [{'data': {'text': '\n\n### 1.1.1\n\n### 1.1.2\n\n### 1.1.3\n\n### 1.1.4', 'tokens': [{'generatedToken': {'token': '<|newline|>', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 0, 'end': 1}}, {'generatedToken': {'token': '<|newline|>', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 1, 'end': 2}}, {'generatedToken': {'token': '▁#', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 2, 'end': 3}}, {'generatedToken': {'token': '##', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 3, 'end': 5}}, {'generatedToken': {'token': '▁', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 5, 'end': 6}}, {'generatedToken': {'token': '1', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 6, 'end': 7}}, {'generatedToken': {'token': '.', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 7, 'end': 8}}, {'generatedToken': {'token': '1', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 8, 'end': 9}}, {'generatedToken': {'token': '.', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 9, 'end': 10}}, {'generatedToken': {'token': '1', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 10, 'end': 11}}, {'generatedToken': {'token': '<|newline|>', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 11, 'end': 12}}, {'generatedToken': {'token': '<|newline|>', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 12, 'end': 13}}, {'generatedToken': {'token': '▁#', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 13, 'end': 14}}, {'generatedToken': {'token': '##', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 14, 'end': 16}}, {'generatedToken': {'token': '▁', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 16, 'end': 17}}, {'generatedToken': {'token': '1', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 17, 'end': 18}}, {'generatedToken': {'token': '.', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 18, 'end': 19}}, {'generatedToken': {'token': '1', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 19, 'end': 20}}, {'generatedToken': {'token': '.', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 20, 'end': 21}}, {'generatedToken': {'token': '2', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 21, 'end': 22}}, {'generatedToken': {'token': '<|newline|>', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 22, 'end': 23}}, {'generatedToken': {'token': '<|newline|>', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 23, 'end': 24}}, {'generatedToken': {'token': '▁#', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 24, 'end': 25}}, {'generatedToken': {'token': '##', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 25, 'end': 27}}, {'generatedToken': {'token': '▁', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 27, 'end': 28}}, {'generatedToken': {'token': '1', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 28, 'end': 29}}, {'generatedToken': {'token': '.', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 29, 'end': 30}}, {'generatedToken': {'token': '1', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 30, 'end': 31}}, {'generatedToken': {'token': '.', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 31, 'end': 32}}, {'generatedToken': {'token': '3', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 32, 'end': 33}}, {'generatedToken': {'token': '<|newline|>', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 33, 'end': 34}}, {'generatedToken': {'token': '<|newline|>', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 34, 'end': 35}}, {'generatedToken': {'token': '▁#', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 35, 'end': 36}}, {'generatedToken': {'token': '##', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 36, 'end': 38}}, {'generatedToken': {'token': '▁', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 38, 'end': 39}}, {'generatedToken': {'token': '1', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 39, 'end': 40}}, {'generatedToken': {'token': '.', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 40, 'end': 41}}, {'generatedToken': {'token': '1', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 41, 'end': 42}}, {'generatedToken': {'token': '.', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 42, 'end': 43}}, {'generatedToken': {'token': '4', 'logprob': 0.0}, 'topTokens': None, 'textRange': {'start': 43, 'end': 44}}]}, 'finishReason': {'reason': 'length', 'length': 40}}]}"""
