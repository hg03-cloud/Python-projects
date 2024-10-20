import pyautogui
import time
import pyperclip
from openai import OpenAI
client = OpenAI(
  api_key="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",
)
# def last(chat_log, sender_name='Rakshim Bhaiya'):
   
#     messages= chat_log.strip().split("/2024]")[-1]
#     if sender_name in messages:
#         return True
#     return False
pyautogui.click(1078,1148 )
time.sleep(0.5)


    #     a= pyautogui.position()
    #     print(a)
    # 612, 269
    # 705,1016
    
 

pyautogui.moveTo(690,300)
pyautogui.dragTo(1858,1100, duration=0.5,button='left')
pyautogui.hotkey("ctrl","c")
pyautogui.click(1858,1000)
time.sleep(0.5)
text = pyperclip.paste()
print(text )

# if last(text): 
completion = client.chat.completions.create(
    model="gpt-4o-mini",     
    messages=[
        {"role": "system", "content": "You are a a person named hardik who is funny . He speaks in  english. you analyze chat history and respond as hardik(text messages only). "},
        {
            "role": "user",       
            "content": text
        }
    ]
)

response=completion.choices[0].message.content
pyperclip.copy(response)

pyautogui.click(1692,1076)
time.sleep(0.5)

pyautogui.hotkey('ctrl','v')
time.sleep(0.5)
