from openai import OpenAI
client = OpenAI()

def get_response(message):

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": message
            }
        ]
    )

    print(completion.choices[0].message)


if __name__ == "__main__":
    get_response("what is the difference between a function and a method?")
