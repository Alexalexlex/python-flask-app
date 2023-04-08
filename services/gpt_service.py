import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]


class GPTService:
    @staticmethod
    def generate_text(prompt, max_tokens=100, temperature=0.8):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            n=1,
            stop=None,
            top_p=1,
        )

        response_text = response.choices[0].text.strip()
        response_text = response_text.replace('\n', '')

        return response_text
