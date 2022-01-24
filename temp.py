board=[i for i in range(0,9)]
player, computer = '',''
# Corners, Center and Others, respectively
moves=((1,7,3,9),(5,),(2,4,6,8))
# Winner combinations
winners=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
# Table
tab=range(1,10)
def print_board():
    x=1
    for i in board:
        end = ' | '
        if x%3 == 0:
            end = ' \n'
            end+='---------\n';
        char=' '
        if i in ('X','O'): char=i;
        x+=1
        print(char,end=end)
print_board()