label talk_suspecter1:
    nvl clear
    "\n\n 이곳에서는 용의자에게 질문을 할 수 있습니다"
    "\n'뒤로가기'를 입력하면 돌아갈 수 있습니다"
    nvl clear
    while True:

        $ user_input = ""  
        $ user_input= renpy.input('무엇이 궁금한가요?')

        $ if user_input == "뒤로가기" : renpy.jump(myP)
        
        $ npc_output = suspect_1.dialog(user_input)

        ch_CP_woman "[npc_output]"

label talk_suspecter2:
    nvl clear
    "\n\n 이곳에서는 용의자에게 질문을 할 수 있습니다"
    "\n'뒤로가기'를 입력하면 돌아갈 수 있습니다"
    nvl clear
    while True:

        $ user_input = ""  
        $ user_input= renpy.input('무엇이 궁금한가요?')

        $ if user_input == "뒤로가기" : renpy.jump(myP)
        
        $ npc_output = suspect_2.dialog(user_input)

        ch_CP_man1 "[npc_output]"

label talk_suspecter3:
    nvl clear
    "\n\n 이곳에서는 용의자에게 질문을 할 수 있습니다"
    "\n'뒤로가기'를 입력하면 돌아갈 수 있습니다"
    nvl clear
    while True:

        $ user_input = ""  
        $ user_input= renpy.input('무엇이 궁금한가요?')

        $ if user_input == "뒤로가기" : renpy.jump(myP)
        
        $ npc_output = suspect_3.dialog(user_input)

        ch_CP_man2 "[npc_output]"
