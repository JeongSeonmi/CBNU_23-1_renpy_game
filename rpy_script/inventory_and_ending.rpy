## endings
label good_ending :
    #(killer_name == '의뢰인') and (see_point > 4)#
    DT "범인은 의뢰인이야!"with vpunch
    stop music fadeout 2
    scene bg_room with fade
    DT "이번에도 무사히 사건을 해결했군"
    return

label bad_ending1 :
    #(killer_name == '의뢰인') and (see_point < 5)#
    DT "어째서 범인 그 사람일까?"
    DT "다시 한번 살펴보자..."
    jump myP

label bad_ending2 :
    #(!(killer_name == '의뢰인'))#
    DT "범인이 아닌것 같은데?"
    DT "다시 한번 살펴보자..."
    jump myP

label error :
    if myP == "villa" :
        if myR == "room1" :
            scene bg_villa_room1
            DT idle "더 이상 기회는 없어."
            jump villa_room1
        elif myR == "room2" :
            scene bg_villa_room2
            DT idle "더 이상 기회는 없어."
            jump villa_room2
        elif myR == "living" :
            scene bg_villa_living
            DT idle "더 이상 기회는 없어."
            jump villa_living

    elif myP == "hospital" :
        if myR == "office1" :
            scene bg_HP_office1
            DT idle "더 이상 기회는 없어."
            jump hospital_office1
        elif myR == "office2" :
            scene bg_HP_office2
            DT idle "더 이상 기회는 없어."
            jump hospital_office2
        elif myR == "room" :
            scene bg_HP_room
            DT idle "더 이상 기회는 없어."
            jump hospital_room
            
    elif myP == "company" :
        if myR == "office1" :
            scene bg_CP_office1
            DT idle "더 이상 기회는 없어."
            jump company_office1
        elif myR == "office2" :
            scene bg_CP_office2
            DT idle "더 이상 기회는 없어."
            jump company_office2
        elif myR == "room" :
            scene bg_CP_room
            DT idle "더 이상 기회는 없어."
            jump company_room


##inventory
label inventory:
    hide screen villa_map
    hide screen company_map
    hide screen hospital_map
    hide screen text_timer
    #visit_장소 = 0 을하면 인벤토리 들어가면 메뉴가 사라져버림

    scene bg_lab
    call screen inventory(inv) with Dissolve(.2)
    return
