## 게임에서 사용할 이미지(배경, 캐릭터 등) ##   
init :    
    $ style.window.left_padding = 220

    # 게임에서 사용할 캐릭터(이름, 이미지태그)
    define narrator = Character(None, kind = nvl,color = "#000000")
 
    define DT = Character('탐정', image="cr_Detective")
    define ch_request = Character('의뢰인', color = "#000000")
    define ch_men1 = Character("용의자 1", image="cr_man1")
    define ch_police = Character('경찰', image="cr_police") 
    image cr_Detective = im.FactorScale("CR/DT.png", 0.9)
    image side cr_Detective idle = "/CR/DT_side_idle.png" #사이드 이미지
    image cr_men1 = im.FactorScale("CR/men1.png", 1.3)
    image cr_police = im.FactorScale("CR/police.png", 1.7)

    #회사 캐릭터
    define ch_CP_woman = Character('정직원', image="cr_CP_woman")
    image cr_CP_woman = im.FactorScale("CR/CP_woman.png", 1.4)

    #병원 캐릭터
    define ch_HP_nurse1 = Character('최간호', image="cr_HP_nurse1")
    define ch_HP_nurse2 = Character('김호순', image="cr_HP_nurse2")
    define ch_HP_doctor = Character('이박사', image="cr_HP_doctor")
    image cr_HP_nurse1 = im.FactorScale("CR/HP_Nurse1.png", 1.3)
    image cr_HP_nurse2 = im.FactorScale("CR/HP_Nurse2.png", 1.3)
    image cr_HP_doctor = im.FactorScale("CR/HP_Doctor1.png", 1.8)

    #별장 캐릭터
    define ch_villa_man = Character('김음악', image="cr_villa_man")
    define ch_villa_girl1 = Character('이미술', image="cr_villa_girl1")
    define ch_villa_girl2 = Character('박체육', image="cr_villa_girl2")
    image cr_villa_man = im.FactorScale("CR/villa_man.png", 1.85)
    image cr_villa_girl1 = im.FactorScale("CR/villa_girl1.png", 1.7)
    image cr_villa_girl2 = im.FactorScale("CR/villa_girl2.png", 1.3)

    #상호작용 버튼 이미지
    image find_idle_btn = im.FactorScale("gui/button/find_idle_ui.png", 0.6)
    image talk_idle_btn = im.FactorScale("gui/button/talk_idle_ui.png", 0.6)
    image find_hover_btn = im.FactorScale("gui/button/find_ui.png", 0.6)
    image talk_hover_btn = im.FactorScale("gui/button/talk_ui.png", 0.6)
    image return_btn = "gui/button/btn_return.png"

    #증거품 이미지 *이름 변수명 다시 지어야함
    image item_hint1 : #메모
        im.FactorScale("Items/pngegg.png", 0.5)
        xpos 720
        ypos 245
    image item_hint2 : #거실 그림
        "Items/monariza.png" 
        xpos 720
        ypos 245

    image item_hint3 : #유리컵
        im.FactorScale("Items/Glass.jpg", 0.4) 
        xpos 720
        ypos 300
    
    image item_hint4 : #방1 그림
        im.FactorScale("Items/room1_painting.png", 0.6) 
        xpos 720
        ypos 300

    image image_cookie : #인벤토리 테스트용
        im.FactorScale("Items/item_cookie.jpg", 10)
        yalign 0.5
        xalign 0.5

    #병원 증거 이미지
    image image_cookie : #인벤토리 테스트용
        im.FactorScale("Items/item_cookie.jpg", 10)
        yalign 0.5
        xalign 0.5
    image item_hospital_drug: #인벤토리 테스트용
        im.FactorScale("Items/item_hospital_drug.jpg", 10)
        yalign 0.5
        xalign 0.5
    image item_hospital_knife: #인벤토리 테스트용
        im.FactorScale("Items/item_hospital_knife.jpg", 10)
        yalign 0.5
        xalign 0.5
    image item_hospital_sytinge: #인벤토리 테스트용
        im.FactorScale("Items/item_hospital_sytinge.jpg", 10)
        yalign 0.5
        xalign 0.5

    #회사 증거 이미지
    image item_company_computer: #인벤토리 테스트용
        im.FactorScale("Items/item_company_computer.jpg", 10)
        yalign 0.5
        xalign 0.5
    image item_company_hotsix: #인벤토리 테스트용
        im.FactorScale("Items/item_company_hotsix.jpg", 10)
        yalign 0.5
        xalign 0.5
    image item_company_cctv: #인벤토리 테스트용
        im.FactorScale("Items/item_company_cctv.jpg", 10)
        yalign 0.5
        xalign 0.5
    image item_company_knife: #인벤토리 테스트용
        im.FactorScale("Items/item_company_knife.jpg", 10)
        yalign 0.5
        xalign 0.5
    image item_company_nameteg: #인벤토리 테스트용
        im.FactorScale("Items/item_company_nameteg.jpg", 10)
        yalign 0.5
        xalign 0.5

    #별장 증거 이미지    
    image item_villa_gun: #인벤토리 테스트용
        im.FactorScale("Items/item_villa_gun.jpg", 10)
        yalign 0.5
        xalign 0.5
    image item_villa_knife: #인벤토리 테스트용
        im.FactorScale("Items/item_villa_knife", 10)
        yalign 0.5
        xalign 0.5
    image item_villa_rope: #인벤토리 테스트용
        im.FactorScale("Items/item_villa_rope", 10)
        yalign 0.5
        xalign 0.5
    image item_villa_saw: #인벤토리 테스트용
        im.FactorScale("Items/item_villa_saw.jpg", 10)
        yalign 0.5
        xalign 0.5
    
   

    # 증거 정의
    define item_cookie = InvItem(_("Cookie"), "item_cookie", 8, _("맛있는 테스트용 쿠키입니다!"), "item_cookie")
    define item_post = InvItem(_("post"), "item_post", 8, _("용의자들의 역할이 적힌 메모"), "item_post")
    define item_painting = InvItem(_("painting"), "item_painting", 8, _("값비싸 보이는 그림이다"), "item_painting")
