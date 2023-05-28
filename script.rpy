## 파이썬 초기 설정
init python:
    renpy.music.register_channel("music", mixer="music",loop = True)
    see_point = 0 #추리점수
    see_point_room1 = False 
    see_point_1bed = 0
    see_point_Shelf = 0
    see_point_1painting = 0

    see_point_room2 = False
    see_point_2bed = 0
    see_point_dressing_table = 0
    see_point_Table = 0
    

    see_point_living = False
    see_point_post = 0
    see_point_Lpainting = 0

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
    image bg_villa = "BG/villa1.jpg"   
    image bg_villa_living = "BG/villa_living.png"
    image bg_villa_room1 = "BG/villa_room1.jpg"
    image bg_villa_room2 = "BG/villa_room2.jpg"
    image bg_DT_office = "BG/DT_office.png"

    #캐릭터 이미지 
    image cr_Detective = im.FactorScale("CR/DT22.png", 0.9)
    image side cr_Detective idle = "/CR/side_idle_DT22.png" #사이드 이미지
    $ style.window.left_padding= 220

    #인벤 이미지
    #image bg shop = Solid("#ffbedb")
    #image bg lab = Solid("#c3beff")

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

## 방1 증거찾기
screen room1_search : 
    imagemap :
        ground "BG/villa_room1.jpg"
        hotspot(1157, 714, 368, 168) action Return("room1_Bed")
        hotspot(199, 778, 172, 118) action Return("Shelf")
        hotspot(522, 390, 136, 172) action Return("room1_painting")
        imagebutton idle "gui/button/btn_return.png" action Jump("villa") xalign 0.01 yalign 0.96

## 방2 증거찾기
screen room2_search : 
    imagemap :
        ground "BG/villa_room2.jpg"
        hotspot(1229, 683, 317, 112) action Return("room2_Bed")
        hotspot(531, 602, 197, 144) action Return("dressing_table")
        hotspot(891, 669, 266, 70) action Return("Table")
        imagebutton idle "gui/button/btn_return.png" action Jump("villa") xalign 0.01 yalign 0.96

## 거실 증거찾기
screen living_search : 
    imagemap :
        ground "BG/villa_living.png"
        hotspot(289, 594, 42, 40) action Return("post")
        hotspot(779, 328, 180, 143) action Return("living_painting")
        hotspot(1654, 449, 125, 118) action Return("test3")
        imagebutton idle "gui/button/btn_return.png" action Jump("villa") xalign 0.01 yalign 0.96
            
screen test3 :  ##이미지 버튼 기능, 이미지 자체가 버튼 기능을 하는데 아직은 사용X
    imagebutton idle "Item/pngegg.png" :
        action Hide("test3")

## 게임 시작
label start:
    scene bg_DT_office with fade
    "\n\n추리 실력이 뛰어난 김탐정 탐정,\n개신동에서 탐정사무소를 오픈하게 되었다."
    nvl clear
    show cr_Detective at center
    DT "의뢰가 들어왔네"
    
    DT "사건 장소로 가볼까?"

    play music "audio/music/music_main.mp3" fadein 2 #음악 재생#

    menu :
        ##받은 의뢰에 따라 랜덤하게 이동할 예정이나 프로토타입에선 정해서 이동
        "병원" :
            jump hospital

        "회사" :
            jump company
            
        "별장" :
            scene bg_villa with fade
            jump villa

##label villa
label villa :
    scene bg_villa with dissolve
    show cr_Detective at right
    DT "어디부터 살펴볼까"
    menu : 
        "방1" :
            DT "그래 방1부터 살펴보자"
            jump room1
        "방2" :
            DT "그래 방2부터 살펴보자"
            jump room2
        "거실" :
            DT "그래 거실부터 살펴보자"
            jump living_room
        "증거":
            jump inventory    
        "그만 살펴본다" :
            DT "그래 이정도면 됐어."
            $killer_name = renpy.input('범인은 ...')
            if (killer_name == '의뢰인') and (see_point < 5):
                jump bad_ending1
            elif (killer_name == '의뢰인') and (see_point > 4):
                jump good_ending
            else :
                jump bad_ending2

## room1
label room1 :
    scene bg_villa_room1 with dissolve
    show screen notify("   큰 방   ") 
    if not see_point_room1 :
        $see_point_room1 = True
        "\n\n방은 먼지가 많이 쌓인 상태이다."
        nvl clear
        show cr_Detective at right
        DT "깨끗해보이는데 먼지가 많네.. 뭘 살펴볼까?"
    hide cr_Detective

    call screen room1_search ## 이미지맵(클릭으로 힌트찾는 부분)
    if _return is "room1_Bed":
        if (see_point_1bed < 1) :
            $see_point_1bed = 2
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "(침대는 가지런히 정리되어 있다.) \n어? 머리끈이 있네?"

    if _return is "Shelf" :
        if (see_point_Shelf < 1) :
            $see_point_Shelf = 2
            $ item_painting.pickup(1)
            show item_hint2 with dissolve :
            DT idle "(여러 장식품들이 놓여있다.) \n유난히 고양이 장식품들이 많네.."
            #---인벤 테스트 구역
            $ item_cookie.pickup(1)
            show image_cookie with dissolve :
            DT idle "맛있어 보이는 테스트용 쿠키다."
            #---
            $see_point +=1
    
    if _return is "room1_painting" :
        if (see_point_1painting < 1) :
            $see_point_1painting = 2
            $ item_painting.pickup(1)
            show item_hint4 with dissolve :
            DT idle "여긴 어떤 장소일까.."
    
    jump room1

## room2
label room2 :
    scene bg_villa_room2 with dissolve
    show screen notify("   작은 방   ")
    if not see_point_room2 :
        $see_point_room2 = True
        "\n\n어젯밤에 이 방에서 살인사건이 일어났어."
        nvl clear
        show cr_Detective at right
        DT "여긴 피해자가 머무던 방이야."
    hide cr_Detective

    call screen room2_search ## 이미지맵(클릭으로 힌트찾는 부분)
    if _return is "room2_Bed":
        if (see_point_2bed < 1) :
            $see_point_2bed = 2
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "피해자는 이 침대에서 자고 있었어"

    if _return is "dressing_table" :
        if (see_point_dressing_table < 1) :
            $see_point_dressing_table = 2
            $ item_painting.pickup(1)
            show item_hint3 with dissolve :
            DT idle "(깨진 유리 조각이 있다)"
            DT "어쩌다 깨진걸까"
    
    if _return is "Table" :
        if (see_point_Table < 1) :
            $see_point_Table = 2
            $ item_painting.pickup(1)
            show item_hint2 with dissolve :
            DT idle "무언가를 먹은 흔적이 있다."
    
    jump room2


##room living
label living_room :
    scene bg_villa_living with dissolve
    show screen notify("   거실   ") 
    if not see_point_living :
        $see_point_living = True
        "\n\n넓은 거실에 가구가 몇 개 없어서 쓸쓸한 느낌이 든다."
        nvl clear
        show cr_Detective at right
        DT "거실에는 사람이 많이 다녔을거야."
    
    call screen living_search ## 이미지맵(클릭으로 힌트찾는 부분)
    hide cr_Detective
    if _return is "post":
        if (see_point_post < 1) :
            $see_point_post = 2
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "이 쪽지의 내용은 추리하는데 도움되겠어"
            DT idle "자세히 보니 용의자들끼리 역할 분담한 내용을 적어놓은 것 같아."    

    if _return is "living_painting" :
        if (see_point_Lpainting < 1) :
            $see_point_Lpainting = 2
            $ item_painting.pickup(1)
            show item_hint2 with dissolve :
            DT idle "이 그림은 고가의 그림인 것 같은데 "
    
    jump living_room

##inventory
label inventory:
    scene bg lab
    call screen inventory(inv) with Dissolve(.2)
    jump villa

## endings
label good_ending :
    #(killer_name == '의뢰인') and (see_point > 4)#
    DT "범인은 의뢰인이야!"with vpunch
    stop music fadeout 2
    scene bg_room with fade
    DT "이번에도 무사히 사건을 해결했군"
    return

label bad_ending1 :
    #(killer_name == '의뢰인') and (see_point < 5)#
    DT "어째서 범인 그 사람일까?"
    DT "다시 한번 살펴보자..."
    jump villa

label bad_ending2 :
    #(!(killer_name == '의뢰인'))#
    DT "범인이 아닌것 같은데?"
    DT "다시 한번 살펴보자..."
    jump villa

