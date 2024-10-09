from openai import OpenAI
 

client = OpenAI(
  api_key="your key",
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "what is full form of html."},
        {
            "role": "user",
            "content": "what is coding."
        }
    ]
)

print(completion.choices[0].message)
