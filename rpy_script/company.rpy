label company : 
    #이름 정의할대 사진 이름은 (영어대문자철자두개_방이름) 예시 : HP_room, 라벨 이름은 (소문자철자네개_방이름) 예시 : hosp_room
    $ myP = "company"

init python:
    #추리점수&방 탐색
    see_point = 0 
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
    #방 이미지
    image bg_CP = "BG/CP.png"   
    image bg_CP_office1 = "BG/CP_office1.png"
    image bg_CP_office2 = "BG/CP_office2.png"
    image bg_CP_room = "BG/CP_room.png"
    image bg_lab = "gui/Background.jpg"

    ## 사무실 201호 증거찾기   // 위치만 설정 완료, 변수명 바꿔야함
    screen comp_office1_search : 
        imagemap :
                        
            ground "BG/CP_office1.png"
            hotspot(537, 553, 122, 112) action Return("room1_Bed") #왼쪽 컴퓨터 
            hotspot(1138, 574, 56, 176) action Return("Shelf") #가운데 서랍
            hotspot(522, 390, 136, 172) action Return("room1_painting") #창문에 빨간색..? 피라고 합시다
            
            imagebutton idle "gui/button/btn_return.png" action Jump("company") xalign 0.01 yalign 0.96
            

    ## 사무실 202호 증거찾기
    screen comp_office2_search : 
        imagemap :
            
            ground "BG/CP_office2.png"
            hotspot(1289, 138, 408, 322) action Return("room2_Bed") #오른쪽 큰화분
            hotspot(323, 631, 91, 222) action Return("dressing_table") #왼쪽 서랍
            hotspot(1733, 149, 150, 690) action Return("Table") #오른쪽 문
            
            imagebutton idle "gui/button/btn_return.png" action Jump("company") xalign 0.01 yalign 0.96

    ## 휴게실 증거찾기
    screen comp_room_search : 
        imagemap :
            
            ground "BG/CP_room.png"
            hotspot(238, 365, 105, 253) action Return("post") #책장
            hotspot(1322, 369, 110, 134) action Return("living_painting") #게시판
            hotspot(2, 607, 97, 176) action Return("test3") #왼쪽 컴퓨터

            imagebutton idle "gui/button/btn_return.png" action Jump("company") xalign 0.01 yalign 0.96

    ## 지도
    screen comp_map :
            imagemap :
                    xalign 0.5
                    yalign 0.5
                    ground "BG/map.png"
                    hotspot(19, 20, 461, 155) action Jump("comp_office1")
                    hotspot(19, 179, 220, 292) action Jump("comp_office2")
                    hotspot(600, 247, 199, 158) action Jump("comp_room")
                    imagebutton idle "gui/button/icon_exit.png" action Hide("comp_map")

## 본 스크립트 ##
scene bg_CP with dissolve
show cr_Detective at right
hide screen back_menu

if not main_point :
    $main_point = True
    DT "어디부터 살펴볼까"
menu : 
    "사무실 201호" :
        DT "그래 사무실 201호부터 살펴보자"
        $ myP = "comp_office1"
        jump comp_office1
    "사무실 202호" :
        DT "그래 진료실 202호부터 살펴보자"
        $ myP = "comp_office2"
        jump comp_office2
    "휴게실" :
        DT "그래 휴게실부터 살펴보자"
        $ myP = "comp_room"
        jump comp_room
    "그만 살펴본다" :
        $ myP = "company"
        DT "그래 이정도면 됐어."
        $killer_name = renpy.input('범인은 ...')
        if (killer_name == '의뢰인') and (see_point < 5):
            jump comp_bad_ending1
        elif (killer_name == '의뢰인') and (see_point > 4):
            jump comp_good_ending
        else :
            jump comp_bad_ending2

## office1
label comp_office1 :
    scene bg_CP_office1 with dissolve
    hide screen comp_map
    if not see_point_office1 :
        $see_point_office1 = True
        "\n\n방은 먼지가 많이 쌓인 상태이다."
        nvl clear
        show cr_Detective at right
        DT "깨끗해보이는데 먼지가 많네.. 뭘 살펴볼까?"
    hide cr_Detective
    call screen comp_office1_search ## 이미지맵(클릭으로 힌트찾는 부분)

    ##증거
    if not see_point_1bed :
        $see_point_1bed = True
        if _return is "room1_Bed":
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "(침대는 가지런히 정리되어 있다.) \n어? 머리끈이 있네?"

    if not see_point_Shelf :
        $see_point_Shelf = True
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
        $see_point_1painting = True
        if _return is "room1_painting" :
            $ item_painting.pickup(1)
            show item_hint4 with dissolve :
            DT idle "여긴 어떤 장소일까.."
    
    jump comp_office1

## office2
label comp_office2 :
    scene bg_CP_office2 with dissolve
    hide screen comp_map
    #show screen notify("   사무실 202호   ")
    if not see_point_office2 :
        $see_point_office2 = True
        "\n\n어젯밤에 이 방에서 살인사건이 일어났어."
        nvl clear
        show cr_Detective at right
        DT "여긴 피해자가 머무던 방이야."
    hide cr_Detective
    call screen comp_office2_search ## 이미지맵(클릭으로 힌트찾는 부분)

    ##증거
    if not see_point_2bed :
        $see_point_2bed = True
        if _return is "room2_Bed":
            #$ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "피해자는 이 침대에서 자고 있었어"

    if not see_point_dressing_table :
        $see_point_dressing_table = True
        if _return is "dressing_table" :
            #$ item_painting.pickup(1)
            show item_hint3 with dissolve :
            DT idle "(깨진 유리 조각이 있다)"
            DT "어쩌다 깨진걸까"

    if not see_point_Table :
        $see_point_Table = True
        if _return is "Table" :
            #$ item_painting.pickup(1)
            show item_hint2 with dissolve :
            DT idle "무언가를 먹은 흔적이 있다."
    
    jump comp_office2


## room
label comp_room :
    scene bg_CP_room with dissolve
    hide screen comp_map
    #show screen notify("   휴게실   ") 
    if not see_point_room :
        $see_point_room = True
        "\n\n넓은 거실에 가구가 몇 개 없어서 쓸쓸한 느낌이 든다."
        nvl clear
        show cr_Detective at right
        DT "거실에는 사람이 많이 다녔을거야."
    hide cr_Detective
    call screen comp_room_search ## 이미지맵(클릭으로 힌트찾는 부분)
    
    ##증거
    if not see_point_post :
        $see_point_post = True
        if _return is "post":
            $ item_post.pickup(1)
            show item_hint1 with dissolve :
            DT idle "이 쪽지의 내용은 추리하는데 도움되겠어"
            DT idle "자세히 보니 용의자들끼리 역할 분담한 내용을 적어놓은 것 같아."    

    if not see_point_Lpainting :
        $see_point_Lpainting = True
        if _return is "living_painting" :
            $ item_painting.pickup(1)
            show item_hint2 with dissolve :
            DT idle "이 그림은 고가의 그림인 것 같은데 "

    jump comp_room
