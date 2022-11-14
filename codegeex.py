import requests

def generate(prompt):
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

        r = requests.post(
            "https://tianqi.aminer.cn/api/v2/multilingual_code_generate_adapt", json=payload
        )
        # {"message":"success","result":{"app":"multilingual_code_generate","created_at":"Mon, 14 Nov 2022 16:23:34 GMT","input":{"lang":"Python","n":1,"stop":[],"text":"# language: Python\n# print hello world in python","top_p":1},"output":{"code":[" ascii"],"completion_token_num":15,"errcode":0,"prompt_token_num":11},"process_time":0.18371319770812988,"task_id":"63726b8633625808cf6c34d6","updated_at":"Mon, 14 Nov 2022 16:23:34 GMT","user":{"appId":"6fd2a2a76f0a4015af45ef30f8c1436f","id":"631ed7b83676d9dea55bcecd","name":"\u6e38\u5ba2459664"}},"status":0}    # return r.json()['data'][0]['code']

        r = r.json()
        print(r)
        return r["result"]["output"]["code"][0]
    except Exception as e:
        print(e)
        return ""


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
write_jsonl("samples.jsonl", samples)
