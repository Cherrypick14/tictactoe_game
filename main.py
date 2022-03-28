board =['-','-','-','-','-','-','-','-','-']

def display():
    print('|'+ board[0] + '|'+ board[1] + '|' + board[2])
    print('|'+ board[3] + '|'+ board[4] + '|' + board[5])
    print('|'+ board[6] + '|'+ board[7] + '|' + board[8])

#check for winner
def check_winner(board):
    player1 ='X'
    player2 = 'O'

    #Horizontal track
    if board[0]==board[1]==board[2] ==player1 or board[0]==board[1]==board[2] ==player2:
        return True
    elif board[3]==board[4]==board[5]==player1 or board[3]==board[4]==board[5]==player2:
        return True
    elif board[6]==board[7]==board[8]==player1 or  board[6]==board[7]==board[8]==player2:
        return True
    #Vertical track
    elif board[0]==board[3]==board[6]==player1 or board[0]==board[3]==board[6]==player2:
        return True
    elif board[1]==board[4]==board[7]==player1 or board[1]==board[4]==board[7]==player2:
        return True
    elif board[2]==board[5]==board[8]==player1 or  board[2]==board[5]==board[8]==player2:
        return True
    #diagonal track
    elif board[0]==board[4]==board[8]==player1 or board[0]==board[4]==board[8]==player2:
        return True
    elif board[2]==board[4]==board[6]==player1 or board[2]==board[4]==board[6]==player2:
        return True
    else:
        return False
#use recursions
def ent(board):
    x = int(input("Enter a position"))
    if board[x-1]!= '-':
        print("value already exists, enter a new value")
        return ent(board)
    else:
        return x
#getting inputs from the players
p1 = input("Player Name 1: ")
p2 = input("Player Name 2: ")
display()  
for i in range(9):
    if i%2==0:
        x =ent(board)
      #  print(type(x))
        board[x-1] = 'X'
        display()
        if check_winner(board):
            print("Player 1 wins")
            break
    else:
        board[x-1] = 'O'
        display()
        if check_winner(board):
            print("Player 2 wins")
            break
print("Game Over")


