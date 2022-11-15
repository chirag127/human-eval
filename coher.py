"""
This module contains the code for the code generation model codex.
"""


import cohere
from apikey import COHERE_KEY
from f import get_samples
from human_eval.data import write_jsonl


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
            model="large",
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
    write_jsonl(f"cohere-{NUM_SAMPLES_PER_TASK}.jsonl", samples)


if __name__ == "__main__":
    main()
