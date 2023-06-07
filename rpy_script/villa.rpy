label villa :
    #증거 찾기 이미지맵이랑, 라벨만 CP붙힘/ search : 이미지맵, find : 라벨
    $ myP = "villa"
    $ myR = ""

init python:
    #추리점수&방 탐색 변수 
    visited = set()
    hint = set()
    Talk = set()

## 게임에서 사용할 이미지(배경, 캐릭터 등) ##
init :
    ##방 이미지
    image bg_villa = "BG/villa.png"   
    image bg_villa_room1 = "BG/villa_room1.jpg"
    image bg_villa_room2 = "BG/villa_room2.jpg"
    image bg_villa_living = "BG/villa_living.png"

    ## 방1 증거찾기
    screen search_villa1 : 
        zorder 99
        imagemap :
            ground "BG/villa_room1.jpg"
            hotspot(1157, 714, 368, 168) action Return("room1_Bed")
            hotspot(199, 778, 172, 118) action Return("Shelf")
            hotspot(522, 390, 136, 172) action Return("room1_painting")

            imagebutton idle "return_btn" :
                xalign 0.01
                yalign 0.96
                action [Hide("text_timer"), Jump("villa_room1")]
            
    ## 방2 증거찾기
    screen search_villa2 :
        zorder 99 
        imagemap :
            ground "BG/villa_room2.jpg"
            hotspot(1229, 683, 317, 112) action Return("2Bed")
            hotspot(531, 602, 197, 144) action Return("Glass")
            hotspot(891, 669, 266, 70) action Return("Table")

            imagebutton idle "return_btn" :
                xalign 0.01
                yalign 0.96
                action [Hide("text_timer"), Jump("villa_room2")]

    ## 거실 증거찾기
    screen search_villa3 : 
        zorder 99
        imagemap :        
            ground "BG/villa_living.png"
            hotspot(289, 594, 42, 40) action Return("post")
            hotspot(779, 328, 180, 143) action Return("living_painting")
            hotspot(1654, 449, 125, 118) action Return("test3")

            imagebutton idle "return_btn" :
                xalign 0.01
                yalign 0.96
                action [Hide("text_timer"), Jump("villa_living")]

    ## 지도   
    screen villa_map :
        zorder 99
        imagemap :
            xalign 0.5
            yalign 0.5
            ground "BG/map.png"
            hotspot(19, 20, 461, 155) action Jump("villa_room1")
            hotspot(19, 179, 220, 292) action Jump("villa_room2")
            hotspot(600, 247, 199, 158) action Jump("villa_living")
            
            imagebutton idle "gui/button/icon_exit.png" action Hide("villa_map")
    
    screen villa_btn :
        imagebutton idle "find_idle_btn" hover "find_hover_btn":
            xalign 0.6
            yalign 0.6
            hover_sound "audio/sound/select.mp3"
            action [
                If(myR == "room1",
                    If("find_villa1" not in visited, Jump("find_villa1"))
                ),
                If(myR == "room2",
                    If("find_villa2" not in visited, Jump("find_villa2"))
                ),
                If(myR == "living",
                    If("find_villa3" not in visited, Jump("find_villa3"))
                ),
                Jump("error")
            ]

        imagebutton idle "talk_idle_btn" hover "talk_hover_btn":
            xalign 0.6
            yalign 0.8
            action Jump("talk_test")  ##npc대화맵은 여기서 바꿔주세요
        
        imagebutton idle "gui/button/btn_return.png" :
            xalign 0.01
            yalign 0.96
            action Jump("villa")

## 본 스크립트 ##
scene bg_villa
show cr_Detective at right with dissolve
$ quick_menu = False

if "villa_main" not in visited: 
    DT "어디부터 살펴볼까"
$ visited.add("villa_main")
menu : 
    "방1" :
        DT "그래 방1부터 살펴보자"
        play sound "audio/sound/open.mp3"
        jump villa_room1

    "방2" :
        DT "그래 방2부터 살펴보자"
        play sound "audio/sound/open.mp3"
        jump villa_room2

    "거실" :
        DT "그래 거실부터 살펴보자"
        play sound "audio/sound/open.mp3"
        jump villa_living

    "그만 살펴본다" :
        $ myP = "villa"
        DT "그래 이정도면 됐어."
        $ killer_name = renpy.input('범인은 ...')
        if (killer_name == '의뢰인') and (see_point < 5):
            jump bad_ending1
        elif (killer_name == '의뢰인') and (see_point > 4):
            jump good_ending
        else :
            jump bad_ending2

###############################################################################################
## room1 ##

label villa_room1 :
    hide screen villa_map 
    show screen notify("별장 큰 방")
    $ myR = "room1"  #증거찾기 재진입 방지용
    $ quick_menu = False
    if "villa_room1" not in visited:
        $ visited.add("villa_room1")
        scene bg_villa_room1 with fade
        show cr_Detective at right

        DT "(방은 먼지가 많이 쌓인 상태이다.)"
        DT "(깨끗해보이는데 먼지가 많네.. 뭘 살펴볼까?)"
        "\n\n\n증거찾기는 단 한 번만 가능합니다"
        "신중하게 결정해주세요." with vpunch

        nvl clear
        hide cr_Detective

    scene bg_villa_room1 
    show cr_men1 at right

    if "men1" not in Talk:
        $ Talk.add("men1")
        ch_men1 "안녕하세요 탐정님"

    call screen villa_btn  

## room1 증거찾기맵    
label find_villa1 :
    $ visited.add("find_villa1")
    $ quick_menu = True
    hide cr_men1
    hide hospital_map
    show screen text_timer
    call screen search_villa1

    ##증거
    if "1bed" not in hint :
        if _return is "room1_Bed":
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "(침대는 가지런히 정리되어 있다.) \n어? 머리끈이 있네?"
            $ hint.add("1bed")
            hide item_hint1
            
    
    if "Shelf" not in hint :
        if _return is "Shelf" :
            $ item_painting.pickup(1)
            show item_hint2 with dissolve :
            DT idle "(여러 장식품들이 놓여있다.) \n유난히 고양이 장식품들이 많네.."
            #---인벤 테스트 구역
            $ item_cookie.pickup(1)
            show image_cookie with dissolve
            DT idle "맛있어 보이는 테스트용 쿠키다."
            #---
            $ see_point +=1
            $ hint.add("Shelf")
            hide item_hint2
            hide image_cookie

    if "1painting" not in hint :
        if _return is "room1_painting" :
            $ item_painting.pickup(1)
            show item_hint4 with dissolve :
            DT idle "여긴 어떤 장소일까.."
            $ hint.add("1painting")
            hide item_hint4
    
    jump find_villa1

###############################################################################################
## room2 ##

label villa_room2 :
    hide screen villa_map
    show screen notify("별장 작은 방")
    $ myR = "room2"
    $ quick_menu = False

    if "villa_room2" not in visited:
        $ visited.add("villa_room2")
        scene bg_villa_room2 with fade
        show cr_Detective at right

        DT "여긴 피해자가 머무던 방이야."
        DT "(어젯밤에 이 방에서 살인사건이 일어났어.)"
        "\n\n\n증거찾기는 단 한 번만 가능합니다"
        "신중하게 결정해주세요." with vpunch

        nvl clear
        hide cr_Detective

    scene bg_villa_room2
    #show cr_men1 at right
    ##npc 추가할경우 상호작용##
    #if "men1" not in Talk:
    #    $ Talk.add("men1")
    #    ch_men1 "안녕하세요 탐정님"
    call screen villa_btn

## room2 증거찾기맵    
label find_villa2 :
    $ visited.add("find_villa2")
    hide hospital_map
    #hide cr_men1
    $ quick_menu = True
    show screen text_timer
    call screen search_villa2
    
    if "2bed" not in hint:
        if _return is "2Bed":
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "피해자는 이 침대에서 자고 있었어"
            $ hint.add("2bed")
            hide item_hint1
    
    if "glass" not in hint:
        if _return is "Glass" :
            $ item_painting.pickup(1)
            show item_hint3 with dissolve :
            DT idle "(깨진 유리 조각이 있다)"
            DT "어쩌다 깨진걸까"
            $ hint.add("glass")
            hide item_hint3
    
    if "table" not in hint:
        if _return is "Table" :
            $ item_painting.pickup(1)
            show item_hint2 with dissolve :
            DT idle "무언가를 먹은 흔적이 있다."
            $ hint.add("table")
            hide item_hint2

    jump find_villa2

###############################################################################################
## living ##

label villa_living :
    hide screen villa_map
    show screen notify("별장 거실")
    $ myR = "living" 
    $ quick_menu = False
    if "villa_living" not in visited:
        $ visited.add("villa_living")
        scene bg_villa_living with fade
        "\n\n넓은 거실에 가구가 몇 개 없어서 쓸쓸한 느낌이 든다."
        nvl clear
        show cr_Detective at right
        DT "거실에는 사람이 많이 다녔을거야."
        "\n\n\n증거찾기는 단 한 번만 가능합니다"
        "신중하게 결정해주세요." with vpunch
        nvl clear
        hide cr_Detective
    
    scene bg_villa_living
    #if "men1" not in Talk:
    #    $ Talk.add("men1")
    #    ch_men1 "안녕하세요 탐정님"
    call screen villa_btn  

## living room 증거찾기맵    
label find_villa3 :
    $ visited.add("find_villa3")
    $ quick_menu = True
    hide hospital_map
    show screen text_timer
    call screen search_villa3

    if "post" not in hint:
        if _return is "post":
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "이 쪽지의 내용은 추리하는데 도움되겠어"
            DT idle "자세히 보니 용의자들끼리 역할 분담한 내용을 적어놓은 것 같아."
            $ hint.add("post")    
            hide item_hint1

    if "2painting" not in hint:
        if _return is "living_painting" :
            $ item_painting.pickup(1)
            show item_hint2 with dissolve :
            DT idle "이 그림은 고가의 그림인 것 같은데 "
            $ hint.add("2painting")
            hide item_hint2
    
    jump find_villa3


#label villa_error :
#    if myR == "room1" :
#        scene bg_villa_room1
#        DT idle "더 이상 기회는 없어."
#        jump villa_room1
#    elif myR == "room2" :
#        scene bg_villa_room2
#        DT idle "더 이상 기회는 없어."
#        jump villa_room2
#    elif myR == "living" :
#        scene bg_villa_living
#        DT idle "더 이상 기회는 없어."
#        jump villa_living