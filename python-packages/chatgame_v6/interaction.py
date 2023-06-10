from chatgpt import getResponse

rej_react = ['네? 이해하기 힘드네요', '그걸 왜 물어보시는 거죠?', '대답하기 곤란하네요..', '(...)', ';;;;', '무슨 소리인지 잘 모르겠어요', '다른 질문을 해주세요', '대답하고 싶지 않네요']

class NPC:
    log = []
    who = ""
    subject = ""
    setting = ""
    role = f"주제 : [ {subject} {setting} ] 질문이 주제와 관련이 없다고 생각되면 [EX]를 출력하고 관련이 있다면 [CR]를 출력해줘\n 예시 질문 : GPT가 뭐야? 답변 : [EX]"

    def __init__(self, who, subject, setting):
        print(f'{who} 생성')

        self.who = who
        self.subject = subject
        self.setting = setting

        log.append({"role": "system", "content": f"{subject}\n{setting}\n 이 이야기의 {who}(이)가 되어서 대화를 해줘"})

    def dialog(self, message):
        if isReject(message):
            return rej_react[0]
        log.append({"role": "user", "content": message})
        npc_respone = getResponse(log)
        log.append({"role": "assistant", "content": npc_respone})

        return npc_respone

    # 주제 이외의 질문 거부 함수
    def isReject(user_input):
        message = []
        message.append({"role": "system", "content": role})
        message.append({"role": "user", "content": user_input})
        judge = getResponse(message)
        print('판단 : ' + judge)

        if 'EX' in judge:
            return True
        else:
            return False
