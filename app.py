from openai import OpenAI

client = OpenAI(
    api_key="sk-c2a0b0a3b5aa4e1cb9a0a1dc0d76bea6",
    base_url="https://api.deepseek.com"
)

mbti = input("输入MBTI类型：")
question = input("请输入问题：")

prompt = f"""
用户MBTI类型：{mbti}
问题：{question}

请根据MBTI性格给出建议。
"""

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print(response.choices[0].message.content)
