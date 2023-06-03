style text_timer_ok:
    size 72
    color "#FFF"
    outlines [(2, "#000", 0, 0)]

style text_timer_near:
    size 72
    color "#F22"
    outlines [(2, "#000", 0, 0)]

init python:

    def text_countdown( st, at, 
                        duration = 10.0,  
                        #screen = 'text_timer',
                        ok_style = 'text_timer_ok',
                        near_style = 'text_timer_near',
                        style_swap = 5.0,
                        text_format = "{minutes:02d}:{seconds:02d}" ):

        remaining = duration - st

        parts_dict = {
            'minutes' : int( remaining // 60 ),
            'seconds' : int( remaining % 60 ),
            #'micro_seconds' : str(int( (remaining % 1) * 10000 )), # we use str() so we can define precision
        }

        if remaining <= 0.0 :
            renpy.hide_screen(screen)
            renpy.jump("[myP]")
        
        #return Text( text_format.format(**parts_dict), 
        #            style = ok_style if remaining > style_swap else near_style), .1

    
#screen text_timer( **kwargs ): #kwargs 는 아마 시간 설정하는 변수인듯
#    vbox:
#        add DynamicDisplayable(text_countdown, **kwargs)
#        xalign 0.99
        # 타이머 끝나면 나가게 해야됨 #
#        textbutton "Found Me":
#           action [ Function(renpy.hide_screen, 'text_timer'), Call(kwargs.get('success_label', 'success_label')) ]


## test label#
#label staart:
#    "start"
#    call screen text_timer
#    "middle"
#    # with parameters (no micro_seconds, 22 seconds long)
#    call screen text_timer(duration=22.0, text_format = "{minutes:02d}:{seconds:02d}" )
#    "end"

#label success_label:
#    "Success"
#    return

#label fail_label:
#    "Too slow"
#    return