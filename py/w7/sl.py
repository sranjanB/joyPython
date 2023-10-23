from PIL import Image
from random import randint
import os
os.environ['TERM'] = 'xterm-256color'
end = 100

def show_board():
    img = Image.open('slb.jpg')
    img.show()

def check_ladder(points):
    if points == 4:
        print('Ladder 4-->22')
        return 22
    elif points == 10:
        print('Ladder 10-->29')
        return 29
    elif points == 14:
        print('Ladder 14-->77')
        return 77
    elif points == 33:
        print('Ladder 33-->51')
        return 51
    elif points == 74:
        print('Ladder 74-->90')
        return 90
    elif points == 64:
        print('Ladder 64-->82')
        return 82
    else:
        return points

def check_snake(points):
    if points == 50:
        print('Snake 16<--50')
        return 16
    elif points == 40:
        print('Snake 20<--40')
        return 20
    elif points == 95:
        print('Snake 36<--95')
        return 36
    elif points == 92:
        print('Snake  52<--92')
        return 52
    elif points == 81:
        print('Snake 78<--81')
        return 78
    else:
        return points
def play():
    print("Welcome to sneak and Ladder")
    #input of players
    p1_name = input('Player 1 , Please Enter your name: ')
    p2_name = input('Player 2 , Please Enter your name: ')
    #Initial points of players
    pp1 = 0
    pp2 = 0
    #Turn count
    turns = 0
    #Game Start
    while(1):
        os.system('clear')
        print("*"*20)
        print(p1_name," : ", pp1)
        print(p2_name, " : ", pp2)
        print("*" * 20)
        if turns%2 == 0:
            #Player_1_turns
            print(p1_name, 'your turn')
            #Ask_approval
            c = input('Press 1 to conitnue, 0 to quit: ')
            if c ==0:
                print(p1_name, ' scored ', pp1)
                print(p2_name, ' scored ', pp2)
                break
            dice = randint(1, 6)
            print("Dice Showed: ", dice)
            pp1 += dice
            pp1 = check_ladder(pp1)
            pp1 = check_snake(pp1)
            #print(p1_name, ' Your score:  ', pp1)
            if pp1 > end:
                pp1 = end
                print(p1_name, ' won')
                break
            turns += 1
        else:
            print(" ")
            # Player 2 turns
            print(p2_name, 'your turn')
            # Ask approval
            c = input('Press 1 to conitnue, 0 to quit: ')
            if c == 0:
                print(p1_name, ' scored ', pp1)
                print(p2_name, ' scored ', pp2)
                break
            dice = randint(1, 6)
            print("Dice Showed: ", dice)
            pp2 += dice
            pp2 = check_ladder(pp2)
            pp2 = check_snake(pp2)
            #print(p2_name, ' Your score:  ', pp2)
            if pp2 > end:
                print(p2_name, ' won')
                break
            turns += 1


show_board()
play()