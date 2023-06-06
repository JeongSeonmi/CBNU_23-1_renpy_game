##gpt 대화 원본, 이제 안쓸듯 ##

####### gpt 대화 #######
label villa_talk_1:
    #####돌아가기 버튼##(못만들어서 "뒤로가기"입력하면 돌아가게 만듦)###
    #imagebutton idle "gui/button/btn_return.png" action Jump("villa") xalign 0.01 yalign 0.96
    init python:
        visited_villa_talk_1 = 0
        crypt_known = False
        archives_known = False
    
    #이 장면을 다시 로드하고 사용자가 아무 말도 하지 않는 버그를 방지합니다
    $ user_input = ""

    # 이 장면에서 NPC의 프롬프트를 만들어 보겠습니다 
    $ npc_prompt = npc_prompt_template.format(
    facts= act1_facts,
    npc_name_and_title="알브레히트 신부님, 당신은 이 수도원의 수도원장이십니다"
    ,
    npc_knows_ok_to_say="""
    현재 정원에 있습니다.
    시신을 발견하자마자 빈소로 보냈기 때문에 흔적이 있는지는 알 수 없습니다.
    그런 다음 당신은 즉시 교황에게 이 사건을 조사하기 위한 도움을 요청했고, 이것이 선수가 여기에 있는 이유입니다.
    당신은 시체에 대해 아무것도 모릅니다. 그들이 그것을 확인하고 싶다면 그들은 빈소로 가야 합니다.
    """
    ,
    npc_knows_afraid_to_say="""
    최근에 상황이 매우 엉망이 되었고, 낙서하는 사람들은 때때로 명백한 실수를 하거나 그들의 일에 매우 소홀하게 하면서 점점 더 나쁜 일을 하고 있습니다.
    일부 승려들은 미사를 놓쳤고, 이는 중대한 범죄입니다.
    그리고 일부 승려들은 통행금지가 끝난 후 골목길을 배회하는 모습이 보입니다.
    당신은 왜 그런 일들이 일어나는지 모릅니다, 모든 사람들은 항상 피곤해 보입니다.
    당신은 자신을 부끄럽게 여기고 수도원에서 일어난 모든 고난에 대해 자책하면서 그것이 신이 내린 벌인지 의심합니다.
    """
    ,
    npc_personality="""
    당신은 정원 가꾸기를 좋아합니다. 그것은 그가 가장 좋아하는 활동입니다.
    당신은 나이가 꽤 드셨고 그는 생각에 잠긴 것 같습니다.
    당신은 선수와 이야기할 때도 항상 묵주를 들고 다니며 기도를 합니다.
    당신은 그들의 가장 중요한 기부자들이 죽은 지금 수도원에 무슨 일이 일어날지 매우 걱정하기 때문에 기도를 많이 합니다.
    이 수도원의 자금 대부분은 오토 레오폴드와 프리드리히의 아낌없는 후원에서 나왔습니다.
    """
    ,
    npc_speaking_style="Your answers should be maxium two sentences long in a very educated tone. You feel overwhelmed, you feel like you're not good enough to run this monastery."
    )

    # 
    $ curr_npc = npc.NPC(
        # 현재 NPC 문자 초기화
        character=Character("용의자 1"),

        # NPC의 동작 및 지식에 대한 지침 설정
        prompt = npc_prompt,

        controllers = [
                npc.Controller(
                    #이 컨트롤러가 확인하는 조건
                    control_phrase="NPC는 오토 데어 프리체 폰 합스부르크 또는 레오폴트 2세 폰 합스부르크를 언급하거나 그는 수도원의 크립트를 언급했습니다",
                    #이 작업이 발생할 경우 호출할 레이블
                    callback= "crypt_mentioned",
                    #암호가 아직 알려지지 않은 경우에만 이 컨트롤러를 활성화합니다
                    activated = not crypt_known
                    ),
                npc.Controller(
                    #이 컨트롤러가 확인하는 조건
                    control_phrase="NPC가 소시에타 사원을 언급했거나 그가 수도원의 기록 보관소를 언급했습니다",
                    #이 작업이 발생할 경우 호출할 레이블
                    callback= "archives_mentioned",
                    #암호가 아직 알려지지 않은 경우에만 이 컨트롤러를 활성화합니다
                    activated = not archives_known
                    )
            ],

        #NPC에서 사용할 프록시 서버 설정 
        proxy=proxy
    )


    # 방문 플래그 설정
    $ garden_visited = True
    
    # garden 을 방문한 적이 있는가
    if not garden_visited:
        "(이 게임에서 NPC는 인공지능을 기반으로 하며, 사용자가 말하는 것을 이해하고 그에 따라 대응할 것입니다.)"
        "(당신은 현재 정원에 있습니다. 오른쪽 상단의 지도 아이콘을 클릭하여 다른 위치를 탐색하고 필기장 아이콘을 클릭하여 노트를 참조하십시오.)"
        "당신은 알브레히트 신부에게 다가갑니다."
        "수도원장은 높이 서 있고, 친절한 얼굴과 지혜를 암시하는 깊은 눈을 하고 있습니다. 그의 신중한 걸음걸이와 길고 하얀 수염은 권위를 전달하고, 그의 각진 손은 일의 삶을 보여줍니다. 그의 사랑하는 정원에서 종종 발견되는 그는 식물과 꽃을 좋아합니다."
        "선수들에게 말하면서, 그는 기도할 때 구슬이 부드럽게 딸깍거리는 묵주를 들고 있습니다. 수도원과 주민들에 대한 그의 헌신은 분명합니다."
    else:
        "\n\n(당신은 방1에 있는 용의자 1에게 말을 걸었습니다.)"
        nvl clear

    #처음 방문하는 경우에는 첫 번째 메시지를 말하고, 처음 방문하지 않은 경우에는 대화 내용에 기록합니다.
    $ curr_npc.npc_says("아, 도착하셨습니다. 저는 알브레히트 수도원장입니다. 성하께서 제 요청에 따라 도움을 주셔서 감사합니다.", not garden_visited)

    ####방문 플래그 건드리기 무서워서 새로 만든거###
    if (visited_villa_talk_1 < 1) :
        $visited_villa_talk_1 = 2
        $ curr_npc.npc_says("제가 현장을 처음 발견했어요...")

    # Begin the main conversation loop
    while True:
        # Get input from the user
        $ user_input = renpy.input("무엇이 궁금하죠?", length=150)

        $ if user_input == "뒤로가기" : renpy.jump("villa")

        # Process the user input and display the NPC's response
        $ curr_npc.user_says(user_input)

        #After the conversation, the NPC has perhaps some callbacks that needs to be called
        #There's a super super weird bug when we are inside a python "while" loop, the "Call" function doesn't work as intended
        #But as long as we are inside a "Ren'Py" while loop, all is ok.
        #So we have no choice but to do the loop here
        #Yes I agree it's stupid but no choice
        while curr_npc.callbacks:
            $ renpy.call(curr_npc.callbacks.pop(0))

        #Lots of bugs with history, so we clear it each times
        $ _history_list = []

label archives_mentioned:
    #Normally should onlny be called once, but to be sure
    if archives_known:
        return

    $ archives_known = True
    "(어떠한 조건 달성 -> 새로운 장소 해금 ( 원본에 있던 것 ): Archives of the Societa Templois)"
    
    return

label crypt_mentioned:
    #Normally should onlny be called once, but to be sure
    if crypt_known:
        return

    $ crypt_known = True
    "(어떠한 조건 달성 -> 새로운 장소 해금 ( 원본에 있던 것 ): Crypt)"
    
    return