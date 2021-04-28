board = {
  '7': ' ',
  '8': ' ',
  '9': ' ',
  '4': ' ',
  '5': ' ',
  '6': ' ',
  '1': ' ',
  '2': ' ',
  '3': ' '
}

board_keys = []

for key in board:
    board_keys.append(key)

def print_board(board):
    print('{0}|{1}|{2}'.format(board['7'], board['8'], board['9']))
    print('-+-+-')
    print('{0}|{1}|{2}'.format(board['4'], board['5'], board['6']))
    print('-+-+-')
    print('{0}|{1}|{2}'.format(board['1'], board['2'], board['3']))
    
def check_for_win(square_one, square_two, square_three):
    if board[square_one] == board[square_two] == board[square_three]:
        return True
    else:
        return False

def print_winning_message(winner):
    print_board(board)
    print('Game over, {0} won'.format(winner))

def play_game():
    print('Welcome to Tic Tac Toe! The board matches the number pad on your keyboard.')

    turn = 'X'
    move_count = 0

  # loop through the range(10) for nine possible moves
    
    for i in range(10):
        print_board(board)
        move = input('It\'s {0}\'s turn. What space do you pick? '.format(turn))

    #move = input()

        if board[move] == ' ':
            #place the character on the board
            board[move] = turn
            #increment our count of turns
            move_count = move_count + 1

        else:
            print('That space is taken. Pick a different space')
            continue
    
    # Check if there is a winning row
        if move_count >= 5:
            if check_for_win('7', '8', '9'):
                print_winning_message(turn)
                break
            elif check_for_win('4', '5', '6'):
                print_winning_message(turn)
                break
            elif check_for_win('1', '2', '3'):
                print_winning_message(turn)
                break
            elif check_for_win('7', '4', '1'):
                print_winning_message(turn)
                break
            elif check_for_win('8', '5', '2'):
                print_winning_message(turn)
                break
            elif check_for_win('9', '6', '3'):
                print_winning_message(turn)
                break
            elif check_for_win('7', '5', '3'):
                print_winning_message(turn)
                break
            elif check_for_win('1', '5', '9'):
                print_winning_message(turn)
                break
  
        if move_count == 9:
            print('Game over, tie game')

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    
    play_again = input('Would you like to play again? Y/N: ')

    if play_again.upper() == 'Y':
        for key in board_keys:
            board[key] = ' '
        play_game()  
          
    else:
        print('thanks for playing')

play_game()

