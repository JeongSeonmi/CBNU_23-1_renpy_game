##########################################

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

    $ visit_company = 0
    $ visit_hospital = 0
    $ visit_villa = 0
    scene bg_lab
    call screen inventory(inv) with Dissolve(.2)
    return

