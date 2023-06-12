## 게임에서 사용할 이미지(배경, 캐릭터 등) ##   
init :    
    $ style.window.left_padding = 220
    define suspecter1 = ""
    define suspecter2 = ""
    define suspecter3 = ""
    define killer = ""
    
    # 게임에서 사용할 캐릭터(이름, 이미지태그)
    define narrator = Character(None, kind = nvl,color = "#000000")
 
    define DT = Character('탐정', image="cr_Detective")

    
    define ch_request = Character('의뢰인', color = "#000000")
    define ch_men1 = Character(suspecter1 , image="cr_man1")
    define ch_police = Character('경찰', image="cr_police") 
    image cr_Detective = im.FactorScale("CR/DT.png", 0.9)
    image side cr_Detective idle = "/CR/DT_side_idle.png" #사이드 이미지
    image cr_men1 = im.FactorScale("CR/men1.png", 1.3)
    image cr_police = im.FactorScale("CR/police.png", 1.7)

    #회사 캐릭터
    define ch_CP_woman = Character('suspecter3', dynamic = True)
    define ch_CP_man1 = Character('suspecter1', dynamic = True)
    define ch_CP_man2 = Character('suspecter2', dynamic = True)

    image cr_CP_woman = im.FactorScale("CR/CP_woman.png", 1.4)
    image cr_CP_man1 = im.FactorScale("CR/CP_man1.png", 1.4)
    image cr_CP_man2 = im.FactorScale("CR/CP_man2.png", 2.0)

    #병원 캐릭터
    define ch_HP_nurse1 = Character('suspecter2', dynamic = True)
    define ch_HP_nurse2 = Character('suspecter3', dynamic = True)
    define ch_HP_doctor = Character('suspecter1', dynamic = True)
    image cr_HP_nurse1 = im.FactorScale("CR/HP_Nurse1.png", 1.3)
    image cr_HP_nurse2 = im.FactorScale("CR/HP_Nurse2.png", 1.3)
    image cr_HP_doctor = im.FactorScale("CR/HP_Doctor1.png", 1.8)

    #별장 캐릭터
    define ch_villa_man = Character('suspecter3', dynamic = True)
    define ch_villa_girl1 = Character('suspecter1', dynamic = True)
    define ch_villa_girl2 = Character('suspecter2', dynamic = True)
    image cr_villa_man = im.FactorScale("CR/villa_man.png", 1.85)
    image cr_villa_girl1 = im.FactorScale("CR/villa_girl1.png", 1.7)
    image cr_villa_girl2 = im.FactorScale("CR/villa_girl2.png", 1.3)

    #상호작용 버튼 이미지
    image find_idle_btn = im.FactorScale("gui/button/find_idle_ui.png", 0.6)
    image talk_idle_btn = im.FactorScale("gui/button/talk_idle_ui.png", 0.6)
    image find_hover_btn = im.FactorScale("gui/button/find_ui.png", 0.6)
    image talk_hover_btn = im.FactorScale("gui/button/talk_ui.png", 0.6)
    image return_btn = "gui/button/btn_return.png"
    image how_to_btn = im.FactorScale("gui/button/how_to.png", 0.15)
    image how_to_map = im.FactorScale("BG/how_too.png", 0.8)

    #증거품 이미지 *이름 변수명 다시 지어야함
    image item_hint1 : #메모
        im.FactorScale("Items/pngegg.png", 0.5)
        xpos 720
        ypos 245
    image item_hint2 : #거실 그림
        "Items/monariza.png" 
        xpos 720
        ypos 245
    image item_hint4 : #방1 그림
        im.FactorScale("Items/villa_picture1.png", 0.6) 
        xpos 720
        ypos 300
    image image_cookie : #인벤토리 테스트용
        im.FactorScale("Items/item_cookie.jpg", 1.0)
        yalign 0.5
        xalign 0.5
    image mini_post : #미니
        im.FactorScale("Items/mini_post.png", 1.5)
        yalign 0.5
        xalign 0.5

    #회사 증거 이미지
    image item_company_computer: #컴퓨터
        im.FactorScale("Items/company_computer.jpg", 1.0)
        yalign 0.5
        xalign 0.5
    image item_company_hotsix: #핫식스
        im.FactorScale("Items/company_hotsix.png", 1.0)
        yalign 0.5
        xalign 0.5
    image item_company_cctv: #cctv
        im.FactorScale("Items/company_cctv.jpg", 1.0)
        yalign 0.5
        xalign 0.5
    image item_company_knife: #커터칼
        im.FactorScale("Items/company_knife.png", 0.9)
        yalign 0.5
        xalign 0.5
    image item_company_nameteg: #사원증
        im.FactorScale("Items/company_nameteg.png", 1.2)
        yalign 0.5
        xalign 0.5
    image item_company_port: #커피포트
        im.FactorScale("Items/company_port.jpg", 0.9)
        yalign 0.5
        xalign 0.5
    image item_company_coffee: #캔커피
        im.FactorScale("Items/company_coffee.jpg", 0.4)
        yalign 0.4
        xalign 0.5
    image item_company_wire: #전선
        im.FactorScale("Items/company_wire.jpg", 1.0)
        yalign 0.5
        xalign 0.5
    image item_company_electricshocker: #전기충격기
        im.FactorScale("Items/company_electricshocker.jpg", 1.0)
        yalign 0.5
        xalign 0.5
    image item_company_stapler: #스테이플러
        im.FactorScale("Items/company_stapler.jpg", 1.0)
        yalign 0.5
        xalign 0.5
    image item_company_view: #회사경치
        im.FactorScale("Items/company_view.png", 1.0)
        yalign 0.5
        xalign 0.5
    image item_company_thirsty: #말라죽은화분
        im.FactorScale("Items/company_thirsty.jpg", 1.0)
        yalign 0.5
        xalign 0.5 

#병원 증거 이미지
    image image_cookie : #인벤토리 테스트용
        im.FactorScale("Items/item_cookie.jpg", 1.0)
        yalign 0.5
        xalign 0.5
    image item_hospital_drug: #독성물질
        im.FactorScale("Items/hospital_drug.png", 1.0)
        yalign 0.5
        xalign 0.5
    image item_hospital_knife: #메스
        im.FactorScale("Items/hospital_knife.png", 1.0)
        yalign 0.5
        xalign 0.5
    image item_hospital_sytinge: #주사기
        im.FactorScale("Items/hospital_syringe.png", 1.0)
        yalign 0.5
        xalign 0.5
    image item_hospital_bed: #침대
        im.FactorScale("Items/hospital_bed.jpg", 1.0)
        yalign 0.5
        xalign 0.5
    image item_hospital_broken: #깨진화분
        im.FactorScale("Items/hospital_broken.jpg", 1.0)
        yalign 0.5
        xalign 0.5
    image item_hospital_drink: #음료수병
        im.FactorScale("Items/hospital_drink.jpg", 1.6)
        yalign 0.5
        xalign 0.5
    image item_hospital_stethoscope: #청진기
        im.FactorScale("Items/hospital_stethoscope.jpg", 0.5)
        yalign 0.5
        xalign 0.5
    image item_hospital_syringe: #주사기
        im.FactorScale("Items/hospital_syringe.png", 1.0)
        yalign 0.5
        xalign 0.5
    image item_hospital_book1: #책들
        im.FactorScale("Items/hospital_book1.jpg", 0.2)
        yalign 0.5
        xalign 0.5
    image item_hospital_curtain: #커튼
        im.FactorScale("Items/hospital_curtain.jpg", 1.3)
        yalign 0.5
        xalign 0.5      
    image item_hospital_file: #파일들
        im.FactorScale("Items/hospital_file.jpg", 1.0)
        yalign 0.5
        xalign 0.5   
    image item_hospital_window: #마지막잎새
        im.FactorScale("Items/hospital_window.png", 1.3)
        yalign 0.5
        xalign 0.5
    image item_hospital_book2: #책
        im.FactorScale("Items/hospital_book2.jpg", 0.6)
        yalign 0.5
        xalign 0.5
    image item_hospital_pillow: #베개
        im.FactorScale("Items/hospital_pillow.png", 1.0)
        yalign 0.5
        xalign 0.5
    image item_hospital_pass: #출입증
        im.FactorScale("Items/hospital_pass.png", 1.0)
        yalign 0.5
        xalign 0.5
    image item_hospital_memo: #메모
        im.FactorScale("Items/hospital_memo.png", 1.6)
        yalign 0.5
        xalign 0.5
    image item_hospital_cutter: #커터칼
        im.FactorScale("Items/hospital_cutter.png", 0.8)
        yalign 0.5
        xalign 0.5    

    #별장 증거 이미지    
    image item_villa_gun: #총
        im.FactorScale("Items/villa_gun.png", 1.8)
        yalign 0.5
        xalign 0.5
    image item_villa_knife: #식칼
        im.FactorScale("Items/villa_knife.png", 1.0)
        yalign 0.5
        xalign 0.5
    image item_villa_rope: #밧줄
        im.FactorScale("Items/villa_rope.png", 1.8)
        yalign 0.5
        xalign 0.5
    image item_villa_saw: #톱
        im.FactorScale("Items/villa_saw.png", 1.2)
        yalign 0.5
        xalign 0.5
    image item_villa_glass : #유리컵
        im.FactorScale("Items/villa_glass.jpg", 0.4) 
        xpos 720
        ypos 300
    
    image item_villa_syringe : #주사기
        im.FactorScale("Items/villa_syringe.png", 1.3) 
        yalign 0.5
        xalign 0.5

    image item_villa_coffee: #커피
        im.FactorScale("Items/villa_coffee.jpg", 1.0)
        yalign 0.5
        xalign 0.5
    image item_villa_sight: #경치
        im.FactorScale("Items/villa_sight.jpg", 1.0)
        yalign 0.5
        xalign 0.5
    image item_villa_deco: #장식물
        im.FactorScale("Items/villa_deco.jpg", 0.2)
        yalign 0.5
        xalign 0.5
    image item_villa_monitor: #모니터
        im.FactorScale("Items/villa_monitor.jpg", 1.3)
        yalign 0.5
        xalign 0.5
    image item_villa_pillow: #베개
        im.FactorScale("Items/villa_pillow.png", 1.0)
        yalign 0.5
        xalign 0.5
    image item_villa_memo: #메모
        im.FactorScale("Items/villa_memo.png", 0.4)
        yalign 0.5
        xalign 0.5
    image item_villa_picture2: #그림2
        im.FactorScale("Items/villa_picture2.png", 1.0)
        yalign 0.35
        xalign 0.5
    image villa_mirror : #거울
        im.FactorScale("Items/villa_mirror.png", 0.2)
        yalign 0.2
        xalign 0.5

    ########################
