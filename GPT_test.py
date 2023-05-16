import openai

openai.api_key = "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"

messages = []
while True:
    user_content = input("user : ")
    messages.append({"role": "user", "content": f"{user_content}"})
    messages.append({"role": "system", "content": "주제를 입력해주면 추리소설을 만들어주고 [범인: 범행도구: 용의자: 사건줄거리: ]형태로 답변해줘"})

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    assistant_content = completion.choices[0].message["content"].strip()

    messages.append({"role": "assistant", "content": f"{assistant_content}"})


    print(f"GPT : {assistant_content}")