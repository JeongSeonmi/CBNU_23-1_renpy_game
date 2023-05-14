# 게임에서 사용할 이미지(배경, 캐릭터 등)
image bg_classRoom = "BG/room.jpg"
image bg_river = "BG/river.jpg"
image cr_jemin = "CR/jemin.png"
image cr_bora = "CR/bora.png"
image cr_mirea = "CR/mirea.png"

# 게임에서 사용할 캐릭터
define ch_jemin = Character('재민', color="#00531d")
define ch_mirea = Character('미래', color= "#C986BE")
define ch_bora = Character("보라", color = "#9d03fc")

define narrator = Character(None, kind = nvl)
define ch_narrator = Character(None)

# 여기에서부터 게임이 시작합니다.~return : 리턴은 메인메뉴로 돌아감
label start:
    scene bg_classRoom with fade
    show cr_bora at right 
    show cr_jemin at left
    with dissolve
    
    ch_bora "넌 내가 좋아?"
    
    $love_point = 0;  #변수 지정
    #변수는 문장이나 한 문자, 숫자, 참 거짓
    $my_name = "재민"
    $pi = 3.14
    $is_boy = True
    $is_girl = False
    
    menu :
        "좋아" :
            ch_jemin "좋아"
            $love_point += 1
        "싫어" :
            ch_jemin "싫어"
            $love_point -= 1

    ch_bora "너는 성별이 뭐야?"
    menu:
        "나는 남자야" :
            $is_boy = True
        "나는 여자야" :
            $is_girl = False

    if(love_point > 0 and is_boy):
        jump good_ending
    else:
        jump bad_ending

label good_ending :
    ch_bora "나도 너가 좋아"
    return
label bad_ending :
    ch_bora "나도 니가 싫어"
    return
