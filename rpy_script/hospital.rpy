label hospital :
    #이름 정의할대 사진 이름은 (영어대문자철자두개_방이름) 예시 : HP_room
    $ myP = "hospital"
    $ myR = ""
init python:
    #추리점수&방 탐색
    visited = set()
    hint = set()
    Talk = set()


## 게임에서 사용할 이미지(배경, 캐릭터 등) ##   
init :
    ##방 이미지
    image bg_HP = "BG/HP.png"   
    image bg_HP_office1 = "BG/HP_office.png"
    image bg_HP_office2 = "BG/HP_office2.png"
    image bg_HP_room = "BG/HP_room.png"


    ## 진료실 101호 증거찾기  // 위치만 설정 완료, 변수명 바꿔야함
    screen search_HP1 : 
        zorder 99
        imagemap :
            ground "BG/HP_office.png"
            hotspot(1048, 500, 141, 53) action Return("room1_Bed")  #책상 위
            hotspot(100, 261, 218, 92) action Return("Shelf") #책장
            hotspot(477, 265, 209, 199) action Return("room1_painting") #게시판

    ## 진료실 102호 증거찾기
    screen search_HP2 : 
        zorder 99
        imagemap :          
            ground "BG/HP_office2.png"
            hotspot(1331, 414, 33, 112) action Return("room2_Bed") #작은 책장
            hotspot(608, 158, 374, 390) action Return("dressing_table") #창문
            hotspot(1727, 768, 170, 258) action Return("Table") #오른쪽 서랍
                
    ## 병실 증거찾기
    screen search_HP3 : 
        zorder 99
        imagemap :
            ground "BG/HP_room.png"
            hotspot(328, 700, 109, 175) action Return("post") #갈색 서랍
            hotspot(717, 988, 197, 78) action Return("living_painting") #침대 밑
            hotspot(918, 505, 208, 107) action Return("test3") #왼쪽 커튼 뒤
   
    ## 지도
    screen hospital_map :
        zorder 99
        imagemap :
                xalign 0.5
                yalign 0.5
                ground "BG/map.png"
                hotspot(19, 20, 461, 155) action Jump("hospital_office1")
                hotspot(19, 179, 220, 292) action Jump("hospital_office2")
                hotspot(600, 247, 199, 158) action Jump("hospital_room")

                imagebutton idle "gui/button/icon_exit.png" action Hide("hospital_map")
    
    # 증거찾기 대화하기 버튼 #    
    screen hospital_btn:
        imagebutton idle "find_idle_btn" hover "find_hover_btn":
                xalign 0.6
                yalign 0.6
                hover_sound "audio/sound/select.mp3"
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
                xalign 0.6
                yalign 0.8
                action Jump("talk_test") ##npc대화맵은 여기서 바꿔주세요
        
        imagebutton idle "gui/button/btn_return.png" :
                xalign 0.01
                yalign 0.96
                action Jump("hospital")
    
#####################################################################################################    
## 본 스크립트 ##

scene bg_HP
show cr_Detective at right with dissolve

if "hopspital_main" not in visited :
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
        if (killer_name == '의뢰인') and (see_point < 5):
            jump bad_ending1
        elif (killer_name == '의뢰인') and (see_point > 4):
            jump good_ending
        else :
            jump bad_ending2

##########################################################################################
## office1 ##

label hospital_office1 :
    hide screen hospital_map
    show screen notify("개신병원 병실 101호")
    $ myR = "office1" #증거찾기 재진입 방지용

    if "hospital_office1" not in visited:
        $ visited.add("hospital_office1")
        scene bg_HP_office1 with fade
        show cr_Detective at right

        DT "어제까지도 환자를 받던 진료실이야.."
        DT "증거가 아직 남아있을까..?"
        "\n\n\n증거찾기는 단 한 번만 가능합니다"
        "신중하게 결정해주세요." with vpunch

        nvl clear
        hide cr_Detective

    scene bg_HP_office1
    #show cr_men1 at right
    ##npc 추가할경우 상호작용##
    #if "men1" not in Talk:
    #    $ Talk.add("men1")
    #    ch_men1 "안녕하세요 탐정님"
    call screen hospital_btn

## office1 증거찾기맵
label find_HP1 :
    $ visited.add("find_HP1")
    #hide cr_men1   #npc 이미지 지우기
    hide hospital_map
    show screen text_timer
    call screen search_HP1 ## 이미지맵(클릭으로 힌트찾는 부분)
    
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
    
    jump find_HP1

###################################################################################
## office2 ##

label hospital_office2 :
    hide screen hospital_map
    show screen notify("별장 작은 방")
    $ myR = "office2"

    if "hospital_office2" not in visited:
        $ visited.add("hospital_office2")
        scene bg_HP_office2 with fade

        DT "여긴 평범해보이는데 자세히 살펴볼까"
        "\n\n\n증거찾기는 단 한 번만 가능합니다"
        "신중하게 결정해주세요." with vpunch

        nvl clear
        hide cr_Detective

    scene bg_HP_office2
    #show cr_men1 at right
    ##npc 추가할경우 상호작용##
    #if "men1" not in Talk:
    #    $ Talk.add("men1")
    #    ch_men1 "안녕하세요 탐정님"
    call screen hospital_btn

## office2 증거찾기맵
label find_HP2 :
    $ visited.add("find_HP2")
    hide hospital_map
    #hide cr_men1
    show screen text_timer
    call screen search_HP2

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
    
    jump find_HP2

##########################################################################################
## room ##

label hospital_room :
    hide screen hospital_map
    show screen notify("개신병원 휴게실")
    $ myR = "room" 

    if "hospital_room" not in visited:
        $ visited.add("hospital_room")
        scene bg_HP_room with fade
        DT "거실에는 사람이 많이 다녔을거야."
        "\n\n\n증거찾기는 단 한 번만 가능합니다"
        "신중하게 결정해주세요." with vpunch
        nvl clear
        hide cr_Detective

    #if "men1" not in Talk:
    #    $ Talk.add("men1")
    #    ch_men1 "안녕하세요 탐정님"
    call screen hospital_btn  ## 타이머 시작


label find_HP3 :
    $ visited.add("find_HP3")
    hide hospital_map
    #hide cr_men1
    show screen text_timer
    call screen search_HP3 

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

    jump find_HP3


#label HP_error :
#    if myR == "office1" :
#        scene bg_HP_office1
#        DT idle "더 이상 기회는 없어."
#        jump company_office1
#    elif myR == "office2" :
#        scene bg_HP_office2
#        DT idle "더 이상 기회는 없어."
#        jump company_office2
#    elif myR == "room" :
#        scene bg_HP_room
#        DT idle "더 이상 기회는 없어."
#        jump company_room