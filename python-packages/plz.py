import requests
import json

# 테스트용 Data Set
subject_1 = '병원에서 살인 사건이 일어났다. 용의자 김민석, 유승환, 최가은, 정선미, 신재혁 중 범인이 있다고 한다. 김민석은 평소 피해자와 자주 다투던 사이였으며 사건 추정시간에는 유승환과 함께 급하게 밖으로 나가는 모습이 CCTV에 포착되었다. 최가은은 피해자와 채무 관계가 있다. 정선미는 피해자와 원한 관계에 있다. 신재혁은 사건 당시 화장실에 있다고 진술했다. 살해 추정 시간은 새벽 1시이며 침대 밑에서 주사기와 침대 옆 선반에 독성 물질이 발견되었다. '
subject_2 = '펜션에서 살인 사건이 일어났다. 용의자 김민석, 유승환, 최가은, 정선미, 신재혁 중 범인이 있다고 한다. 김민석은 평소 피해자와 친한 사이였으며 사건 추정시간에는 유승환과 함께 급하게 밖으로 나가는 모습이 CCTV에 포착되었다. 최가은은 피해자와 채무 관계가 있다. 정선미는 피해자의 담당 간호사이다. 신재혁은 사건 당시 화장실에 있다고 진술했다. 살해 추정 시간은 새벽 1시이며 침대 밑에서 피 묻은 칼과 침대 옆 선반에 수면제 가루가 발견되었다. '
subject_3 = '밀실에서 살인 사건이 일어났다. 용의자 김민석, 유승환, 최가은, 정선미, 신재혁 중 범인이 있다고 한다. 김민석은 평소 피해자와 원한 관계였으며 사건 추정시간에 유승환과 바로 옆방에 있었다고 주장한다. 최가은은 피해자와 절친한 사이이다. 정선미는 피해자와 직장 동료이다. 신재혁은 당시 화장실에 있다고 진술했다. 살해 추정시간은 오후 11시이며 밧줄과 바늘이 발견되었다. 바늘에는 독이 검출되었다. '
subject_4 = '회사에서 살인 사건이 일어났다. 용의자 김민석, 유승환, 최가은, 정선미, 신재혁 중 범인이 있다고 한다. 김민석은 평소 피해자와 회사 동료이며 사건 추정시간에는 유승환과 회의실에 있었다고 주장했다. 최가은은 피해자의 직장 상사이다. 정선미는 피해자와 직장 후재이다. 신재혁은 당시 화장실에 있다고 진술했다. 살해 추정시간은 오후 10시 30분이며 청소부의 증언에 따르면 쓰레기 통에 피 비린 냄새가 난다고 진술했다. 현재 증거로는 화장실 변기에 피 묻은 셔츠가 발견되었다. '

setting = ""
api_key = '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'

# gpt 통신 함수
def getResponse(messages, proxy=''):
    # Set the API endpoint URL for ChatGPT completions
    url = "https://api.openai.com/v1/chat/completions"

    # If a proxy is set, then it should use that instead
    if proxy is not None and proxy != '': url = proxy

    # Set the headers for the API request, including the Content-Type and Authorization with the API key
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Set the data for the API request, including the model and the input messages
    data = {
        "model": "gpt-3.5-turbo",
        "messages": messages
    }

    # Send the API request using the POST method, passing the headers and the data as JSON
    response = requests.post(url, headers=headers, data=json.dumps(data))
    # Check if the response status code is 200 (successful)
    if response.status_code == 200:
        # Extract the message from the response JSON and append it to the messages list
        completion = response.json()["choices"][0]["message"]
        messages.append(completion)
        return messages[-1]["content"]  # Return the updated messages list
    else:
        # If the status code is not 200, raise an exception with the error details
        raise Exception(f"Error: {response.status_code}, {response.text}")



# 상호작용에 관련된 함수들


# 주제 이외의 질문 거부 함수
def isReject(subject, user_input):
    message = []
    role = "주제 : [ " + subject + setting + " ] 질문이 주제와 관련이 없다고 생각되면 [EX]를 출력하고 관련이 있다면 [CR]를 출력해줘\n 예시 질문 : GPT가 뭐야? 답변 : [EX]"
    message.append({"role": "system", "content": role})
    message.append({"role": "user", "content": user_input})
    judge = getResponse(message)
    #print('판단 : ' + judge)

    if 'EX' in judge:
        return True
    else:
        return False


# 상호작용하는 함수
def person(subject, who, user_input):
    message = []
    message.append({"role": "system", "content": subject + "\n" + setting + "\n 이 이야기의 " + who + "(이)가 되어서 대화를 해줘"})

    if not isReject(subject, user_input):
        message.append({"role": "user", "content": user_input})
        npc_respone = getResponse(message)
        #message.append({"role": "assistant", "content": npc_respone})
        return npc_respone
    else:
        return '그 질문은 사건과 관계없는 것 같은데요'


# 게임 초기 세팅에 관련된 함수들


# 주제를 입력받아 긴 String(세팅값)으로 형식화해주는 함수
def getSetting(subject):
    message = []
    message.append({"role": "system", "content": "주제와 용의자를 통해 범인을 특정해서 살인사건 이야기를 만들어서 [범인: 범행도구: 사망원인: ]형태로 답변해줘"})
    message.append({"role": "user", "content": f"{subject}"})
    setstr = getResponse(message)
    # [범인: 범행도구: 사건줄거리: ] 형태로 값이 주어진다.
    #print(setstr)
    # getDetail(Setting)
    return setstr

    # 연구 중인 세세한 스토리 출력 함수


def getDetail(story):
    message = []
    message.append({"role": "system", "content": "너는 이번 살인사건의 범인이다. 주어진 정보를 토대로 살해동기를 만들어 변명해"})
    message.append({"role": "user", "content": f"{story}"})
    Detail = getResponse(message)
    #print(Detail)


# n(기본 6)개의 용의자 이름을 list형태로 반환하는 함수
def getName(n=6):
    message = []
    names = []
    message.append(
        {"role": "system", "content": "[1. 이름 (나이) 성별] 형태로 출력해줘 예를 들어 [1. 김민석 (23세) 남자] 나이는 20보다 크고 30보다 작게 설정해줘"})
    message.append({"role": "user", "content": f"성과 이름을 포함한 한국어 이름과 나이와 성별을 {n}개 출력해줘"})
    temp = getResponse(message).replace('\n', '.').split('.')

    for i in range(n):
        names.append(temp[i * 2 + 1])

    # [1. 김민수 (27세) 남자] 형태로 n개 출력된다
    #print(names)
    return names


# 게임에 필요한 정보가 담긴 객체
class GameInform:
    # 포멧팅된 문자열 string

    killer = ""  # killer	범인 string
    equipment = ""  # equipment	도구 string
    motivation = ""  # motivation 살해동기 string
    suspects = []  # 용의자
    victim = ""  # 피해자

    # 객체 초기화(세팅) 함수
    def __init__(self, subject):

        # 가끔씩 포멩팅이 안되는 경우 정해진 횟수 내에서 다시 실행하도록 하는 반복문
        e_count = 0
        while e_count < 2:

            # gpt에게 세팅값 받기
            global setting
            setting = getSetting(subject_1)
            e_count += 1
            # [범인: 범행도구: 사망원인: ] 형식으로 값이 주어진다.

            # 범인, 범행도구 파싱(추출)
            if '범인:' in setting and '범행도구: ' in setting:
                self.killer = setting[setting.find('범인:') + 4: setting.find('범행도구') - 1]
                self.equipment = setting[setting.find('범행도구: ') + 6:setting.find('사망원인') - 1]
                e_count = 200

        # 오류 처리
        if e_count < 200:
            print('CODE(10) 파싱 오류 발생')
            return

        # motivation = setting[setting.find('범행도구: ') + 6 :setting.find('사망원인')] 동기가 완성 안됨
        # 용의자 이름 자동 생성
        # self.suspects = settingHandler.getName()

    def getkiller(self):  # 문자열
        return self.killer

    def getequipment(self):  # 문자열
        return self.equipment

    def getmotivation(self):  # 문자열 ※ 작동안됨
        return self.motivation

    def getSuspects(self):  # 문자열 리스트
        return self.suspects

    def getSuspect(self, index):  # 문자열
        return self.suspects[index]


aaaa = GameInform(subject_2)
#person(subject_2 ,'김민석','문자열')
