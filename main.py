from apikey import cohere_key

import cohere


def generate_one_completion(prompt):
    try:
        co = cohere.Client(cohere_key)
        response = co.generate(
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
    except Exception as e:
        print(e)
        return "None"

from human_eval.data import write_jsonl, read_problems

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