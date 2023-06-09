
##############################
label ending_calculate :
    
    #범행도구 gpt한테 변수로 받아와서 검사(임시로 item_post가 정답으로 해놓음)#
    if (painting == killer_item.id):
        $ ending_point += 50
    else :
        $ ending_point += 20

    scene bg_DT_office with fade
    show cr_Detective at left   
    DT "범행 도구는 [killer_item.name]일 거야"
    show cr_police at right
    ch_police "그럼 자네를 믿고 [killer_name]을 체포하겠네."
    
    if(ending_point==150):
        jump good_ending
    elif(ending_point==120):
        jump bad_ending1
    elif(ending_point==60):
        jump bad_ending2
    else:
        jump bad_ending3                

#################################
label ending_credit:
    "엔딩 크레딧 작성 부분"
    scene loading with fade
    $ renpy.pause(1.0, hard=True)

    return

###################################
## endings
label good_ending :
    #범인과 도구 맞음#
    scene bg_DT_office
    show cr_Detective at left
    show cr_police at right
    DT "범인은 의뢰인이야!"with vpunch
    stop music fadeout 2
    DT "이번에도 무사히 사건을 해결했군"
    jump ending_credit

label bad_ending1 :
    #범인만 맞음#
    scene bg_DT_office
    show cr_Detective at left
    show cr_police at right
    DT "어째서 범인 그 사람일까?"
    DT "다시 한번 살펴보자..."
    jump ending_credit

label bad_ending2 :
    #도구만 맞음#
    scene bg_DT_office
    show cr_Detective at left
    show cr_police at right
    DT "범인이 아닌것 같은데?"
    ch_police "범행도구는 맞는 것 같아"
    jump ending_credit

label bad_ending3 :
    #둘다 틀림#
    scene bg_DT_office
    show cr_Detective at left
    show cr_police at right
    DT "이게 맞나?"
    ch_police "자네는 재능이 없군"
    jump ending_credit
