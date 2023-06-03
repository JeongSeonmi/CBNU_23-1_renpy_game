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

##inventory
label inventory:
    hide screen quick_menu
    hide screen villa_map
    hide screen comp_map
    hide screen hosp_map
    #visit_장소 = 0 을하면 인벤토리 들어가면 메뉴가 사라져버림

    scene bg_lab
    call screen inventory(inv) with Dissolve(.2)
    jump back    