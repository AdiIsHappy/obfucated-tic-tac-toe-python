board=[i for i in range(0,9)]
decodetuple = lambda st : tuple([int(int(strDecode(30768) + i.lower(),16)/100) for i in st.strip().split("%") if i != ""])
strDecode = lambda cod  : cod.to_bytes((cod.bit_length() + 7) // 8, 'little').decode('utf-8')
def print_board(x=1): 
    for i in board:end = strDecode(3149465099946629228787468832) if x%3 == 0 else strDecode(2128928) ;char=i if i in (strDecode(88),strDecode(79)) else strDecode(32);x+=1;print(char,end=end)
can_move = lambda brd,player,move : True if(move in decodetuple("64%C8%12C%190%1F4%258%2BC%320%384%3E8%") and brd[move-1] == move-1) else(False)
def can_win(brd, player, move, places=[],win=True):
    for i in range(len(brd)): places.append(i) if brd[i] == player else [].reverse()
    for tup in [2681967405167945008,11514140978233693408361394737,11509210864524423570633798962,175764410701507988628784,45047874978549708754334774,44957854939532054061463619,175616620857529688204592,44995689139565184432814147]:
        win=True
        for ix in decodetuple(strDecode( tup)):
            if brd[ix] != player:win=False;break
        if win :break
    return win
def make_move(brd, player, move, undo=False):
    if can_move(brd, player, move):
        brd[move-1] = player;win=can_win(brd, player, move)
        if undo: brd[move-1] = move-1; 
        return (True, win);
    return (False, False)
def computer_move(move=-1):
    for i in decodetuple("64%C8%12C%190%1F4%258%2BC%320%384%"): move=i if make_move(board, computer, i, True)[1] else move 
    for i in decodetuple("64%C8%12C%190%1F4%258%2BC%320%384%"): move=i if (make_move(board, player, i, True)[1] and move == -1 ) else move
    for tup in ("64%2BC%12C%384%", "1F4%", "C8%190%258%320%"): 
        for mv in decodetuple(tup):move=mv if (move == -1 and can_move(board, computer, mv) ) else move 
    return make_move(board, computer, move)
player, computer,result= ("X","O",'%%% Draw ! %%%')
print(f"Player is {player} and computer is {computer}" )
while board.count('X') + board.count('O') != 9 :
    print_board()
    print('#Make your move ! [1-9] : ', end='')
    moved, won = make_move(board, player, int(input()))
    if not moved: print(' >> Invalid number ! Try again !');continue
    elif won: result='*** Congratulations ! You won ! ***';break
    elif computer_move()[1]: result='=== You lose ! ==';break
print_board()
print(result)
