from gptapi import getResponse
import random
import time

rej_react = ['네? 이해하기 힘드네요', '그걸 왜 물어보시는 거죠?', '대답하기 곤란하네요..', '(...)', ';;;;', '무슨 소리인지 잘 모르겠어요', '다른 질문을 해주세요', '대답하고 싶지 않네요', '하아.....', '사건과 관련있는 질문만 해주세요', '대화와 관련이 없어보이네요']

class NPC:
    log = []
    who = ""
    subject = ""
    setting = ""
    role = ""

    def __init__(self, who, subject, setting):
        print(f'{who} 생성')

        self.who = who
        self.subject = subject
        self.setting = setting
        self.role = f"주제: [{subject}\n{setting}]\n질문이 주제와 관련이 없다고 생각되면 [EX]를 출력하고 관련이 있다면 [CR]를 출력해줘"
        self.log.append({"role": "system", "content": f"{subject}\n{setting}\n 이 이야기의 {who}(이)가 되어서 대화를 해줘"})

    def dialog(self, message):
        if not self.who[1:] in message:
            print('이름이 없는 경우')
            message = self.who[1:] + " " + message
        if self.isReject(message):
            print('이름이 있음')
            return random.choice(rej_react)
        time.sleep(1)
        self.log.append({"role": "user", "content": message})
        npc_respone = getResponse(self.log)
        self.log.append({"role": "assistant", "content": npc_respone})

        return npc_respone

    # 주제 이외의 질문 거부 함수
    def isReject(self, user_input):
        message = []
        message.append({"role": "system", "content": self.role})
        message.append({"role": "user", "content": user_input})
        judge = getResponse(message)
        print('판단 : ' + judge)

        if 'EX' in judge:
            return True
        else:
            return False