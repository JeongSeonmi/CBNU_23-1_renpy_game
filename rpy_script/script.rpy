## 파이썬 초기 설정
init python:
    myP = ""
    see_point = 0 
    main_point = 0

    #gpt-대화
    import npc
    import chatgpt
    import re

    #음악
    renpy.music.register_channel("music", mixer="music",loop = True)
    
    ####인벤토리 초기값 구현
    gold = 20 #starting amount
    inv = []
    seen_items = []
    #2# #crafting
    #2#known_recipes = []
    #2#seen_recipes = []
    #2#made_recipes = []
    #2#newitem = ""

## 게임에서 사용할 이미지(배경, 캐릭터 등) ##   
init :
    #방 이미지
    image bg_DT_office = "BG/DT_office.png"
    
    #캐릭터 이미지 
    image cr_Detective = im.FactorScale("CR/DT22.png", 0.9)
    image side cr_Detective idle = "/CR/side_idle_DT22.png" #사이드 이미지
    image cr_men1 = im.FactorScale("CR/men1.png", 1.3)
    $ style.window.left_padding= 220

    #인벤 이미지
    #image bg shop = Solid("#ffbedb")
    #image bg lab = Solid("#c3beff")S

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
        im.FactorScale("CR/im_cookie.jpg", 10)
        yalign 0.5
        xalign 0.5

    # 게임에서 사용할 캐릭터(이름, 이미지태그)
    define DT = Character('탐정', image="cr_Detective")
    define ch_request = Character('의뢰인', image="cr_Detective")
    define ch_men1 = Character("시민1", image="cr_Detective")
    define narrator = Character(None, kind = nvl,color = "#000000")
    define ch_narrator = Character(None)

    #------chatGPT API사용 예시------##연구 필요
    #init python:
    #    import openai  ##api키 보안 유의##
    #    openai.api_key = "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"

    # 추가 정의
    define item_cookie = InvItem(_("Cookie"), "item_cookie", 8, _("맛있는 테스트용 쿠키입니다!"), "item_cookie")
    define persistent.see_point = 0 
    define item_post = InvItem(_("post"), "item_post", 8, _("용의자들의 역할이 적힌 메모"), "item_post")
    define item_painting = InvItem(_("painting"), "item_painting", 8, _("값비싸 보이는 그림이다"), "item_painting")

    #screen icon_menu :
    #    hbox :
    #        spacing 10
    #        imagebutton :
    #            idle "gui/button/icon_menu.png"
    #            action Jump("[myP]_inventory")
    #        imagebutton :
    #                idle "gui/button/icon_map.png"
    #                action Show("[myP]_map")


## 게임 시작
label start:
    scene bg_DT_office with fade
    "\n\n추리 실력이 뛰어난 김탐정 탐정,\n개신동에서 탐정사무소를 오픈하게 되었다."
    nvl clear
    show cr_Detective at center
    DT "의뢰가 들어왔네"
    
    DT "사건 장소로 가볼까?"

    play music "audio/music/music_main.mp3" fadein 2 #음악 재생#

    "\n\n받은 의뢰에 따라 랜덤하게 이동할 예정\n 아직 프로토타입이라 정해서 이동"
    
    nvl clear
    menu :
        ##받은 의뢰에 따라 랜덤하게 이동할 예정이나 프로토타입에선 정해서 이동
        "병원" :
            jump hospital

        "회사" :
            jump company

        "별장" :
            jump villa
