## 파이썬 초기 설정
init python:
    see_point = 0 
    visit_hospital = 0
    visit_company = 0
    visit_villa = 0
    myP = ""
    last_inventory=False
    ending_point=0

    killer_item = InvItem(_("컴퓨터"), "company_computer", 8,
    _("작업 중이던 컴퓨터 이다"), "company_computer")


    #gpt-대화
    import npc
    import chatgpt
    import re
    import plz

    #음악
    renpy.music.register_channel("music", mixer="music",loop = True)
    renpy.music.register_channel("music", mixer="music",loop = True)
    ####인벤토리 초기값 구현
    gold = 0 #추리점수
    inv = []
    seen_items = []


init :
    #방 이미지
    image loading = "BG/loading.png"
    image bg_DT_office = "BG/DT_office.png"
    image bg_lab = "gui/Background.jpg"
    
    define persistent.see_point = 0

## 게임 시작
label start:
    stop music
    play music "audio/music/music_office.mp3"
    ###로딩창 - 5초동안 클릭 안됨
    scene loading with fade
    $ renpy.pause(5.0, hard=True)
    ##GPT 초기설정 하는 공간
    $ story_set= plz.getSetting('병원에서 살인 사건이 일어났다. 용의자 김민석, 유승환, 최가은, 정선미, 신재혁 중 범인이 있다고 한다. 김민석은 평소 피해자와 자주 다투던 사이였으며 사건 추정시간에는 유승환과 함께 급하게 밖으로 나가는 모습이 CCTV에 포착되었다. 최가은은 피해자와 채무 관계가 있다. 정선미는 피해자와 원한 관계에 있다. 신재혁은 사건 당시 화장실에 있다고 진술했다. 살해 추정 시간은 새벽 1시이며 침대 밑에서 주사기와 침대 옆 선반에 독성 물질이 발견되었다. ')
    



    scene bg_DT_office with dissolve
    "\n\n추리 실력이 뛰어난 김탐정 탐정,\n개신동에서 탐정사무소를 오픈하게 되었다."
    nvl clear

    show cr_Detective at left
    DT "재미있는 사건이 있으면 좋겠는데.."
    show cr_police at right
    ch_police "김탐정, 오랜만이야"
    DT "자네가 여기 왔다는 건... 당연히 흥미로운 사건이겠지?"
    ch_police "우리한테는 골치아픈 일이지"
    DT "내 기대를 저버리지 않았으면 좋겠군."
    hide cr_police
    show cr_Detective at center

    DT "사건 장소로 가볼까?"
    ##스토리 셋팅 (미완)##
    ##장소만 변수로 받아서 [장소]로 이동시켜야 함.
    ## 용의자 목록/ 범행도구/ 범인은 각각 변수로 만들어서 저장 후, 범인과 범행도구는 ending에서 사용, 용의자 목록과 사건 개요는 label 이동 후 경찰이 말해 주어야 함
    "[story_set]" 
    ##  ##
    
    nvl clear
    
    
    menu :
        ##받은 의뢰에 따라 랜덤하게 이동할 예정이나 프로토타입에선 정해서 이동
        "병원" :
            play music "audio/music/music_main.mp3" fadein 2 #음악 재생#
            $ visit_hospital = 1
            $ myP = "hospital"
            jump hospital

        "회사" :
            play music "audio/music/music_main.mp3" fadein 2 #음악 재생#
            $ visit_company = 1
            $ myP = "company"
            jump company

        "별장" :
            play music "audio/music/music_main.mp3" fadein 2 #음악 재생#
            $ visit_villa = 1
            $ myP = "villa"
            jump villa