admin_login = [
         ['damien','admin'],
         ['jonas','password'],
         ['kola','administrator']
]

teacher_login = [
            ['marion','fense'],
            ['nadia','bloc']
]

parent_login = [
            ['casco','ami'],
            ['voiture','audrey']
]




def login():
    username = input('enter your username : ')
    password = input('enter your password: ')
    for row in admin_login:
        if username == row[0] and password == row[1]:
            print(f'welcome {username} here are your options : ')
            return
        
    for row in teacher_login:
        if username == row[0] and password == row[1]:
            print(f'welcome {username} you are a teacher here are your options')
            return
        
    for row in parent_login:
        if username == row[0] and password == row[1]:
            print(f'welcome {username} you are parent here is your only options ')
            return
    
    print('wronf username or password please contact the deveollpement team')
login()

    

