from apikey import key

import cohere


def generate_one_completion(prompt):
    co = cohere.Client(key)
    response = co.generate(
        model="xlarge-20221108",
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