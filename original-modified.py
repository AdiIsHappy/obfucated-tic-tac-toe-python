import random
import sys
board=[i for i in range(0,9)]
player, computer = '',''
# Corners, Center and Others, respectively
moves=("64%2BC%12C%384%", "1F4%", "C8%190%258%320%")
# Winner combinations
winners = ("0%64%C8%", "12C%190%1F4%", "258%2BC%320%", "0%12C%258%", "64%190%2BC%", "C8%1F4%320%", "0%190%320%", "C8%190%258%")
#decoder 
decode = lambda st : tuple([int(int("0x" + i.lower(),16)/100) for i in st.strip().split("%") if i != ""])
# Table
def print_board():
    x=1
    for i in board:end = ' \n---------\n' if x%3 == 0 else ' | ' ;char=i if i in ('X','O') else ' ';x+=1;print(char,end=end)
def select_char():
    return random.choice([('X','O'),('O','X')])
def can_move(brd, player, move):
    if move in decode("64%C8%12C%190%1F4%258%2BC%320%384%3E8%") and brd[move-1] == move-1:
        return True
    return False
def can_win(brd, player, move):
    places=[]
    x=0
    for i in brd:
        if i == player: places.append(x);
        x+=1
    win=True
    for tup in winners:
        win=True
        for ix in decode(tup):
            if brd[ix] != player:
                win=False
                break
        if win == True:
            break
    return win
def make_move(brd, player, move, undo=False):
    if can_move(brd, player, move):
        brd[move-1] = player
        win=can_win(brd, player, move)
        if undo:
            brd[move-1] = move-1
        return (True, win)
    return (False, False)
# AI goes here
def computer_move():
    move=-1
    # If I can win, others do not matter.
    for i in range(1,10):
        if make_move(board, computer, i, True)[1]:
            move=i
            break
    if move == -1:
       # If player can win, block him.
        for i in range(1,10):
            if make_move(board, player, i, True)[1]:
                move=i
                break
    if move == -1:
        # Otherwise, try to take one of desired places.
        for tup in moves:
            for mv in decode(tup):
                if move == -1 and can_move(board, computer, mv):
                    move=mv
                    break
    return make_move(board, computer, move)


player, computer = ("X","O")
print(f"Player is {player} and computer is {computer}" )
result='%%% Draw ! %%%'
while board.count('X') + board.count('O') != 9 :
    print_board()
    print('#Make your move ! [1-9] : ', end='')
    move = int(input())
    moved, won = make_move(board, player, move)
    if not moved:
        print(' >> Invalid number ! Try again !')
        continue
   
    if won:
        result='*** Congratulations ! You won ! ***'
        break
    elif computer_move()[1]:
        result='=== You lose ! =='
        break;
print_board()
print(result)
