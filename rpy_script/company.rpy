label company : 
    #증거 찾기 이미지맵이랑, 라벨만 CP붙힘/ search : 이미지맵, find : 라벨
    $ myP = "company"
    $ myR = ""  
    $ visit_company = 1
        
init python:
    #추리점수&방 탐색
    visited = set()
    hint = set()
    Talk = set()

## 게임에서 사용할 이미지(배경, 캐릭터 등) ##   
init :
    #방 이미지
    image bg_CP = "BG/CP.png"   
    image bg_CP_office1 = "BG/CP_office1.png"
    image bg_CP_office2 = "BG/CP_office2.png"
    image bg_CP_room = "BG/CP_room.png"
   

    ## 사무실 201호 증거찾기   // 위치만 설정 완료, 변수명 바꿔야함
    screen search_CP1 : 
        zorder 99
        imagemap :
            ground "BG/CP_office1.png"
            hotspot(537, 553, 122, 112) action Return("room1_Bed")
            hotspot(1138, 574, 56, 176) action Return("Shelf") 
            hotspot(522, 390, 136, 172) action Return("room1_painting") 
            
            imagebutton idle "return_btn" :
                xalign 0.01
                yalign 0.96
                action [Hide("text_timer"), Jump("company_office1")]

    ## 사무실 202호 증거찾기
    screen search_CP2 : 
        zorder 99
        imagemap :
            ground "BG/CP_office2.png"
            hotspot(1289, 138, 408, 322) action Return("room2_Bed") 
            hotspot(323, 631, 91, 222) action Return("dressing_table") 
            hotspot(1733, 149, 150, 690) action Return("Table") 

            imagebutton idle "return_btn" :
                xalign 0.01
                yalign 0.96
                action [Hide("text_timer"), Jump("company_office2")]

    ## 휴게실 증거찾기
    screen search_CP3 : 
        zorder 99
        imagemap :
            ground "BG/CP_room.png"
            hotspot(238, 365, 105, 253) action Return("post")
            hotspot(1322, 369, 110, 134) action Return("living_painting")
            hotspot(2, 607, 97, 176) action Return("test3")

            imagebutton idle "return_btn" :
                xalign 0.01
                yalign 0.96
                action [Hide("text_timer"), Jump("company_room")]

    ## 지도
    screen company_map :
        zorder 99
        imagemap :
                xalign 0.5
                yalign 0.5
                ground "BG/map.png"
                hotspot(19, 20, 461, 155) action Jump("company_office1")
                hotspot(19, 179, 220, 292) action Jump("company_office2")
                hotspot(600, 247, 199, 158) action Jump("company_room")
                
                imagebutton idle "gui/button/icon_exit.png" action Hide("company_map")

    screen company_btn:
        imagebutton idle "find_idle_btn" hover "find_hover_btn":
            xpos 927
            ypos 498
            action [
                If(myR == "office1",
                    If("find_CP1" not in visited, Jump("find_CP1"))
                ),
                If(myR == "office2",
                    If("find_CP2" not in visited, Jump("find_CP2"))
                ),
                If(myR == "room",
                    If("find_CP3" not in visited, Jump("find_CP3"))
                ),
                Jump("error")
            ]

        imagebutton idle "talk_idle_btn" hover "talk_hover_btn" :
                xpos 927
                ypos 350
                action Jump("talk_test")   ##npc대화맵은 여기서 바꿔주세요
        
        imagebutton idle "gui/button/btn_return.png" :
                activate_sound "audio/sound/select.mp3"
                xalign 0.01
                yalign 0.96
                action Jump("company")

#############################################################################
## 본 스크립트 ##

scene bg_CP
show cr_Detective at right with dissolve
$ quick_menu = False

if "company_main" not in visited : 
    "\n\n\n\n각 방 마다 증거찾기와 대화하기를 한번씩 할 수 있습니다.\n" 
    "\n증거찾기는 클릭하는 방식으로 찾을 수 있습니다.\n대화하기는 NPC 에게 궁금한 것을 물어볼 수 있습니다.\n"
    "단 한 번만 가능하니 신중하게 결정해주세요.\n\n"
    "좌측 상단 버튼을 통해 찾은 증거 확인과 방 이동을 할 수 있습니다."
    nvl clear
    DT "어디부터 살펴볼까"
    
$ visited.add("company_main")
menu : 
    "사무실 201호" :
        DT "그래 사무실 201호부터 살펴보자"
        play sound "audio/sound/open.mp3"
        jump company_office1

    "사무실 202호" :
        DT "그래 진료실 202호부터 살펴보자"
        play sound "audio/sound/open.mp3"
        jump company_office2

    "휴게실" :
        DT "그래 휴게실부터 살펴보자"
        play sound "audio/sound/open.mp3"
        jump company_room

    "그만 살펴본다" :
        $ myP = "company"
        DT "그래 이정도면 됐어."
        $ killer_name = renpy.input('범인은 ...')
        if (killer_name == '의뢰인') and (see_point < 5):
            jump bad_ending1
        elif (killer_name == '의뢰인') and (see_point > 4):
            jump good_ending
        else :
            jump bad_ending2

##########################################################################
## office1 ##

label company_office1 :
    hide screen company_map
    show screen notify("사무실 201호")
    $ myR = "office1"
    $ quick_menu = False
    if "company_office1" not in visited:
        $ visited.add("company_office1")
        scene bg_CP_office1 with fade
        show cr_Detective at right

        DT "이 사무실에 평소와 같이 출근 했다고 들었는데.."

        hide cr_Detective

    scene bg_CP_office1
    show cr_CP_woman :
        xpos 407
        ypos 170  
    call screen company_btn

label find_CP1 :
    $ visited.add("find_CP1")
    $ quick_menu = True
    hide cr_CP_woman

    hide company_map
    show screen text_timer
    call screen search_CP1

    if "1bed" not in hint :
        if _return is "room1_Bed":
            play sound "audio/sound/save.mp3"
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "(침대는 가지런히 정리되어 있다.) \n어? 머리끈이 있네?"
            $ hint.add("1bed")
            hide item_hint1
            
    
    if "Shelf" not in hint :
        if _return is "Shelf" :
            play sound "audio/sound/save.mp3"
            $ item_painting.pickup(1)
            show item_hint2 with dissolve :
            DT idle "(여러 장식품들이 놓여있다.) \n유난히 고양이 장식품들이 많네.."
            #---인벤 테스트 구역
            $ item_cookie.pickup(1)
            show image_cookie with dissolve :
            DT idle "맛있어 보이는 테스트용 쿠키다."
            #---
            $ see_point +=1
            $ hint.add("Shelf")
            hide item_hint2

    if "1painting" not in hint :
        if _return is "room1_painting" :
            play sound "audio/sound/save.mp3"
            $ item_painting.pickup(1)
            show item_hint4 with dissolve :
            DT idle "여긴 어떤 장소일까.."
            $ hint.add("1painting")
            hide item_hint4
    
    jump find_CP1

##########################################################################
## office2 ##

label company_office2 :
    hide screen company_map
    show screen notify("사무실 202호")
    $ myR = "office2"
    $ quick_menu = False

    if "company_office2" not in visited:
        $ visited.add("company_office2")
        scene bg_CP_office2 with fade
        show cr_Detective at right

        DT "어젯밤에 이 방에서 살인사건이 일어났어."

        nvl clear
        hide cr_Detective

    scene bg_CP_office2
    #show cr_men1 at right
    ##npc 추가할경우 상호작용##
    #if "men1" not in Talk:
    #    $ Talk.add("men1")
    #    ch_men1 "안녕하세요 탐정님"
    call screen company_btn 

label find_CP2 :
    $ visited.add("find_CP2")
    $ quick_menu = True
    hide company_map
    #hide cr_men1

    show screen text_timer
    call screen search_CP2 

    if "2bed" not in hint:
        if _return is "2Bed":
            play sound "audio/sound/save.mp3"
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "피해자는 이 침대에서 자고 있었어"
            $ hint.add("2bed")
            hide item_hint1
    
    if "glass" not in hint:
        if _return is "Glass" :
            play sound "audio/sound/save.mp3"
            $ item_painting.pickup(1)
            show item_hint3 with dissolve :
            DT idle "(깨진 유리 조각이 있다)"
            DT "어쩌다 깨진걸까"
            $ hint.add("glass")
            hide item_hint3
    
    if "table" not in hint:
        if _return is "Table" :
            play sound "audio/sound/save.mp3"
            $ item_painting.pickup(1)
            show item_hint2 with dissolve :
            DT idle "무언가를 먹은 흔적이 있다."
            $ hint.add("table")
            hide item_hint2
    
    jump find_CP2

##############################################################################
## room ##

label company_room :
    hide screen company_map
    show screen notify("회사 휴게실")
    $ myR = "room"
    $ quick_menu = False

    if "company_room" not in visited:
            $ visited.add("company_room")
            scene bg_CP_room with fade
            show cr_Detective at right

            DT "\n\n어젯밤에 이 방에서 살인사건이 일어났어."

            nvl clear
            hide cr_Detective

    scene bg_CP_room
    #show cr_men1 at right ##npc 이미지
    ##npc 추가할경우 상호작용##
    #if "men1" not in Talk:
    #    $ Talk.add("men1")
    #    ch_men1 "안녕하세요 탐정님"
    call screen company_btn 
 
label find_CP3 :
    $ visited.add("find_CP3")
    $ quick_menu = True
    hide company_map
    #hide cr_men1

    show screen text_timer
    call screen search_CP3
    
    ##증거
    if "post" not in hint:
        if _return is "post":
            play sound "audio/sound/save.mp3"
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "이 쪽지의 내용은 추리하는데 도움되겠어"
            DT idle "자세히 보니 용의자들끼리 역할 분담한 내용을 적어놓은 것 같아."
            $ hint.add("post") 
            hide item_hint1   

    if "2painting" not in hint:
        if _return is "living_painting" :
            play sound "audio/sound/save.mp3"
            $ item_painting.pickup(1)
            show item_hint2 with dissolve :
            DT idle "이 그림은 고가의 그림인 것 같은데 "
            $ hint.add("2painting")
            hide item_hint2

    jump find_CP3


#label CP_error :
#    if myR == "office1" :
#        scene bg_CP_office1
#        DT idle "더 이상 기회는 없어."
#        jump company_office1
#    elif myR == "office2" :
#        scene bg_CP_office2
#        DT idle "더 이상 기회는 없어."
#        jump company_office2
#    elif myR == "room" :
#        scene bg_CP_room
#        DT idle "더 이상 기회는 없어."
#        jump company_room
