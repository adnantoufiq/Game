from random import  randint

board = []

for i in range(0, 5):
    board.append(['O']*5)


# this define a function for board
def print_board(board):
    for row in board:
        print(' '.join(row))

print('Lets Play A battleship')
print_board(board)


def random_row(board):
    return randint(0,len(board)-1)

def random_col(board):
    return randint(0,len(board)-1)

ship_row = random_row(board)
ship_col = random_col(board)


turn =0

# for the input again and again
for turn in range (4):
   guess_row = int(input("Guess Row: "))

   guess_col = int(input("Guess Col: "))
# win condition
   if (guess_row==ship_row and guess_col==ship_col):
    print("Congratulations! You shank my battleship!")
    break

#  give input anything for out of the range
   else:
     if (guess_col< 0 or guess_row >4) or (guess_col<0 or guess_col>4):
        print('Opps that not even in the ocean')


# if given input give that again
     elif  (board[guess_row][guess_col] == 'X'):
               print('You guessed that in already.')


     else:
         print("You miss my battleship")
         board[guess_row][guess_col] = 'X'
    # if board go for lop equal than give that print
         if turn==3:
             print('Game Over')
     print_board(board)
   print(turn+1)

