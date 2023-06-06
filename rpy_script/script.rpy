## 파이썬 초기 설정
init python:
    see_point = 0 
    visit_hospital = 0
    visit_company = 0
    visit_villa = 0
    myP = ""

    #gpt-대화
    import npc
    import chatgpt
    import re
    import plz

    #음악
    renpy.music.register_channel("music", mixer="music",loop = True)
    
    ####인벤토리 초기값 구현
    gold = 20 #starting amount
    inv = []
    seen_items = []


## 게임에서 사용할 이미지(배경, 캐릭터 등) ##   
init :
    #방 이미지
    image bg_DT_office = "BG/DT_office.png"
    image bg_lab = "gui/Background.jpg"
    
    #캐릭터 이미지 
    image cr_Detective = im.FactorScale("CR/DT.png", 0.9)
    image side cr_Detective idle = "/CR/DT_side_idle.png" #사이드 이미지
    image cr_men1 = im.FactorScale("CR/men1.png", 1.3)
    image cr_men1 idle = "/CR/men1_idle.png" #사이드 이미지
    image cr_police = im.FactorScale("CR/police.png", 1.7)
    $ style.window.left_padding = 220

    #상호작용 버튼 이미지
    image find_idle_btn = im.FactorScale("gui/button/find_idle_ui.png", 0.6)
    image talk_idle_btn = im.FactorScale("gui/button/talk_idle_ui.png", 0.6)
    image find_hover_btn = im.FactorScale("gui/button/find_ui.png", 0.6)
    image talk_hover_btn = im.FactorScale("gui/button/talk_ui.png", 0.6)

    #증거품 이미지 *이름 변수명 다시 지어야함
    image item_hint1 : #메모
        im.FactorScale("Items/pngegg.png", 0.5)
        xpos 720
        ypos 245
    image item_hint2 : #거실 그림
        "Items/monariza.png" 
        xpos 720
        ypos 245

    image item_hint3 : #유리컵
        im.FactorScale("Items/Glass.jpg", 0.4) 
        xpos 720
        ypos 300
    
    image item_hint4 : #방1 그림
        im.FactorScale("Items/room1_painting.png", 0.6) 
        xpos 720
        ypos 300

    image image_cookie : #인벤토리 테스트용
        im.FactorScale("Items/item_cookie.jpg", 10)
        yalign 0.5
        xalign 0.5

    #병원 증거 이미지
    image image_cookie : #인벤토리 테스트용
        im.FactorScale("Items/item_cookie.jpg", 10)
        yalign 0.5
        xalign 0.5
    image item_hospital_drug: #인벤토리 테스트용
        im.FactorScale("Items/item_hospital_drug.jpg", 10)
        yalign 0.5
        xalign 0.5
    image item_hospital_knife: #인벤토리 테스트용
        im.FactorScale("Items/item_hospital_knife.jpg", 10)
        yalign 0.5
        xalign 0.5
    image item_hospital_sytinge: #인벤토리 테스트용
        im.FactorScale("Items/item_hospital_sytinge.jpg", 10)
        yalign 0.5
        xalign 0.5

    #회사 증거 이미지
    image item_company_computer: #인벤토리 테스트용
        im.FactorScale("Items/item_company_computer.jpg", 10)
        yalign 0.5
        xalign 0.5
    image item_company_hotsix: #인벤토리 테스트용
        im.FactorScale("Items/item_company_hotsix.jpg", 10)
        yalign 0.5
        xalign 0.5
    image item_company_cctv: #인벤토리 테스트용
        im.FactorScale("Items/item_company_cctv.jpg", 10)
        yalign 0.5
        xalign 0.5
    image item_company_knife: #인벤토리 테스트용
        im.FactorScale("Items/item_company_knife.jpg", 10)
        yalign 0.5
        xalign 0.5
    image item_company_nameteg: #인벤토리 테스트용
        im.FactorScale("Items/item_company_nameteg.jpg", 10)
        yalign 0.5
        xalign 0.5

    #별장 증거 이미지    
    image item_villa_gun: #인벤토리 테스트용
        im.FactorScale("Items/item_villa_gun.jpg", 10)
        yalign 0.5
        xalign 0.5
    image item_villa_knife: #인벤토리 테스트용
        im.FactorScale("Items/item_villa_knife", 10)
        yalign 0.5
        xalign 0.5
    image item_villa_rope: #인벤토리 테스트용
        im.FactorScale("Items/item_villa_rope", 10)
        yalign 0.5
        xalign 0.5
    image item_villa_saw: #인벤토리 테스트용
        im.FactorScale("Items/item_villa_saw.jpg", 10)
        yalign 0.5
        xalign 0.5
    
    # 게임에서 사용할 캐릭터(이름, 이미지태그)
    define DT = Character('탐정', image="cr_Detective")
    define ch_request = Character('의뢰인', color = "#000000")
    define ch_men1 = Character("용의자 1", color = "#000000")
    define narrator = Character(None, kind = nvl,color = "#000000")
    define ch_narrator = Character(None)
    define ch_police = Character('경찰', color = "#000000")

    # 증거 정의
    define item_cookie = InvItem(_("Cookie"), "item_cookie", 8, _("맛있는 테스트용 쿠키입니다!"), "item_cookie")
    define item_post = InvItem(_("post"), "item_post", 8, _("용의자들의 역할이 적힌 메모"), "item_post")
    define item_painting = InvItem(_("painting"), "item_painting", 8, _("값비싸 보이는 그림이다"), "item_painting")

    #추가 정의
    define persistent.see_point = 0

## 게임 시작
label start:
    scene bg_DT_office with fade
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
    $ story_set= plz.getSetting('병원에서 살인 사건이 일어났다. 용의자 김민석, 유승환, 최가은, 정선미, 신재혁 중 범인이 있다고 한다. 김민석은 평소 피해자와 자주 다투던 사이였으며 사건 추정시간에는 유승환과 함께 급하게 밖으로 나가는 모습이 CCTV에 포착되었다. 최가은은 피해자와 채무 관계가 있다. 정선미는 피해자와 원한 관계에 있다. 신재혁은 사건 당시 화장실에 있다고 진술했다. 살해 추정 시간은 새벽 1시이며 침대 밑에서 주사기와 침대 옆 선반에 독성 물질이 발견되었다. ')
    
    "[story_set]" 
    ##  ##
    play music "audio/music/music_main.mp3" fadein 2 #음악 재생#
    nvl clear
    
    
    menu :
        ##받은 의뢰에 따라 랜덤하게 이동할 예정이나 프로토타입에선 정해서 이동
        "병원" :
            $ visit_hospital = 1
            $ myP = "hospital"
            jump hospital

        "회사" :
            $ visit_company = 1
            $ myP = "company"
            jump company

        "별장" :
            $ visit_villa = 1
            $ myP = "villa"
            jump villa