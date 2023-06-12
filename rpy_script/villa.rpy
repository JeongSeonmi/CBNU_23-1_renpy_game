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
    image villa_map = im.FactorScale("BG/villa_map.png", 1.3)

    ## 방1 증거찾기
    screen search_villa1 : 
        zorder 99
        imagemap :
            ground "BG/villa_room1.jpg" ## 리턴할 값이랑 증거(곂쳐도 될거같긴 한데) 다시 못찾게할 변수 이름(곂쳐도 됨) 정하기
            hotspot(732, 487, 60, 58) action Return("hint1") #작은 그림
            hotspot(526, 394, 130, 162) action Return("hint2") #중간 그림
            hotspot(105, 272, 287, 343) action Return("hint3") # 큰 그림
            hotspot(1232, 725, 335, 144) action Return("hint4") #베개 밑
            hotspot(1331, 575, 76, 119) action Return("hint5") #수면등
            hotspot(181, 767, 209, 136) action Return("hint6") #큰 그림 밑 물건
            hotspot(891, 327, 392, 319) action Return("hint7") #그냥 창문
            hotspot(477, 33, 434, 197) action Return("hint8") #그냥 천장

            imagebutton idle "return_btn" :
                xalign 0.01
                yalign 0.96
                action [Hide("text_timer"), Jump("villa_room1")]
            
    ## 방2 증거찾기
    screen search_villa2 :
        zorder 99 
        imagemap :
            ground "BG/villa_room2.jpg"
            hotspot(1213, 682, 361, 125) action Return("hint1") #침대 위
            hotspot(888, 665, 263, 63) action Return("hint2") #테이블 위
            hotspot(538, 599, 187, 142) action Return("hint3") #화장대
            hotspot(833, 336, 378, 278) action Return("hint4") #그냥 창문
            hotspot(892, 4, 231, 181) action Return("hint5") #전등
            hotspot(570, 952, 741, 117) action Return("hint6") #그냥 바닥
            hotspot(1652, 114, 175, 261) action Return("hint7") #그냥 벽
            hotspot(18, 173, 366, 893) action Return("hint8") #문


            imagebutton idle "return_btn" :
                xalign 0.01
                yalign 0.96
                action [Hide("text_timer"), Jump("villa_room2")]

    ## 거실 증거찾기
    screen search_villa3 : 
        zorder 99
        imagemap :        
            ground "BG/villa_living.png"
            hotspot(294, 593, 34, 35) action Return("hint1") #왼쪽 TV밑 쪽지
            hotspot(782, 328, 171, 136) action Return("hint2") #가운데 그림
            hotspot(1754, 544, 165, 321) action Return("hint3") #오른쪽 장식장
            hotspot(558, 701, 513, 128) action Return("hint4") #테이블 위
            hotspot(0, 242, 143, 584) action Return("hint5") #왼쪽 작은 문
            hotspot(225, 328, 183, 213) action Return("hint6") #티비 모니터
            hotspot(570, 930, 439, 129) action Return("hint7") #테이블 아래
            hotspot(1811, 117, 108, 371) action Return("hint8") #오른쪽 거울

            imagebutton idle "return_btn" :
                xalign 0.01
                yalign 0.96
                action [Hide("text_timer"), Jump("villa_living")]

    ## 지도   
    screen villa_map :
        zorder 100
        imagemap :
            xalign 0.25
            yalign 0.45
            ground "villa_map"
            hotspot(276, 301, 158, 178) action Jump("villa_room1")
            hotspot(240, 12, 195, 164) action Jump("villa_room2")
            hotspot(7, 173, 238, 302) action Jump("villa_living")
            
            imagebutton idle "gui/button/icon_exit.png" action Hide("villa_map")
    
    screen villa_btn :
        imagebutton idle "find_idle_btn" hover "find_hover_btn":
            xpos 927
            ypos 350
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
            ypos 498
            action [
                If(myR == "room1",
                    If("talk_suspecter1" not in visited, Jump("talk_suspecter1"))
                ),
                If(myR == "room2",
                    If("talk_suspecter2" not in visited, Jump("talk_suspecter2"))
                ),
                If(myR == "living",
                    If("talk_suspecter3" not in visited, Jump("talk_suspecter3"))
                ),
                Jump("error")
            ]
        
        imagebutton idle "gui/button/btn_return.png" :
            activate_sound "audio/sound/select.mp3"
            xalign 0.01
            yalign 0.96
            action Jump("villa")

## 본 스크립트 ##
hide screen villa_map
scene bg_villa
show cr_Detective at right with dissolve
$ quick_menu = False

if "villa_main" not in visited: 
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
                
        $ killer_name = renpy.input('범인은 ...')
        $ last_inventory=True
        DT "범인은 [killer_name]이야!"
        
        hide cr_Detective
        hide cr_police
        
        if (killer_name == killer):
            $ ending_point += 100
        else :
            $ ending_point += 10   
        
        DT "범행 도구는..."
        jump inventory 

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
        ch_villa_girl1 "탐정님! 저는 이 사건과 관련이 없어요!"

    call screen villa_btn  

## room1 증거찾기맵    
label find_villa1 :
    $ visited.add("find_villa1")
    $ quick_menu = True
    hide cr_villa_girl1  # 캐릭터 지우기
    hide hospital_map
    #stop music 오류 장난아님

    show screen text_timer
    call screen search_villa1
    #play music "audio/music/choose.mp3"
    ##증거
    if "room1_hint1" not in hint : #작은 그림
        if _return is "hint1":
            #play sound "audio/sound/save.mp3"
            # 일부러 아이템 안넣음.pickup(1)
            #show item_villa_picture with dissolve :
            DT idle "(평범한 인테리어용 그림이다.)"
            $ hint.add("room1_hint1")
            #hide item_villa_picture
            
    if "room1_hint2" not in hint : #중간 그림
        if _return is "hint2" :
            play sound "audio/sound/save.mp3"
            $ InvItem(*item_villa_picture2).pickup(1)
            show item_villa_picture2 with dissolve :
            DT idle "별장 주인의 취향이 드러나는 값비싼 그림이다. 단서가 될 수 있을까?"
            #---인벤 테스트 구역
            #$ item_cookie.pickup(1)
            #show image_cookie with dissolve
            #DT idle "맛있어 보이는 테스트용 쿠키다."
            #---
            #$ see_point +=1
            $ hint.add("room1_hint2")
            hide item_villa_picture2
            #hide image_cookie

    if "room1_hint3" not in hint : #큰 그림
        if _return is "hint3" :
            play sound "audio/sound/save.mp3"
            $ InvItem(*item_villa_picture1).pickup(1)
            show item_hint4 with dissolve :
            DT idle "(고급스러워보이는 풍경화이다.)\n이건 뭐지?"
            $ hint.add("room1_hint3")
            hide item_hint4

    if "room1_hint4" not in hint : #베개 밑
        if _return is "hint4":
            play sound "audio/sound/save.mp3"
            $ InvItem(*item_post).pickup(1)
            show mini_post with dissolve :
            DT idle "이게 뭐야"
            $ hint.add("room1_hint4")
            hide mini_post

    if "room1_hint5" not in hint : #수면등
        if _return is "hint5":
            play sound "audio/sound/save.mp3"
            $ InvItem(*item_villa_gun).pickup(1)
            show item_villa_gun with dissolve :
            DT idle "취미가 사냥인 사람이 있었나?"
            $ hint.add("room1_hint5")
            hide item_villa_gun

    if "room1_hint6" not in hint : #큰 그림 밑 물건
        if _return is "hint6":
            play sound "audio/sound/save.mp3"
            $ InvItem(*item_villa_deco).pickup(1)
            show item_villa_deco with dissolve :
            DT idle "(장식물이 무겁고 단단해보인다.)\n유난히 고양이 장식품들이 많네.."
            $ hint.add("room1_hint6")
            hide item_villa_deco

    if "room1_hint7" not in hint : #그냥 창문
        if _return is "hint7":
            play sound "audio/sound/save.mp3"
            $ InvItem(*item_villa_sight).pickup(1)
            
            show item_villa_sight with dissolve :
            DT idle "밖은 이러한 풍경이군.\n혹시 단서가 될까?"
            $ hint.add("room1_hint7")
            hide item_villa_sight
    
    if "room1_hint8" not in hint : #그냥 천장
        if _return is "hint8":
            #play sound "audio/sound/save.mp3"
            $ InvItem(*item_post).pickup(1)
            #show item_hint1 with dissolve :
            DT idle "(천장에는 아무것도 없다.)"
            $ hint.add("room1_hint8")
            #hide item_hint1

    jump find_villa1
    return 

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
        ch_villa_girl2 "하아... 안녕하세요.."
    call screen villa_btn

## room2 증거찾기맵    
label find_villa2 :
    $ visited.add("find_villa2")
    hide hospital_map
    hide cr_villa_girl2

    $ quick_menu = True
    show screen text_timer
    call screen search_villa2
    
    if "room2_hint1" not in hint : #침대 위
        if _return is "hint1":
            play sound "audio/sound/save.mp3"
            $ InvItem(*item_villa_pillow).pickup(1)
            
            show item_villa_pillow with dissolve :
            DT idle "베개군. 베개가 터진 점이 수상해."
            $ hint.add("room2_hint1")
            hide item_villa_pillow
            
    
    if "room2_hint2" not in hint : #테이블 위
        if _return is "hint2" :
            play sound "audio/sound/save.mp3"
            
            $ InvItem(*item_villa_knife).pickup(1)
            show item_villa_knife with dissolve :
            DT idle "주방에 있어야 할 식칼이 왜 방에서 나오지?"
            $ hint.add("room2_hint2")
            hide item_villa_knife


    if "room2_hint3" not in hint : #화장대
        if _return is "hint3" :
            play sound "audio/sound/save.mp3"
            
            $ InvItem(*item_painting).pickup(1)
            show item_villa_deco with dissolve :
            DT idle "장식물이 무겁고 단단해보인다."
            $ hint.add("room2_hint3")
            hide item_villa_deco

    if "room2_hint4" not in hint : #그냥 창문
        if _return is "hint4":
            play sound "audio/sound/save.mp3"
            $ InvItem(*item_villa_sight).pickup(1)
           
            show item_villa_sight with dissolve :
            DT idle "밖은 이러한 풍경이군. 혹시 단서가 될까?"
            $ hint.add("room2_hint4")
            hide item_villa_sight

    if "room2_hint5" not in hint : #전등
        if _return is "hint5":
            #play sound "audio/sound/save.mp3"
            #$ InvItem(*item_post).pickup(1)

            #show item_hint1 with dissolve :
            DT idle "(평범한 전등이다. 관리를 안했는지 벌레시체가 쌓여있다.)"
            $ hint.add("room2_hint5")
            #hide item_hint1

    if "room2_hint6" not in hint : #그냥 바닥
        if _return is "hint6":
            play sound "audio/sound/save.mp3"
            $ InvItem(*item_villa_syringe).pickup(1)
            
            show item_villa_syringe with dissolve :
            DT idle "(병원에서 많이 쓰는 주사기이다)\n이게 왜 여기있는걸까.."
            $ hint.add("room2_hint6")
            hide item_villa_syringe

    if "room2_hint7" not in hint : #그냥 벽
        if _return is "hint7":
            play sound "audio/sound/save.mp3"
            $ InvItem(*item_villa_memo).pickup(1)
            
            show item_villa_memo with dissolve :
            DT idle "이건 대체 무슨 내용일까?"
            $ hint.add("room2_hint7")
            hide item_villa_memo
    
    if "room2_hint8" not in hint : #문
        if _return is "hint8":
            #play sound "audio/sound/save.mp3"
            #$ InvItem(*item_post).pickup(1)
            
            #show item_hint1 with dissolve :
            DT idle "(내가 방금 들어왔던 문이다.\n특별히 살펴볼 부분은 없는 것 같다.)"
            $ hint.add("room2_hint8")
            #hide item_hint1

    jump find_villa2
    return 

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
        ch_villa_man "난 정말 아무 상관없다고!"
    call screen villa_btn  

## living room 증거찾기맵    
label find_villa3 :
    $ visited.add("find_villa3")
    $ quick_menu = True
    hide hospital_map
    hide cr_villa_man
    
    show screen text_timer
    call screen search_villa3

    if "living_hint1" not in hint : #왼쪽 TV밑 쪽지
        if _return is "hint1":
            play sound "audio/sound/save.mp3"
            $ InvItem(*item_villa_memo).pickup(1)
            
            show item_villa_memo with dissolve :
            DT idle "이건 대체 무슨 내용일까?"
            $ hint.add("living_hint1")
            hide item_villa_memo
            
    
    if "living_hint2" not in hint : #가운데 그림
        if _return is "hint2" :
            play sound "audio/sound/save.mp3"
            
            $ InvItem(*item_painting).pickup(1)
            show item_hint2 with dissolve :
            DT idle "고급스러워보이는 풍경화이다."
            $ hint.add("living_hint2")
            hide item_hint2

    if "living_hint3" not in hint : #오른쪽 장식장
        if _return is "hint3" :
            play sound "audio/sound/save.mp3"
            $ InvItem(*item_villa_rope).pickup(1)
            
            show item_villa_rope with dissolve :
            DT idle "적당한 길이의 밧줄이다"
            $ hint.add("living_hint3")
            hide item_villa_rope

    if "living_hint4" not in hint : #테이블 위
        if _return is "hint4":
            play sound "audio/sound/save.mp3"
            
            $ InvItem(*item_villa_coffee).pickup(1)
            show item_villa_coffee with dissolve :
            DT idle "흔히 볼 수 있는 커피다."
            $ hint.add("living_hint4")
            hide item_villa_coffee

    if "living_hint5" not in hint : #작은 문
        if _return is "hint5":
            play sound "audio/sound/save.mp3"
            $ InvItem(*item_villa_saw).pickup(1)
            
            show item_villa_saw with dissolve :
            DT idle "(문 바로 옆에 톱이 놓여있다.)\n무척 날카로운 톱이네.\n 무엇이든 자를 수 있을 것 같아."
            $ hint.add("living_hint5")
            hide item_villa_saw

    if "living_hint6" not in hint : #티비 모니터
        if _return is "hint6":
            play sound "audio/sound/save.mp3"
            
            $ InvItem(*item_villa_monitor).pickup(1)
            show item_villa_monitor with dissolve :
            DT idle "모니터이다.\n여기 안에 단서가 있을지도 몰라."
            $ hint.add("living_hint6")
            hide item_villa_monitor

    if "living_hint7" not in hint : #테이블 아래
        if _return is "hint7":
            play sound "audio/sound/save.mp3"
            
            $ InvItem(*item_villa_glass).pickup(1)
            show item_villa_glass with dissolve :
            DT idle "(깨진 유리조각이다.)\n무슨일이 있었던 거지?"
            $ hint.add("living_hint7")
            hide item_villa_glass
    
    if "living_hint8" not in hint : #오른쪽 거울
        if _return is "hint8":
            play sound "audio/sound/save.mp3"
            $ InvItem(*item_villa_monitor).pickup(1)
           
            show villa_mirror with dissolve :
            DT idle "(나의 모습이 비친다.)\n오늘도 잘생겼군"
            $ hint.add("living_hint8")
            hide villa_mirror

    jump find_villa3
    return 