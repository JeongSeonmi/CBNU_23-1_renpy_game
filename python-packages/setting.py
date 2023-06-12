from gptapi import getResponse
import time
import random

# 게임 초기 세팅에 관련된 함수들

# 주제를 입력받아 긴 String(세팅값)으로 형식화해주는 함수
def getSetting(subject):
    message = []
    message.append({"role": "system", "content": "주제와 용의자를 통해 범인을 특정해서 살인사건 이야기를 만들어서 [범인: 범행도구: 사망원인: ]형태로 답변해줘"})
    message.append({"role": "user", "content": f"{subject}"})
    setstr = getResponse(message)
    # [범인: 범행도구: 사건줄거리: ] 형태로 값이 주어진다.
    print(setstr)
    # getDetail(Setting)
    return setstr

# 연구 중인 세세한 스토리 출력 함수
def getDetail(story):
    message = []
    message.append({"role": "system", "content": "너는 이번 살인사건의 범인이다. 주어진 정보를 토대로 살해동기를 만들어 변명해"})
    message.append({"role": "user", "content": f"{story}"})
    Detail = getResponse(message)
    print(Detail)


# n(기본 6)개의 용의자 이름을 list형태로 반환하는 함수
def getName(n=3):
    message = []
    names = []
    message.append({"role": "system", "content": "[1. 이름] 형태로 출력해줘 예를 들어 [1. 김민석]"})
    message.append({"role": "user", "content": f"성과 이름을 포함한 한국어 이름을 {n}개 출력해줘"})
    temp = getResponse(message).replace('\n', '.').split('.')

    for i in range(n):
        names.append(temp[i * 2 + 1].strip())

    # [1. 김민수] 형태로 n개 출력된다
    print(names)
    return names

def getSubject(choice, names):
    relation = ['채무 관계이다.', '원한 관계이다.', '회사 동료이다.', '친한 친구이다.', '초면이다.', '약간의 다툼이 있었디.', '부하 직원이다.']
    random.shuffle(relation)
    action = ['밖에 있었다고 주장했다.', '밖에 있었다고 주장했지만 CCTV에는 나가지 않을 것으로 확인되었다.', '화장실에 있었다고 주장한다.', 'CCTV에 급하게 현장을 떠나는 모습이 확인되었다.', '간식을 먹었다고 진술했다.']

    if choice == '병원':
        room1 = '진료실 101호'
        room2 = '진료실 102호'
        room3 = '병실'
        room1_e = ['에서 사건과 관련이 있어보이는 메모가 발견되었다.', ' 서랍 안에서 메스가 발견되었다.', '에서 사건과 관려이 있어보이는 서류파일이 발견되었다.']
        room2_e = ['에서 책장 위에 커터칼이 발견되었다.', '의 서랍장 안에서 주사기가 발견되었다.']
        room3_e = [' 침대 밑에서 독성물질이 발견되었다.', ' 창가에 깨져있는 화분이 발견되었다.', ' 서랍에서 음료수 병이 발견되었다.', '에서 피해자 DNA가 묻은 커튼이 발견되었다.', '에서 의심스럽게 찢어진 베개가 발견되었다.']
    elif choice == '회사': 
        room1 = '사무실 201호'
        room2 = '사무실 202호'
        room3 = '휴게실'
        room1_e = [' 서랍 안에서 커터칼이 발견되었다.']
        room2_e = ['에서 스테이플러가 발견되었다.']
        room3_e = ['에서 범행 도구로 의심되는 커피포트가 발견되었다.', '에서 목을 조를 수 있는 전선이 발견되었다.', '에서 전기충격기가 발견되었다.']
    else : 
        room1 = '1번 방'
        room2 = '2번 방'
        room3 = '거실'
        room1_e = [' 서랍에서 총을 발견하였다.', ' 장식장 위에 무거워 보이는 장식물이 발견되었다.']
        room2_e = ['에서 화장대 위 장식물을 발견하였다.', ' 탁자 위에서 식칼을 발견하였다.', '에서 주사기가 발견되었다.', '에서 찢어져 있는 베개를 발견하였다.']
        room3_e = ['에서 장식장 속 밧줄을 발견하었다.', '에서 테이블 밑 유리조각을 발견하였다.', ' 문 옆에 톱이 발견되었다.']

    subject = f'{choice}에서 살인 사건이 일어났다. 용의자 {names[0]}, {names[1]}, {names[2]} 중 범인이 있다고 한다. {names[0]}은 피해자와 {relation[0]} 사건 추정시간에 {names[1]}은 {action[0]} {names[2]}은 피해자와 {relation[1]} 살해 추정 시간은 새벽 1시이다. 수사 결과 {room1}{random.choice(room1_e)} 또한 {room2}{random.choice(room2_e)} 그리고 {room3}{random.choice(room3_e)}'
    #'병원에서 살인 사건이 일어났다. 용의자 김민석, 유승환, 최가은, 정선미, 신재혁 중 범인이 있다고 한다. 김민석은 평소 피해자와 자주 다투던 사이였으며 사건 추정시간에는 유승환과 함께 급하게 밖으로 나가는 모습이 CCTV에 포착되었다. 최가은은 피해자와 채무 관계가 있다. 정선미는 피해자와 원한 관계에 있다. 신재혁은 사건 당시 화장실에 있다고 진술했다. 살해 추정 시간은 새벽 1시이며 침대 밑에서 주사기와 침대 옆 선반에 독성 물질이 발견되었다. '
    print(subject)
    return subject


# 게임에 필요한 정보가 담긴 객체
class GameInform:
    # 포멧팅된 문자열 string

    killer = ""  # killer	범인 string
    equipment = ""  # equipment	도구 string
    motivation = ""  # motivation 살해동기 string
    suspects = []  # 용의자
    victim = ""  # 피해자

    subject = "" # 주제
    setting = "" # 세팅 값

    # 객체 초기화(세팅) 함수
    def __init__(self, choice):

        # 용의자 이름 자동 생성
        self.suspects = getName()
        time.sleep(0.5)
        # 주제 생성
        self.subject = getSubject(choice, self.suspects)
        
        # 가끔씩 포멩팅이 안되는 경우 정해진 횟수 내에서 다시 실행하도록 하는 반복문
        e_count = 0
        while e_count < 2:
            time.sleep(0.5)
            # gpt에게 세팅값 받기
            self.setting = getSetting(self.subject)
            e_count += 1
            # [범인: 범행도구: 사망원인: ] 형식으로 값이 주어진다.

            # 범인, 범행도구 파싱(추출)
            if '범인:' in self.setting and ('범행도구: ' in self.setting or '범행 도구: ' in self.setting):
                self.killer = self.setting[self.setting.find('범인:') + 4: self.setting.find('범행') - 1]
                self.equipment = self.setting[self.setting.find('도구: ') + 4:self.setting.find('사망원인') - 1]
                e_count = 200

        # 오류 처리
        if e_count < 200:
            print('CODE(10) 파싱 오류 발생')
            return

        # motivation = setting[setting.find('범행도구: ') + 6 :setting.find('사망원인')] 동기가 완성 안됨
        

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
    
    def getSub(self):
        return self.subject
    
    def getSet(self):
        return self.setting