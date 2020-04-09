# Naughts and Crosses


def player_names():
    global player1
    global player2
    global player1_score
    global player2_score
    player1_score = 0
    player2_score = 0
    print("Welcome to this game of Naughts and Crosses")
    player1 = str(input("Please enter your name player one "))
    player1 = player1.upper()[0] + player1.lower()[1:]
    print("Welcome to the game {}!".format(player1))
    player2 = str(input("Please enter your name player two "))
    player2 = player2.upper()[0] + player2.lower()[1:]
    print("Welcome to the game {}!".format(player2))
    first_time = str(
        input("{0} and {1} have you both played Naughts and Crosses before? (Y/N) (Please enter N if this is the "
              "first time you are running this program): ".format(player1, player2)))
    if first_time.upper()[0] == "N":
        first_time_playing_naughts_and_crosses()


def start_game():
    global play_game
    start_the_game = str(
        input("{0} and {1} are you ready to play Naughts and Crosses? (Y/N): ".format(player1, player2)))
    if start_the_game.lower()[0] == "y":
        play_game = True
    else:
        are_you_sure = str(input("Are you sure you want to exit the game? (Y/N): "))
        if are_you_sure.lower()[0] == "y":
            exit()
        else:
            play_game = True
            print("Ok, then lets start the game!")


def create_blank_game_board():
    global game_board
    game_board = [" "] * 10


def print_game_board(board):
    print("   |   |  ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |  ")
    print("-----------")
    print("   |   |  ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |  ")
    print("-----------")
    print("   |   |  ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |  ")


def first_time_playing_naughts_and_crosses():
    print("   |   |  ")
    print(" " + "7" + " | " + "8" + " | " + "9")
    print("   |   |  ")
    print("-----------")
    print("   |   |  ")
    print(" " + "4" + " | " + "5" + " | " + "6")
    print("   |   |  ")
    print("-----------")
    print("   |   |  ")
    print(" " + "1" + " | " + "2" + " | " + "3")
    print("   |   |  ")
    print("Shown above is the grid you will be playing on. Each valid position is numbered 1 to 9, when it is your "
          "turn you will be asked to enter a number which corresponds to a position on the grid as shown.")
    print("The aim of Naughts and Crosses is to place 3 of your markers (X or O) in a horizontal, vertical or "
          "diagonal line before the other player can do the same.")
    print("The player who achieves this will win the game, if no player is able to achieve this, the game will be "
          "declared a tie!")


def player_markers():
    marker = ""
    while not (marker == "X") or (marker == "O"):
        marker = input("{} Would you like your marker to be X or O? ".format(player1)).upper()
        if marker == "X":
            print("Ok {0} will be X and {1} will be O".format(player1, player2))
            return "X", "O"
        elif marker == "O":
            print("Ok {0} will be O and {1} will be X".format(player1, player2))
            return "O", "X"
        else:
            print("That was an invalid input! {0} will be X and {1} will be O".format(player1, player2))
            return "X", "O"


def place_marker(board, marker, position):
    global move_was_invalid
    if is_space_free(board, position):
        board[position] = marker
        move_was_invalid = False

    elif player1_marker == "X" and board[position] == "X" and turn == ("{}".format(player1)):
        print("{} you have already placed a marker there! Please try again!".format(player1))
        move_was_invalid = True
    elif player1_marker == "O" and board[position] == "O" and turn == ("{}".format(player1)):
        print("{} you have already placed a marker there! Please try again!".format(player1))
        move_was_invalid = True
    elif player1_marker == "X" and board[position] == "X" and turn == ("{}".format(player2)):
        print("{1}, {0} has already placed a marker there! Please try again!".format(player1, player2))
        move_was_invalid = True
    elif player1_marker == "O" and board[position] == "O" and turn == ("{}".format(player2)):
        print("{1}, {0} has already placed a marker there! Please try again!".format(player1, player2))
        move_was_invalid = True

    elif player2_marker == "X" and board[position] == "X" and turn == ("{}".format(player2)):
        print("{} you have already placed a marker there! Please try again!".format(player2))
        move_was_invalid = True
    elif player2_marker == "O" and board[position] == "O" and turn == ("{}".format(player2)):
        print("{} you have already placed a marker there! Please try again!".format(player2))
        move_was_invalid = True
    elif player2_marker == "X" and board[position] == "X" and turn == ("{}".format(player1)):
        print("{0}, {1} has already placed a marker there! Please try again!".format(player1, player2))
        move_was_invalid = True
    elif player2_marker == "O" and board[position] == "O" and turn == ("{}".format(player1)):
        print("{0}, {1} has already placed a marker there! Please try again!".format(player1, player2))
        move_was_invalid = True



def check_for_win(board, mark):
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    else:
        return False


def is_space_free(board, position):
    if board[position] == " ":
        return True
    else:
        return False


def is_board_full(board):
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


def player_move():
    global move_was_invalid
    position = int(input("Choose a position to place your marker on the grid:"))
    if position in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        move_was_invalid = False
        return position
    else:
        if turn == ("{}".format(player1)):
            print("{} please enter a valid position!".format(player1))
        elif turn == ("{}".format(player2)):
            print("{} please enter a valid position!".format(player2))
        move_was_invalid = True
        return


# def player_to_go_first (): #requires import module

def player_score(player):
    global player1_score
    global player2_score
    if player == player1:
        player1_score = player1_score + 1
    elif player == player2:
        player2_score = player2_score + 1
    print("{}'s score is".format(player1), player1_score)
    print("{}'s score is".format(player2), player2_score)


def play_again():
    global game_was_played
    game_was_played = True
    again = str(input("{0} and {1} would you like to play again? (Y/N): ".format(player1, player2)))
    if again.lower()[0] == "y":
        game_play()


def game_play():
    global play_game
    global turn
    global player1_marker
    global player2_marker
    if not game_was_played:
        player_names()
    elif game_was_played:
        new_names_needed = str(input(("{0} and {1}? or do the names need to change? (Y/N): ".format(player1, player2))))
        if new_names_needed == "y".lower()[0]:
            player_names()
    start_game()
    create_blank_game_board()
    turn = ("{}".format(player1))

    if play_game:
        player1_marker, player2_marker = player_markers()

    while play_game:
        if turn == ("{}".format(player1)):
            if not move_was_invalid:
                print_game_board(game_board)
            print("It's your turn {}!".format(player1))
            position = player_move()
            if not move_was_invalid:
                place_marker(game_board, player1_marker, position)
            if check_for_win(game_board, player1_marker):
                print_game_board(game_board)
                print("{} has won the game!".format(player1))
                player_score(player1)
                play_game = False
            else:
                if is_board_full(game_board):
                    print_game_board(game_board)
                    print("The game is a draw")
                    play_game = False
                else:
                    if move_was_invalid:
                        turn = ("{}".format(player1))
                    elif not move_was_invalid:
                        turn = ("{}".format(player2))

        if turn == ("{}".format(player2)):
            if not move_was_invalid:
                print_game_board(game_board)
            print("It's your turn {}!".format(player2))
            position = player_move()
            if not move_was_invalid:
                place_marker(game_board, player2_marker, position)
            if check_for_win(game_board, player1_marker):
                print_game_board(game_board)
                print("{} has won the game!".format(player1))
                player_score(player2)
                play_game = False
            else:
                if is_board_full(game_board):
                    print_game_board(game_board)
                    print("The game is a draw")
                    play_game = False
                else:
                    if move_was_invalid:
                        turn = ("{}".format(player2))
                    elif not move_was_invalid:
                        turn = ("{}".format(player1))

    if not play_game:
        play_again()


game_was_played = False
move_was_invalid = False
game_play()
