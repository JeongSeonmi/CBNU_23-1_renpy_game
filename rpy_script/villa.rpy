label villa :
    #증거 찾기 이미지맵이랑, 라벨만 CP붙힘/ search : 이미지맵, find : 라벨
    $ myP = "villa"
    $ myR = ""
    $ visit_villa = 1
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
            xpos 927
            ypos 498
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
            xpos 927
            ypos 350
            action Jump("talk_test")  ##npc대화맵은 여기서 바꿔주세요
        
        imagebutton idle "gui/button/btn_return.png" :
            activate_sound "audio/sound/select.mp3"
            xalign 0.01
            yalign 0.96
            action Jump("villa")

## 본 스크립트 ##
scene bg_villa
show cr_Detective at right with dissolve
$ quick_menu = False

if "villa_main" not in visited: 
    nvl clear
    "\n\n\n\n각 방 마다 증거찾기와 대화하기를 한번씩 할 수 있습니다.\n" 
    "\n증거찾기는 클릭하는 방식으로 찾을 수 있습니다.\n대화하기는 NPC 에게 궁금한 것을 물어볼 수 있습니다.\n"
    "단 한 번만 가능하니 신중하게 결정해주세요.\n\n"
    "좌측 상단 버튼을 통해 찾은 증거 확인과 방 이동을 할 수 있습니다."
    nvl clear
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
        show cr_Detective at left
        DT "이 사건의 수수께끼는 모두 풀렸어"
        show cr_police at right
        ch_police "역시 자네야! 사건의 진상을 알려주게!"
        
        ## 수정중
        $ killer_name = renpy.input('범인은 ...')
        $ last_inventory=True
        DT "범인은 [killer_name]이야!"
        # $ users_result = renpy.input("내 생각에 범인과 범행도구는...")
        # $ if (users_result.find(범인이름 <- gtp한테 받아오는 범인 변수)>0) and (users_result.find(범행도구 <-gpt 한테 받아오는 도구 변수)):jump
        
        hide cr_Detective
        hide cr_police
        

        if (killer_name == '의뢰인'):
            $ ending_point += 100
        else :
            $ ending_point += 10   
        
        DT "범행 도구는..."
        jump inventory
        #### 여기까지 수정중     

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

        hide cr_Detective

    scene bg_villa_room1 
    show cr_villa_girl1 at right with dissolve

    if "girl1" not in Talk:
        $ Talk.add("girl1")
        ch_villa_girl1 "안녕하세요 탐정님"

    call screen villa_btn  

## room1 증거찾기맵    
label find_villa1 :
    $ visited.add("find_villa1")
    $ quick_menu = True
    hide cr_villa_girl1  # 캐릭터 지우기
    hide hospital_map
    #stop music 오류 장난아님ㅠ

    show screen text_timer
    call screen search_villa1
    #play music "audio/music/choose.mp3"
    ##증거
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
            show image_cookie with dissolve
            DT idle "맛있어 보이는 테스트용 쿠키다."
            #---
            $ see_point +=1
            $ hint.add("Shelf")
            hide item_hint2
            hide image_cookie

    if "1painting" not in hint :
        if _return is "room1_painting" :
            play sound "audio/sound/save.mp3"
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

        hide cr_Detective
 
    scene bg_villa_room2
    show cr_villa_girl2 with dissolve :
        xpos 378
        ypos 190  
    ##npc 추가할경우 상호작용##
    if "girl2" not in Talk:
        $ Talk.add("girl2")
        ch_villa_girl2 "안녕하세요 탐정님"
    call screen villa_btn

## room2 증거찾기맵    
label find_villa2 :
    $ visited.add("find_villa2")
    hide hospital_map
    hide cr_villa_girl2

    $ quick_menu = True
    show screen text_timer
    call screen search_villa2
    
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

        nvl clear
        hide cr_Detective
    
    scene bg_villa_living
    show cr_villa_man with dissolve :
        xpos 1300
        ypos 80
    if "man" not in Talk:
        $ Talk.add("man")
        ch_villa_man "안녕하세요 탐정님"
    call screen villa_btn  

## living room 증거찾기맵    
label find_villa3 :
    $ visited.add("find_villa3")
    $ quick_menu = True
    hide hospital_map
    hide cr_villa_man
    
    show screen text_timer
    call screen search_villa3

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