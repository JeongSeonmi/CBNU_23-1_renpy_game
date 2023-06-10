label hospital :
    #이름 정의할대 사진 이름은 (영어대문자철자두개_방이름) 예시 : HP_room
    $ myP = "hospital"
    $ myR = ""
    $ visit_hospital = 1
    
init python:
    #추리점수&방 탐색
    visited = set()
    hint = set()
    Talk = set()


## 게임에서 사용할 이미지(배경, 캐릭터 등) ##   
init :
    ##방 이미지
    image bg_HP = "BG/HP.png"   
    image bg_HP_office1 = "BG/HP_office1.png"
    image bg_HP_office2 = "BG/HP_office2.png"
    image bg_HP_room = "BG/HP_room.png"
    image HP_map = im.FactorScale("BG/HP_map.png", 1.0)


    ## 진료실 101호 증거찾기  // 위치만 설정 완료, 변수명 바꿔야함
    screen search_HP1 : 
        zorder 99
        imagemap :
            ground "BG/HP_office1.png"
            hotspot(1034, 503, 239, 50) action Return("hint1")  #책상 위
            hotspot(84, 214, 252, 150) action Return("hint2") #책장
            hotspot(468, 231, 231, 244) action Return("hint3") #게시판
            hotspot(962, 525, 59, 144) action Return("hint4") #서랍1
            hotspot(1202, 565, 78, 156) action Return("hint5") #서랍2
            hotspot(1473, 661, 117, 192) action Return("hint6") #서랍3
            hotspot(1024, 503, 282, 55) action Return("hint7") #책상
            hotspot(1236, 282, 180, 216) action Return("hint8") #블라인드
            
            imagebutton idle "return_btn" :
                xalign 0.01
                yalign 0.96
                action [Hide("text_timer"), Jump("hospital_office1")]

    ## 진료실 102호 증거찾기
    screen search_HP2 : 
        zorder 99
        imagemap :          
            ground "BG/HP_office2.png"
            hotspot(1319, 414, 51, 115) action Return("hint1") #작은 책장
            hotspot(608, 158, 374, 390) action Return("hint2") #창문
            hotspot(1023, 744, 79, 282) action Return("hint3") #서랍1
            hotspot(192, 235, 87, 148) action Return("hint4") #왼쪽 책장 중 한칸
            hotspot(1405, 589, 306, 56) action Return("hint5") #오른쪽 책상
            hotspot(891, 610, 314, 103) action Return("hint6") #왼쪽 책상
            hotspot(524, 841, 126, 102) action Return("hint7") #그냥 바닥
            hotspot(1719, 763, 198, 295) action Return("hint8") #오른쪽 서랍

            imagebutton idle "return_btn" :
                xalign 0.01
                yalign 0.96
                action [Hide("text_timer"), Jump("hospital_office2")] 
                           
    ## 병실 증거찾기
    screen search_HP3 : 
        zorder 99
        imagemap :
            ground "BG/HP_room.png"
            hotspot(328, 700, 109, 175) action Return("hint1") #갈색 서랍
            hotspot(694, 956, 287, 101) action Return("hint2") #침대 밑
            hotspot(916, 474, 73, 121) action Return("hint3") #왼쪽 커튼 뒤
            hotspot(1598, 496, 262, 231) action Return("hint4") #오른쪽 커튼 뒤
            hotspot(783, 595, 135, 76) action Return("hint5") #파란색 서랍
            hotspot(518, 651, 280, 62) action Return("hint6") #베개 밑
            hotspot(99, 187, 83, 824) action Return("hint7") #문
            hotspot(433, 224, 137, 135) action Return("hint8") #그냥 벽

            imagebutton idle "return_btn" :
                xalign 0.01
                yalign 0.96
                action [Hide("text_timer"), Jump("hospital_room")]
   
    ## 지도
    screen hospital_map :
        zorder 100
        imagemap :
                xalign 0.25
                yalign 0.45
                ground "HP_map" 
                hotspot(19, 20, 461, 155) action Jump("hospital_office1")
                hotspot(19, 179, 220, 292) action Jump("hospital_office2")
                hotspot(600, 247, 199, 158) action Jump("hospital_room")

                imagebutton idle "gui/button/icon_exit.png" action Hide("hospital_map")
    
    # 증거찾기 대화하기 버튼 #    
    screen hospital_btn:
        imagebutton idle "find_idle_btn" hover "find_hover_btn":
                xpos 927
                ypos 350
                action [
                If(myR == "office1",
                    If("find_HP1" not in visited, Jump("find_HP1"))
                ),
                If(myR == "office2",
                    If("find_HP2" not in visited, Jump("find_HP2"))
                ),
                If(myR == "room",
                    If("find_HP3" not in visited, Jump("find_HP3"))
                ),
                Jump("error")
                ]

        imagebutton idle "talk_idle_btn" hover "talk_hover_btn":
                xpos 927
                ypos 498
                action [
                    If(myR == "office1",
                        If("talk_suspecter1" not in visited, Jump("talk_suspecter"))
                    ),
                    If(myR == "office2",
                        If("talk_suspecter2" not in visited, Jump("talk_suspecter2"))
                    ),
                    If(myR == "room",
                        If("talk_suspecter3" not in visited, Jump("talk_suspecter3"))
                    ),
                    Jump("error")
                ]
        
        imagebutton idle "gui/button/btn_return.png" :
                activate_sound "audio/sound/select.mp3"
                xalign 0.01
                yalign 0.96
                action Jump("hospital")
    
#####################################################################################################    
## 본 스크립트 ##
hide screen hospital_map
scene bg_HP
show cr_Detective at right with dissolve
$ quick_menu = False

if "hopspital_main" not in visited :
    "\n\n\n\n각 방 마다 증거찾기와 대화하기를 한번씩 할 수 있습니다.\n" 
    "\n증거찾기는 클릭하는 방식으로 찾을 수 있습니다.\n대화하기는 NPC 에게 궁금한 것을 물어볼 수 있습니다.\n"
    "단 한 번만 가능하니 신중하게 결정해주세요.\n\n"
    "좌측 상단 버튼을 통해 찾은 증거 확인과 방 이동을 할 수 있습니다."
    nvl clear
    DT "어디부터 살펴볼까"

$ visited.add("hopspital_main")
menu : 
    "진료실 101호" :
        DT "그래 진료실 101호부터 살펴보자"
        play sound "audio/sound/open.mp3"
        jump hospital_office1

    "진료실 102호" :
        DT "그래 진료실 102호부터 살펴보자"
        play sound "audio/sound/open.mp3"
        jump hospital_office2

    "병실" :
        DT "그래 병실부터 살펴보자"
        play sound "audio/sound/open.mp3"
        jump hospital_room  

    "그만 살펴본다" :
        $ myP = "hospital"
        DT "그래 이정도면 됐어."
        $ killer_name = renpy.input('범인은 ...')
        if (killer_name == killer) and (see_point < 5):
            jump bad_ending1
        elif (killer_name == killer) and (see_point > 4):
            jump good_ending
        else :
            jump bad_ending2

##########################################################################################
## office1 ##

label hospital_office1 :
    hide screen hospital_map
    show screen notify("개신병원 병실 101호")
    $ myR = "office1" #증거찾기 재진입 방지용
    $ quick_menu = False

    if "hospital_office1" not in visited:
        $ visited.add("hospital_office1")
        scene bg_HP_office1 with fade
        show cr_Detective at right

        DT "어제까지도 환자를 받던 진료실이야.."
        DT "증거가 아직 남아있을까..?"
 
        hide cr_Detective

    scene bg_HP_office1
    show cr_HP_doctor :
        xpos 368
        ypos 200
    ##npc 추가할경우 상호작용##
    #if "men1" not in Talk:
    #    $ Talk.add("men1")
    #    ch_men1 "안녕하세요 탐정님"
    call screen hospital_btn

## office1 증거찾기맵
label find_HP1 :
    $ visited.add("find_HP1")
    $ quick_menu = True
    hide cr_HP_doctor
    hide hospital_map

    show screen text_timer
    call screen search_HP1 ## 이미지맵(클릭으로 힌트찾는 부분)

    if "office1_hint1" not in hint : #책상 위
        if _return is "hint1":
            play sound "audio/sound/save.mp3"
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "(침대는 가지런히 정리되어 있다.) \n어? 머리끈이 있네?"
            $ hint.add("office1_hint1")
            hide item_hint1
            
    
    if "office1_hint2" not in hint : #책장
        if _return is "hint2" :
            play sound "audio/sound/save.mp3"
            $ item_painting.pickup(1)
            show item_hint2 with dissolve :
            DT idle "(여러 장식품들이 놓여있다.) \n유난히 고양이 장식품들이 많네.."
            #---인벤 테스트 구역
            $ item_cookie.pickup(1)
            show image_cookie with dissolve
            DT idle "맛있어 보이는 테스트용 쿠키다."
            #---
            $ see_point +=1
            $ hint.add("office1_hint2")
            hide item_hint2
            hide image_cookie

    if "office1_hint3" not in hint : #게시판
        if _return is "hint3" :
            play sound "audio/sound/save.mp3"
            $ item_painting.pickup(1)
            show item_hint4 with dissolve :
            DT idle "여긴 어떤 장소일까.."
            $ hint.add("office1_hint3")
            hide item_hint4
    
    if "office1_hint4" not in hint : #서랍1
        if _return is "hint4":
            play sound "audio/sound/save.mp3"
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "증거 4 테스트"
            $ hint.add("office1_hint4")
            hide item_hint1

    if "office1_hint5" not in hint : #서랍2
        if _return is "hint5":
            play sound "audio/sound/save.mp3"
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "증거 5 테스트"
            $ hint.add("office1_hint5")
            hide item_hint1

    if "office1_hint6" not in hint : #서랍3
        if _return is "hint6":
            play sound "audio/sound/save.mp3"
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "증거 6 테스트"
            $ hint.add("office1_hint6")
            hide item_hint1

    if "office1_hint7" not in hint : #책상
        if _return is "hint7":
            play sound "audio/sound/save.mp3"
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "증거 7 테스트"
            $ hint.add("office1_hint7")
            hide item_hint1
    
    if "office1_hint8" not in hint : #블라인드
        if _return is "hint8":
            play sound "audio/sound/save.mp3"
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "증거 8 테스트"
            $ hint.add("office1_hint8")
            hide item_hint1
    jump find_HP1
    return

###################################################################################
## office2 ##

label hospital_office2 :
    hide screen hospital_map
    show screen notify("별장 작은 방")
    $ myR = "office2"
    $ quick_menu = False

    if "hospital_office2" not in visited:
        $ visited.add("hospital_office2")
        scene bg_HP_office2 with fade

        DT "여긴 평범해보이는데 자세히 살펴볼까"

        nvl clear
        hide cr_Detective

    scene bg_HP_office2
    show cr_HP_nurse1 : 
        xpos 407
        ypos 170
    ##npc 추가할경우 상호작용##
    if "nurse1" not in Talk:
        $ Talk.add("nurse1")
        ch_HP_nurse1 "안녕하세요 탐정님"
    call screen hospital_btn

## office2 증거찾기맵
label find_HP2 :
    $ visited.add("find_HP2")
    $ quick_menu = True
    hide hospital_map
    hide cr_HP_nurse1

    show screen text_timer
    call screen search_HP2

    if "office1_hint1" not in hint : #작은 책장
        if _return is "hint1":
            play sound "audio/sound/save.mp3"
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "(침대는 가지런히 정리되어 있다.) \n어? 머리끈이 있네?"
            $ hint.add("office2_hint1")
            hide item_hint1
            
    
    if "office2_hint2" not in hint : #창문
        if _return is "hint2" :
            play sound "audio/sound/save.mp3"
            $ item_painting.pickup(1)
            show item_hint2 with dissolve :
            DT idle "(여러 장식품들이 놓여있다.) \n유난히 고양이 장식품들이 많네.."
            #---인벤 테스트 구역
            $ item_cookie.pickup(1)
            show image_cookie with dissolve
            DT idle "맛있어 보이는 테스트용 쿠키다."
            #---
            $ see_point +=1
            $ hint.add("office2_hint2")
            hide item_hint2
            hide image_cookie

    if "office2_hint3" not in hint : #서랍1
        if _return is "hint3" :
            play sound "audio/sound/save.mp3"
            $ item_painting.pickup(1)
            show item_hint4 with dissolve :
            DT idle "여긴 어떤 장소일까.."
            $ hint.add("office2_hint3")
            hide item_hint4
    
    if "office2_hint4" not in hint : #왼쪽 책장 중 한칸
        if _return is "hint4":
            play sound "audio/sound/save.mp3"
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "증거 4 테스트"
            $ hint.add("office2_hint4")
            hide item_hint1

    if "office2_hint5" not in hint : #오른쪽 책상
        if _return is "hint5":
            play sound "audio/sound/save.mp3"
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "증거 5 테스트"
            $ hint.add("office2_hint5")
            hide item_hint1

    if "office2_hint6" not in hint : #왼쪽 책상
        if _return is "hint6":
            play sound "audio/sound/save.mp3"
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "증거 6 테스트"
            $ hint.add("office2_hint6")
            hide item_hint1

    if "office2_hint7" not in hint : #그냥 바닥
        if _return is "hint7":
            play sound "audio/sound/save.mp3"
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "증거 7 테스트"
            $ hint.add("office2_hint7")
            hide item_hint1
    
    if "office2_hint8" not in hint : #오른쪽 서랍
        if _return is "hint8":
            play sound "audio/sound/save.mp3"
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "증거 8 테스트"
            $ hint.add("office2_hint8")
            hide item_hint1
    jump find_HP2
    return

##########################################################################################
## room ##

label hospital_room :
    hide screen hospital_map
    show screen notify("개신병원 병실")
    $ myR = "room" 
    $ quick_menu = False
    
    if "hospital_room" not in visited:
        $ visited.add("hospital_room")
        scene bg_HP_room with fade

        DT "거실에는 사람이 많이 다녔을거야."

        nvl clear
        hide cr_Detective
    scene bg_HP_room
    show cr_HP_nurse2 :
        xpos 1312
        ypos 160
    if "nurse2" not in Talk:
        $ Talk.add("nurse2")
        ch_HP_nurse2 "안녕하세요 탐정님"
    call screen hospital_btn  ## 타이머 시작


label find_HP3 :
    $ visited.add("find_HP3")
    $ quick_menu = True
    hide hospital_map
    hide cr_HP_nurse2

    show screen text_timer
    call screen search_HP3 

    if "room_hint1" not in hint : #갈색 서랍
        if _return is "hint1":
            play sound "audio/sound/save.mp3"
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "(침대는 가지런히 정리되어 있다.) \n어? 머리끈이 있네?"
            $ hint.add("room_hint1")
            hide item_hint1
            
    if "room_hint2" not in hint : #침대 밑
        if _return is "hint2" :
            play sound "audio/sound/save.mp3"
            $ item_painting.pickup(1)
            show item_hint2 with dissolve :
            DT idle "(여러 장식품들이 놓여있다.) \n유난히 고양이 장식품들이 많네.."
            #---인벤 테스트 구역
            $ item_cookie.pickup(1)
            show image_cookie with dissolve
            DT idle "맛있어 보이는 테스트용 쿠키다."
            #---
            $ see_point +=1
            $ hint.add("room_hint2")
            hide item_hint2
            hide image_cookie

    if "room_hint3" not in hint : #왼쪽 커튼 뒤
        if _return is "hint3" :
            play sound "audio/sound/save.mp3"
            $ item_painting.pickup(1)
            show item_hint4 with dissolve :
            DT idle "여긴 어떤 장소일까.."
            $ hint.add("room_hint3")
            hide item_hint4
    
    if "room_hint4" not in hint : #오른쪽 커튼 뒤
        if _return is "hint4":
            play sound "audio/sound/save.mp3"
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "증거 4 테스트"
            $ hint.add("room_hint4")
            hide item_hint1

    if "room_hint5" not in hint : #파란색 서랍
        if _return is "hint5":
            play sound "audio/sound/save.mp3"
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "증거 5 테스트"
            $ hint.add("room_hint5")
            hide item_hint1

    if "room_hint6" not in hint : #베개 밑
        if _return is "hint6":
            play sound "audio/sound/save.mp3"
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "증거 6 테스트"
            $ hint.add("room_hint6")
            hide item_hint1

    if "room_hint7" not in hint : #문
        if _return is "hint7":
            play sound "audio/sound/save.mp3"
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "증거 7 테스트"
            $ hint.add("room_hint7")
            hide item_hint1
    
    if "room_hint8" not in hint : #그냥 벽
        if _return is "hint8":
            play sound "audio/sound/save.mp3"
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "증거 8 테스트"
            $ hint.add("room_hint8")
            hide item_hint1
    jump find_HP3
    return
