"""
This module contains the code for the code generation model codex
"""

from time import sleep

import openai

from apikey import OPENAI_KEY
from human_eval.data import read_problems, write_jsonl

openai.api_key = OPENAI_KEY


def generate(prompt):
    """
    The generate function takes a prompt as input and returns the generated code.
    The prompt is a string of text that will be used to generate code. The function
    returns the generated code as a string.
    """

    try:
        sleep(3)

        response = openai.Completion.create(
            # model="code-cushman-001",
            model="code-davinci-002",
            prompt=prompt,
            temperature=0.2,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\nclass", "\ndef"],
        )
        sleep(20)
        code = response.choices[0].text
        print("".join([prompt, code]))
        return code

    except Exception as error:  # pylint: disable=broad-except
        print(error)
        print("Error")
        return ""


problems = read_problems()

NUM_SAMPLES_PER_TASK = 1
samples = [
    dict(task_id=task_id, completion=generate(problems[task_id]["prompt"]))
    for task_id in problems
    for _ in range(NUM_SAMPLES_PER_TASK)
]
write_jsonl("cd.jsonl", samples)
