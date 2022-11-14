import os
import openai
from apikey import openai_key

openai.api_key = openai_key

def generate(p):

    response = openai.Completion.create(
  model="code-cushman-001",
  prompt=p,
  temperature=0.2,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["\nclass", "\ndef"]
)
    sleep(3)
    code = response.choices[0].text
    return code



from human_eval.data import write_jsonl, read_problems

problems = read_problems()

num_samples_per_task = 1
samples = [
    dict(
        task_id=task_id, completion=generate(problems[task_id]["prompt"])
    )
    for task_id in problems
    for _ in range(num_samples_per_task)
]
write_jsonl("cush.jsonl", samples)

# print(generate("# Write a function that takes a string and returns a string")  )
