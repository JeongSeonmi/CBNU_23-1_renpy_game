# 게임에서 사용할 이미지(배경, 캐릭터 등)
image bg_villa = "BG/villa1.jpg"   
image bg_villa_living = "BG/villa_living.png"
image bg_villa_room1 = "BG/villa_room1.jpg"
image bg_villa_room2 = "BG/villa_room2.jpg"
image bg_room = "BG/room.jpg"
image cr_tam = "CR/pngegg.png"

# 게임에서 사용할 캐릭터
define ch_tam = Character('탐정', color="#00531d")
define ch_request = Character('의뢰인', color= "#C986BE")
define ch_men1 = Character("시민1", color = "#9d03fc")
define narrator = Character(None, kind = nvl)
define ch_narrator = Character(None)

define persistent.see_point = 0 
#방을 살펴봤을 경우, 나레이션이 사라지도록 변수 사용예정
#문제점 : 어떤 방을 살피고 다른 방을 살필 경우에도 나레이션이 사라져버림

# 여기에서부터 게임이 시작합니다.~return : 리턴은 메인메뉴로 돌아감
label start:
    $see_point = 0
    scene bg_room with fade
    "\n\n추리 실력이 뛰어난 김탐정 탐정,\n개신동에서 탐정사무소를 오픈하게 되었다."
    nvl clear #독백만 지워져야하는데 장소사진이 다시뜨는 문제
    show cr_tam at right
    ch_tam "의뢰가 들어왔네"
    
    ch_tam "사건 장소로 가볼까?"

    jump villa

label villa :
    scene bg_villa with fade
    show cr_tam at right
    ch_tam "어디부터 살펴볼까"
    menu : 
        "방1" :
            ch_tam "그래 방1부터 살펴보자"
            jump room1
        "방2" :
            ch_tam "그래 방2부터 살펴보자"
            jump room2
        "거실" :
            ch_tam "그래 거실부터 살펴보자"
            jump living_room
        "그만 살펴본다" :
            ch_tam "그래 이정도면 됐어."

label room1 :
    scene bg_villa_room1 with fade
    if(see_point < 1) :
        "\n\n방은 먼지가 많이 쌓인 상태이다."
        show cr_tam at right
        ch_tam "깨끗해보이는데 먼지가 많네.. 뭘 살펴볼까?"
    show cr_tam at right
    menu : 
        "침대" :
            ch_tam "(침대는 가지런히 정리되어 있다.) \n어? 머리끈이 있네?"
            $see_point +=1
            jump room1
        "선반" :
            ch_tam "(여러 장식품들이 놓여있다.) \n유난히 고양이 장식품들이 많네.."
            $see_point +=1
            jump room1
            
        "그림" :
            ch_tam "여긴 어떤 장소일까.."
            $see_point +=1
            jump room1
        "다른 곳을 살펴본다." :
            jump villa


            
    
label room2 :
    scene bg_villa_room2 with fade
    if(see_point < 1) :
        show cr_tam at right
        ch_tam "여긴 피해자가 머무던 방이야."
    show cr_tam at right
    menu : 
        "침대" :
            ch_tam "침대"
            $see_point +=1
            jump room2
        "옷장" :
            ch_tam "옷장"
            $see_point +=1
            jump room2
        "침대 밑" :
            ch_tam "침대밑"
            $see_point +=1
            jump room2
        "다른 곳을 살펴본다." :
            jump villa

label living_room :
    scene bg_villa_living with fade
    if(see_point < 1) :
        show cr_tam at right
        ch_tam "거실에는 사람이 많이 다녔을거야."
    show cr_tam at right
    menu : 
        "화분" :
            ch_tam "(화분은 햇빛을 못 받았는지 약간 시들어있다.)"
            $see_point +=1
            jump living_room
        "장식장" :
            ch_tam "(장식장에는 알 수 없는 장식품들이 가득하다)\n주인이 이런걸 좋아하는 걸까?"
            $see_point +=1
            jump living_room
        "쇼파" :
            ch_tam "(쇼파에서는 광이나고 있다.)"
            $see_point +=1
            jump living_room
        "다른 곳을 살펴본다." :
            jump villa