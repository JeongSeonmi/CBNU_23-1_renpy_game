label villa :
    #이름 정의할대 사진 이름은 (영어대문자철자두개_방이름) 예시 : HP_room, 라벨 이름은 (소문자철자네개_방이름) 예시 : hosp_room
    $ myP = "villa"

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
    image bg_lab = "gui/Background.jpg"
    image find_btn = im.FactorScale("gui/button/find_ui.png", 0.6)
    image talk_btn = im.FactorScale("gui/button/talk_ui.png", 0.6)

    ## 방1 증거찾기
    screen room1_search : 
        zorder 99
        imagemap :
            #add DynamicDisplayable(text_countdown) xalign 0.99 ##타이머
            ground "BG/villa_room1.jpg"
            hotspot(1157, 714, 368, 168) action Return("room1_Bed")
            hotspot(199, 778, 172, 118) action Return("Shelf")
            hotspot(522, 390, 136, 172) action Return("room1_painting")
            
            ##GPT npc 위치###
            #imagebutton idle "cr_men1" :
            #    at left
            #    action Jump("villa_talk_test")
            
            #imagebutton idle "gui/button/btn_return.png" action Jump("villa") xalign 0.01 yalign 0.96

    ## 방2 증거찾기
    screen room2_search : 
        imagemap :
            ground "BG/villa_room2.jpg"
            hotspot(1229, 683, 317, 112) action Return("2Bed")
            hotspot(531, 602, 197, 144) action Return("Glass")
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

    ## 지도   
    screen villa_map :
        imagemap :
            xalign 0.5
            yalign 0.5
            ground "BG/map.png"
            hotspot(19, 20, 461, 155) action Jump("villa_room1")
            hotspot(19, 179, 220, 292) action Jump("villa_room2")
            hotspot(600, 247, 199, 158) action Jump("villa_living")
            
            imagebutton idle "gui/button/icon_exit.png" action Hide("villa_map")

    screen btn :
        imagebutton idle "find_btn" :
            xalign 0.6
            yalign 0.6
            action Jump("find")

        imagebutton idle "talk_btn" :
            xalign 0.6
            yalign 0.8
            action Jump("villa_talk_test")
        
        imagebutton idle "gui/button/btn_return.png" :
            xalign 0.01
            yalign 0.96
            action Jump("villa") 

    screen exit_btn :
        imagebutton idle "gui/button/btn_return.png" action Jump("villa") xalign 0.01 yalign 0.96
            

## 본 스크립트 ##
scene bg_villa
show cr_Detective at right with dissolve

if "villa_main" not in visited:  ##조건문 형태 변경 -> 변수 줄임
    DT "어디부터 살펴볼까"
$ visited.add("villa_main")
menu : 
    "방1" :
        DT "그래 방1부터 살펴보자"
        jump villa_room1

    "방2" :
        DT "그래 방2부터 살펴보자"
        jump villa_room2

    "거실" :
        DT "그래 거실부터 살펴보자"
        jump villa_living

    "그만 살펴본다" :
        DT "그래 이정도면 됐어."
        $ killer_name = renpy.input('범인은 ...')
        if (killer_name == '의뢰인') and (see_point < 5):
            jump bad_ending1
        elif (killer_name == '의뢰인') and (see_point > 4):
            jump good_ending
        else :
            jump bad_ending2

## room1
label villa_room1 :
    scene bg_villa_room1 with fade
    hide screen villa_map 
    #call screen exit_btn
    if "villa_room1" not in visited:
        $ visited.add("villa_room1")
        show cr_Detective at right
        DT "(방은 먼지가 많이 쌓인 상태이다.)"
        DT "(깨끗해보이는데 먼지가 많네.. 뭘 살펴볼까?)"

        "\n\n\n증거찾기는 단 한 번만 가능합니다"
        "신중하게 결정해주세요." with vpunch
        nvl clear

    hide cr_Detective
    show cr_men1 at right with dissolve
    if "men1" not in Talk:
        $ Talk.add("men1")
        ch_men1 "안녕하세요 탐정님"
    
    call screen btn  ## 타이머 시작
    jump find
    
    

## 타이머 돌아가는 증거찾기맵    
label find :
    #if "find_room1" not in visited :
    #    $ visited.add("find_room1")
    hide cr_men1
    show screen text_timer
    call screen room1_search

    ##증거
    if "1bed" not in hint :
        $ hint.add("1bed")
        if _return is "room1_Bed":
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "(침대는 가지런히 정리되어 있다.) \n어? 머리끈이 있네?"
    
    if "Shelf" not in hint :
        $ hint.add("Shelf")
        if _return is "Shelf" :
            $ item_painting.pickup(1)
            show item_hint2 with dissolve :
            DT idle "(여러 장식품들이 놓여있다.) \n유난히 고양이 장식품들이 많네.."
            #---인벤 테스트 구역
            $ item_cookie.pickup(1)
            show image_cookie with dissolve :
            DT idle "맛있어 보이는 테스트용 쿠키다."
            #---
            $ see_point +=1

    if "1painting" not in hint :
        $ hint.add("1painting")
        if _return is "room1_painting" :
            $ item_painting.pickup(1)
            show item_hint4 with dissolve :
            DT idle "여긴 어떤 장소일까.."
    
    jump find

## room2
label villa_room2 :
    scene bg_villa_room2 with fade
    hide screen villa_map
    show screen notify("작은 방")
    if "villa_room2" not in visited:
        $ visited.add("villa_room2")
        "\n\n어젯밤에 이 방에서 살인사건이 일어났어."
        nvl clear
        show cr_Detective at right
        DT "여긴 피해자가 머무던 방이야."
    hide cr_Detective
    
    call screen room2_search ## 이미지맵(클릭으로 힌트찾는 부분)
    
    ##증거
    if "2bed" not in hint:
        $ hint.add("2bed")
        if _return is "2Bed":
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "피해자는 이 침대에서 자고 있었어"
    
    if "glass" not in hint:
        $ hint.add("glass")
        if _return is "Glass" :
            $ item_painting.pickup(1)
            show item_hint3 with dissolve :
            DT idle "(깨진 유리 조각이 있다)"
            DT "어쩌다 깨진걸까"
    
    if "table" not in hint:
        $ hint.add("table")
        if _return is "Table" :
            $ item_painting.pickup(1)
            show item_hint2 with dissolve :
            DT idle "무언가를 먹은 흔적이 있다."

    jump villa_room2


##room living
label villa_living :
    scene bg_villa_living with fade
    hide screen villa_map
    show screen notify("별장 거실") 
    if "villa_living" not in visited:
        $ visited.add("villa_living")
        "\n\n넓은 거실에 가구가 몇 개 없어서 쓸쓸한 느낌이 든다."
        nvl clear
        show cr_Detective at right
        DT "거실에는 사람이 많이 다녔을거야."
    hide cr_Detective
    
    call screen living_search ## 이미지맵(클릭으로 힌트찾는 부분)

    ##증거
    if "post" not in hint:
        $ hint.add("post")
        if _return is "post":
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "이 쪽지의 내용은 추리하는데 도움되겠어"
            DT idle "자세히 보니 용의자들끼리 역할 분담한 내용을 적어놓은 것 같아."    

    if "2painting" not in hint:
        $ hint.add("2painting")
        if _return is "living_painting" :
            $ item_painting.pickup(1)
            show item_hint2 with dissolve :
            DT idle "이 그림은 고가의 그림인 것 같은데 "
    
    jump villa_living

### 캐릭터 사진 클릭해서 대화하는 공간 ###
label villa_talk_test:
    scene bg_villa_room1
    show cr_men1 at center
    call screen exit_btn
    jump villa_talk_1