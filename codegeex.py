

"""
This module contains the code for the code generation model codegeex.
"""

import requests

from human_eval.data import read_problems, write_jsonl
NUM_SAMPLES_PER_TASK = 102


def generate(prompt: str) -> str:
    """
    The generate function takes a prompt as input and returns the generated code.
    The prompt is a string of text that will be used to generate code. The function
    returns the generated code as a string.

    :param prompt: Generate a code snippet
    :return: The code generated by the model
    """

    try:
        payload = {
            # "lang": "Python",
            "prompt": prompt,
            "n": 1,
            "apikey": "68cf004321e94b47a91c2e45a8109852",
            "apisecret": "e82b86a16f9d471ab215f653060310e3",
            "temperature": 0.8,
            "top_p": 1,
            "top_k": 0,
        }

        response = requests.post(
            "https://tianqi.aminer.cn/api/v2/multilingual_code_generate_adapt",
            json=payload,
            timeout=30,
        )

        response = response.json()
        print(response)
        code = response["result"]["output"]["code"][0]
        print(code)
        return code
    except Exception as error:  # pylint: disable=broad-except
        print(error)
        return ""


def get_samples() -> list:
    """
    This function gets the samples for the code generation model.
    :return: The samples for the code generation model
    """

    problems = read_problems()

    samples = [
        dict(task_id=task_id, completion=generate(problems[task_id]["prompt"]))
        for task_id in problems
        for _ in range(NUM_SAMPLES_PER_TASK)
    ]
    return samples


def main() -> None:
    """
    This function is the main function for the code generation model codegeex.
    """
    samples = get_samples()
    write_jsonl("cg102.jsonl", samples)


if __name__ == "__main__":
    main()
