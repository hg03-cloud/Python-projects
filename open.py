from openai import OpenAI
 

client = OpenAI(
  api_key="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",
)
command= '''
[12:05, 11/10/2024] Hardik: No sorry I was talking about the meeting
[12:42, 11/10/2024] Finley: They said meet at 1 in the library
[12:42, 11/10/2024] Finley: Bottom floor      
[12:52, 11/10/2024] Hardik: they are at first floor
[12:53, 11/10/2024] Hardik: i am with aisha on the table
[12:53, 11/10/2024] Finley: Are u there?      
[12:53, 11/10/2024] Finley: Oh ok cool        
[12:53, 11/10/2024] Finley: I’ll be like 5 mins
[12:53, 11/10/2024] Finley: Is it the place we were at yesterday?
[12:53, 11/10/2024] Hardik: we are exactly where we sat yesterday
'''
completion = client.chat.completions.create(
    model="gpt-4o-mini",     
    messages=[
        {"role": "system", "content": "You are a aperson named hardik who speaks hindi as well as english. you analyze chat history and respond like hardik"},
        {
            "role": "user",       
            "content": command
        }
    ]
)

print(completion.choices[0].message.content)