import sys
import random

# the variables W, T, L shows wins , ties and losses

w = 0
t = 0
l = 0

#game entry loop with scoreboard
while true:
    print('%s wins  %s  losses  %s ties',w,t,l)

    #player input taking loop
    while true:
        choice = input()

        if choice == 'q':
            sys.exit()

        elif choice =='r' or choice =='p' or choice =='s':
            break
    print('Enter (p)paper  (r)rock  (s)scissor')

    if choice == 'r':
        print('Rock versus')

    elif choice =='p':
        print
    num = random.randint(1,3)

    if num ==1:
        com_choice = 