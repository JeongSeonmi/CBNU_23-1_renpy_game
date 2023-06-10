init:
    image law = "BG/law.png"
    define ch_Judge = Character('판사', image="cr_Judge")
    image cr_Judge = im.FactorScale("CR/judge.png", 0.9)
    image side cr_Judge idle = "/CR/judge.png"
    image side cr_police idle = "/CR/police_idle.png"

##############################
label ending_calculate :
    
    #범행도구 gpt한테 변수로 받아와서 검사(임시로 item_post가 정답으로 해놓음)#
    if (killer_item.id == "item_painting"):
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
    play music "audio/music/music_start.mp3" fadein 1
    
    image ending1 = "ED/ending_1.png"
    image ending2 = "ED/ending_2.png"
    image ending3 = "ED/ending_3.png"
    image ending4 = "ED/ending_4.png"
    image ending5 = "ED/ending_5.png"
    image ending6 = "ED/ending_6.png"
    image ending7 = "ED/ending_7.png"
    image ending8 = "ED/ending_8.png"
    image ending9 = "ED/ending_9.png"

    scene ending1 with fade
    $ renpy.pause(3, hard=True)
    scene ending2 with dissolve
    $ renpy.pause(3, hard=True)
    scene ending3 with dissolve
    $ renpy.pause(3, hard=True)
    scene ending4 with dissolve
    $ renpy.pause(3, hard=True)
    scene ending5 with dissolve
    $ renpy.pause(3, hard=True)
    scene ending6 with dissolve
    $ renpy.pause(3, hard=True)
    scene ending7 with dissolve
    $ renpy.pause(3, hard=True)
    scene ending8 with dissolve
    $ renpy.pause(3, hard=True)
    scene ending9 with dissolve
    $ renpy.pause(5, hard=True)
    
    stop music


    return

###################################
## endings
label good_ending :
    #범인과 도구 맞음#
    stop music
    play music "audio/music/law.mp3" fadein 2 #음악 재생#
    scene law
    ch_Judge idle "피고인 ...에게 무가징역을 선고한다"
    
    ##땅땅땅 소리
    ##판결문 이미지
    DT idle "이번 사건도 잘 해결했군."
    stop music fadeout 2

    jump ending_credit

label bad_ending1 :
    #범인만 맞음#
    stop music
    play music "audio/music/law.mp3" fadein 2 #음악 재생#
    scene law
    ch_Judge idle "피고인 ...은 증거불충분으로 무죄를 선고한다"
    
    ##땅땅땅 소리
    ##판결문 이미지
    DT idle "범인은 저 사람이 맞는데.."
    DT idle "범행 도구가 틀린건가..?."
    stop music fadeout 2

    jump ending_credit

label bad_ending2 :
    #도구만 맞음#
    stop music
    play music "audio/music/law.mp3" fadein 2 #음악 재생#
    scene law
    ch_Judge idle "피고인 ...은 범행과 무관한 것으로 판단되므로"
    ch_Judge idle "무죄를 선고한다"
    
    ##땅땅땅 소리
    ##판결문 이미지
    DT idle "범행 도구는 맞은데.."
    DT idle "범인이 틀린건가..?."
    jump ending_credit

label bad_ending3 :
    #둘다 틀림#
    stop music
    play music "audio/music/law.mp3" fadein 2 #음악 재생#
    scene law
    ch_Judge idle "피고인 ...은 범행과 무관한 것으로 판단되므로"
    ch_Judge idle "무죄를 선고한다"
    
    ##땅땅땅 소리
    ##판결문 이미지
    ch_police idle "범인과 범행 도구 모두 틀렸더군.."
    ch_police idle "실망이 크네.."
    DT idle "..."
    jump ending_credit

################################

