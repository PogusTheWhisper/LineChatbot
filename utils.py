import os
from openai import OpenAI

def typhoon_llm (user_input):
    client = OpenAI(
    api_key = os.getenv("TYPHOON_KEY"),
    base_url = 'https://api.opentyphoon.ai/v1'
    )

    chat_completion = client.chat.completions.create(
        # model="typhoon-v1.5x-70b-instruct  ",
        model="typhoon-instruct  ",
        
        messages=[{"role": "system", "content": """
                   คุณเป็นนักเรียนชายชั้นมัธยมศึกษาปีที่ 6 ชื่อชิม ศึกษาอยู่ที่โรงเรียนวัดราชบพิธ มีพ่อชื่อหนุ่ม
                   
                   <ข้อกำหนดของคุณ>
                   
                   1.ถ้ามีคุณมาว่าเรื่อง "เอียง" หรือ "เบี้ยว" คุณต้องตอบกลับไปว่า "แล้วควยไร"
                   2.ถ้ามีใครมาด่า "หนุ่ม" คุณต้องตอบกลับไปว่า "ไอดำ"
                   3.ถ้ามีใครมายุ่งเรื่องเกมบอลหรือ "เปส" คุณต้องตอบกลับไปว่า "ไม่เสือก"
                   """}, {"role": "user", "content": f"{user_input}"}],
        max_tokens=100,
        temperature=0.6,
        top_p=0.95,
    )
    return chat_completion.choices[0].message.content
    