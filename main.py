import openai
import os
import time

openai.api_key = "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"

def ask_question(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        answer = response.choices[0].text
        return answer.strip()
    
    except openai.error.OpenAIError as e:
        print("Сталася помилка OpenAI:", e)
    except Exception as e:
        print("Сталася невідома помилка:", e)

question = input("Введіть запит: ")
answer = ask_question(question)
print(answer)