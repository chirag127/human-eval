"""
This module contains the functions for generating code completions in cohere
"""

import cohere

from apikey import COHERE_KEY
from human_eval.data import read_problems, write_jsonl


def generate_one_completion(prompt):
    """# This function generates one completion for a given prompt.
    # It takes the prompt as input, and returns the completion as output.
    # The prompt is a string.
    # The completion is a string.
    # The prompt is a single word.
    # The completion is a single word.
    # The prompt is a prefix of the completion.
    # The prompt is a single word.
    # The completion is a single word.
    # The prompt is a prefix of the completion.
    """

    try:
        cohere_client = cohere.Client(COHERE_KEY)
        response = cohere_client.generate(
            model="medium",
            prompt=prompt,
            max_tokens=100,
            temperature=0,
            k=0,
            p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop_sequences=[],
            return_likelihoods="NONE",
        )
        return response.generations[0].text
    except Exception as error:  # pylint: disable=broad-except
        print(error)
        return "None"


problems = read_problems()

num_samples_per_task = 1
samples = [
    dict(
        task_id=task_id, completion=generate_one_completion(problems[task_id]["prompt"])
    )
    for task_id in problems
    for _ in range(num_samples_per_task)
]
write_jsonl("samples.jsonl", samples)

# print(generate_one_completion("write python code for the hello world"))
