label hospital :
    #이름 정의할대 사진 이름은 (영어대문자철자두개_방이름) 예시 : HP_room
    $ myP = "hospital"

init python:
    #추리점수&방 탐색
    see_point_office1 = False  #방에 처음 갔을 때
    see_point_1bed = 0         #아이템을 처음 확인 했을 때
    see_point_Shelf = 0
    see_point_1painting = 0

    see_point_office2 = False
    see_point_2bed = 0
    see_point_dressing_table = 0
    see_point_Table = 0
    
    see_point_room = False
    see_point_post = 0
    see_point_Lpainting = 0


## 게임에서 사용할 이미지(배경, 캐릭터 등) ##   
init :
    ##방 이미지
    image bg_HP = "BG/HP.png"   
    image bg_HP_office1 = "BG/HP_office.png"
    image bg_HP_office2 = "BG/HP_office2.png"
    image bg_HP_room = "BG/HP_room.png"
    image bg_lab = "gui/Background.jpg"

    ## 진료실 101호 증거찾기  // 위치만 설정 완료, 변수명 바꿔야함
    screen hospital_office1_search : 
        imagemap :
            
            ground "BG/HP_office.png"
            hotspot(1048, 500, 141, 53) action Return("room1_Bed")  #책상 위
            hotspot(100, 261, 218, 92) action Return("Shelf") #책장
            hotspot(477, 265, 209, 199) action Return("room1_painting") #게시판
            
            imagebutton idle "gui/button/btn_return.png" action Jump("hospital") xalign 0.01 yalign 0.96

    #만약 단서를 다 찾으면 다 찾았다는 문구 출력

    ## 진료실 102호 증거찾기
    screen hospital_office2_search : 
        imagemap :
                      
            ground "BG/HP_office2.png"
            hotspot(1331, 414, 33, 112) action Return("room2_Bed") #작은 책장
            hotspot(608, 158, 374, 390) action Return("dressing_table") #창문
            hotspot(1727, 768, 170, 258) action Return("Table") #오른쪽 서랍
            
            imagebutton idle "gui/button/btn_return.png" action Jump("hospital") xalign 0.01 yalign 0.96
    
    ## 병실 증거찾기
    screen hospital_room_search : 
        imagemap :
            
            ground "BG/HP_room.png"
            hotspot(328, 700, 109, 175) action Return("post") #갈색 서랍
            hotspot(717, 988, 197, 78) action Return("living_painting") #침대 밑
            hotspot(918, 505, 208, 107) action Return("test3") #왼쪽 커튼 뒤

            imagebutton idle "gui/button/btn_return.png" action Jump("hospital") xalign 0.01 yalign 0.96
    
    ## 지도
    screen hospital_map :
        imagemap :
                xalign 0.5
                yalign 0.5
                ground "BG/map.png"
                hotspot(19, 20, 461, 155) action Jump("hospital_office1")
                hotspot(19, 179, 220, 292) action Jump("hospital_office2")
                hotspot(600, 247, 199, 158) action Jump("hospital_room")
                imagebutton idle "gui/button/icon_exit.png" action Hide("hospital_map")
    
## 본 스크립트 ##
scene bg_HP with dissolve
show cr_Detective at right with dissolve
hide screen back_menu

if not main_point :
    $ main_point = True
    DT "어디부터 살펴볼까"
menu : 
    "진료실 101호" :
        DT "그래 진료실 101호부터 살펴보자"
        jump hospital_office1

    "진료실 102호" :
        DT "그래 진료실 102호부터 살펴보자"
        jump hospital_office2

    "병실" :
        DT "그래 병실부터 살펴보자"
        jump hospital_room  

    "그만 살펴본다" :
        DT "그래 이정도면 됐어."
        $killer_name = renpy.input('범인은 ...')
        if (killer_name == '의뢰인') and (see_point < 5):
            jump bad_ending1
        elif (killer_name == '의뢰인') and (see_point > 4):
            jump good_ending
        else :
            jump bad_ending2

## office1
label hospital_office1 :
    scene bg_HP_office1 with dissolve
    hide screen hospital_map
    if not see_point_office1 :
        $ see_point_office1 = True
        "\n\n방은 먼지가 많이 쌓인 상태이다."
        nvl clear
        show cr_Detective at right
        DT "깨끗해보이는데 먼지가 많네.. 뭘 살펴볼까?"
    hide cr_Detective

    call screen hospital_office1_search ## 이미지맵(클릭으로 힌트찾는 부분)
    
    ##증거
    if not see_point_1bed :
        $ see_point_1bed  = True
        if _return is "room1_Bed":
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "(침대는 가지런히 정리되어 있다.) \n어? 머리끈이 있네?"
            
    if not see_point_Shelf :
        $ see_point_Shelf = True
        if _return is "Shelf" :
            $ item_painting.pickup(1)
            show item_hint2 with dissolve :
            DT idle "(여러 장식품들이 놓여있다.) \n유난히 고양이 장식품들이 많네.."
            #---인벤 테스트 구역
            $ item_cookie.pickup(1)
            show image_cookie with dissolve :
            DT idle "맛있어 보이는 테스트용 쿠키다."
            #---
            $see_point +=1

    if not see_point_1painting :
        $ see_point_1painting  = True
        if _return is "room1_painting" :
            $ item_painting.pickup(1)
            show item_hint4 with dissolve :
            DT idle "여긴 어떤 장소일까.."
    
    jump hospital_office1

## office2
label hospital_office2 :
    scene bg_HP_office2 with dissolve
    hide screen hospital_map

    if not see_point_office2 :
        $ see_point_office2 = True
        "\n\n어젯밤에 이 방에서 살인사건이 일어났어."
        nvl clear
        show cr_Detective at right
        DT "여긴 피해자가 머무던 방이야."
    hide cr_Detective

    call screen hospital_office2_search ## 이미지맵(클릭으로 힌트찾는 부분)

    ##증거
    if not see_point_2bed :
        $ see_point_2bed = True
        if _return is "room2_Bed" :
            #$ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "피해자는 이 침대에서 자고 있었어"
        
    if not see_point_dressing_table :
        $ see_point_dressing_table = True
        if _return is "dressing_table" :
            #$ item_painting.pickup(1)
                show item_hint3 with dissolve :
                DT idle "(깨진 유리 조각이 있다)"
                DT "어쩌다 깨진걸까"
        
    if not see_point_Table :
        $ see_point_Table = True
        if _return is "Table" :
            #$ item_painting.pickup(1)
            show item_hint2 with dissolve :
            DT idle "무언가를 먹은 흔적이 있다."
    
    jump hospital_office2


## room
label hospital_room :
    scene bg_HP_room with dissolve
    hide screen hospital_map
    if not see_point_room :
        $ see_point_room = True
        "\n\n넓은 거실에 가구가 몇 개 없어서 쓸쓸한 느낌이 든다."
        nvl clear
        show cr_Detective at right
        DT "거실에는 사람이 많이 다녔을거야."
    hide cr_Detective

    call screen hospital_room_search ## 이미지맵(클릭으로 힌트찾는 부분)

    ##증거
    if not see_point_post :
        $ see_point_post = True
        if _return is "post":
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "이 쪽지의 내용은 추리하는데 도움되겠어"
            DT idle "자세히 보니 용의자들끼리 역할 분담한 내용을 적어놓은 것 같아."    

    if not see_point_Lpainting :
        $ see_point_Lpainting = True
        if _return is "living_painting" :
            $ item_painting.pickup(1)
            show item_hint2 with dissolve :
            DT idle "이 그림은 고가의 그림인 것 같은데 "

    jump hospital_room
