import gradio as gr
from openai import OpenAI

client = OpenAI(
    api_key="sk-c2a0b0a3b5aa4e1cb9a0a1dc0d76bea6",
    base_url="https://api.deepseek.com"
)

def mbti_ai(mbti, question):

    prompt = f"""
    你是一名MBTI人格专家。

    用户人格：{mbti}

    用户问题：{question}

    请根据MBTI人格特点进行分析回答。
    """

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


demo = gr.Interface(
    fn=mbti_ai,
    inputs=[
        gr.Textbox(label="你的MBTI"),
        gr.Textbox(label="你的问题")
    ],
    outputs="text",
    title="MBTI AI 人格助手",
    description="输入MBTI类型和问题，AI会根据人格为你分析"
)

demo.launch()
