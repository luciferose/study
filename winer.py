import random

choice=['rock','paper','scissors']

while True:
    com_ch = random.choice(choice)
    hum_ch = input('please input choice rock paper scissors: ')
    hum_ch=hum_ch.lower()
    win = ''
    quit=['q','Q']
    if hum_ch in quit:
        break
    if hum_ch not in choice:
        continue
    if com_ch == hum_ch:
        print('a draw')
        print('com', com_ch, '\n', 'user', hum_ch)
        continue
    elif com_ch=='paper' and hum_ch=='rock':
        win='com'
    elif com_ch=='rock' and hum_ch=='scissors':
        win='com'
    elif com_ch=='scissors'and hum_ch=='paper':
        win='com'
    else:
        win='user'
    print('the',win,'wins!')
    print('com:',com_ch)
    print('user:',hum_ch)