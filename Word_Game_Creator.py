from random import *
overall = []
written_file = open('Output.py','w+')
print('\nHi, welcome to the Word Game Creator!\nI\'m the developer of this program, KHB.\nThis program makes it easier for you to create your own\nword game by makeing each scene a class.\nString formatting & exec() is also involved\nThis engine works by creating scenes and link them to form a game')
while True:
    print('''\nPlease set up death scene / game_over scene\nWhat do you want to name your death scene?\n''')
    death_name = input('Death Scene name>> ')
    print('''\nWhat death message do you want to show? This will display randomly at death scene\nType in message, press enter to move to next message, \'continue\' to continue\n''')
    death_message = []
    while True:
        temp = input('Death message>> ')
        if temp == 'continue':
            break
        else:
            death_message.append(temp)
    death_message = '\n'.join(death_message)
    print(f'''\nYour name for death scene is "{death_name}"\nYour randomly displayed messages are:\n\n{death_message}''')
    while True:
        correct = input('\nCorrect? (yes or no) >>')
        if correct == 'yes' or correct == 'Yes':
            break
        elif correct == 'no' or correct == 'No':
            break
        else:
            print('Unknown Input, try again')
    if correct == 'yes' or correct == 'Yes':
        break
death_model = f'class {death_name}(object):\n    def enter(self):\n        print(choice(death_message))\n        input()\n        exit(0)'
overall.append(death_model)
exec(death_model)
while True:
    print('\nSetting up the win scene.....\nWhat is the message you want to show after winning?\n')
    messagetwo = input('Message>> ')
    print('\nWhat do you want to name your winning scene?\n')
    win_name = input('Name>> ')
    mode = f'''class {win_name}(object):\n    def enter(self):\n        print('{messagetwo}')\n        input('Press enter to quit')\n        exit(0)'''
    overall.append(mode)
    exec(mode)
    print('\nDo you want to set another winning scene?\n')
    choiice = input('Yes/No>> ')
    if choiice == 'Yes' or choiice == 'yes' or choiice == 'y' or choiice == 'Y':
        pass
    else:
        break
print('--------------------------------------------------------------------------------\nDeath scene & winning scene created successfully, start creating other scenes\n')
while True:
    while True:
        print('What is the name of the scene?(Enter \'continue\' to continue)\n')
        scene_name = input('>> ')
        if scene_name == 'continue' or scene_name == 'Continue':
            break
        print('\nWhat is the message you want to show players when entering the scene?\nPress enter to change lines, type in \'continue\' to continue\n')
        message = ''
        while True:
            temp = input('> ')
            if temp == 'continue':
                break
            else:
                message += temp
                message += '\n'
        print(f'Your message is:\n\n{message}\n\n\nYour scene name is:\n\n{scene_name}\n\nCorrect?')
        yes_no = input('yes/no>> ')
        if yes_no == 'yes' or yes_no == 'y' or yes_no == 'Yes' or yes_no == 'Y':
            break
    if scene_name == 'continue' or scene_name == 'Continue':
        break
    inputt = []
    while True:
        print('\nWhat are the choices and the scene they led to?(\'Continue\') to continue\n')
        temp = input('Choice>> ')
        if temp != 'Continue' and temp != 'continue':
            choice1 = temp
            messages = ''
            print("\nWhat message is going to display?(\'Continue\' to continue)")
            while True:
                temp = input('\nMessage >>')
                if temp == 'continue' or temp == "Continue":
                    break
                else:
                    messages += temp
                    messages += '\n'
            print('\nWhich scene is this choice leading to\n?')
            lead_scene = input('Scene?>> ')
        else:
            break
        messages = messages.split('\n')
        input_temp = f'''\n        if choice_made == '{temp}':\n            print({messages})\n            return '{lead_scene}\''''
        inputt.append(input_temp)
    inputt.append(f'''\n        else:\n            print('Invalid option\n')\n            return '{scene_name}\'''')
    model = f'''class {scene_name}(object):\n    def enter(self):\n        for a in {messages}:\n            print(a)\n        choice_made = input('What do you do?>> ')'''
    for temp1 in inputt:
        model += temp1
    overall.append(model)
    exec(model)
while True:
    start_scene = input('\nWhich scene do you want to start at?')
    try:
        exec(f'testt = {start_scene}()')
        break
    except:
        print('Invalid scene name')
engine = f'''class E_n_GiN_e(object):\n    def __init__(self):\n        self.start_scene = {start_scene}()\n    def play(self):\n        self.current_scene = self.start_scene\n        while True:\n            while True:\n                try:\n                    next_scene = self.current_scene.enter()'''
engine_part = '''                    exec(f\'self.current_scene = {next_scene}()\')\n                except:\n                    print('Not an valid option, please try something else')'''
overall.append(engine)
overall.append(engine_part)
execute = '''\nEngine_OBJ = E_n_GiN_e()\nEngine_OBJ.play()\n'''
overall.append(execute)
text_written = '\n'.join(overall)
written_file.write(text_written)
print('\n\n\nYour game has been successfully created! See Output.py in the folder')
