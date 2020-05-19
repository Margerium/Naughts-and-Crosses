# Naughts and Crosses


def player_names():
    print("Welcome to this game of Naughts and Crosses")

    player1 = ""
    while player1 == "":
        try:
            player1 = str(input("Please enter your name player one "))
        except ValueError:
            print("Please enter your name player one")
    player1 = player1.upper()[0] + player1.lower()[1:]
    print("Welcome to the game {}!".format(player1))

    player2 = ""
    while player2 == "":
        try:
            player2 = str(input("Please enter your name player two "))
        except ValueError:
            print("Please enter your name player two")

    player2 = player2.upper()[0] + player2.lower()[1:]
    print("Welcome to the game {}!".format(player2))

    first_time = str(input(
        "{0} and {1} have you both played Naughts and Crosses before? (Y/N) (Please enter N if this is "
        "the first time you are running this program): ".format(player1, player2)))

    while not first_time or first_time[0].upper() != "Y" and first_time[0].upper() != "N":
        print("Please enter Y (Yes) or N (No)")
        first_time = str(input(
            "{0} and {1} have you both played Naughts and Crosses before? (Y/N) (Please enter N if this is "
            "the first time you are running this program): ".format(player1, player2)))

    if first_time[0].upper() == "N":
        first_time_playing_naughts_and_crosses()

    names = [player1, player2]
    return names


def start_game(player1, player2, ):
    start_the_game = str(
        input("{0} and {1} are you ready to play Naughts and Crosses? (Y/N): ".format(player1, player2)))

    while not start_the_game or start_the_game[0].upper() != "Y" and start_the_game[0].upper() != "N":
        print("Please enter Y (Yes) or N (No)")
        start_the_game = str(
            input("{0} and {1} are you ready to play Naughts and Crosses? (Y/N): ".format(player1, player2)))

    if start_the_game.lower()[0] == "y":
        return True

    else:
        are_you_sure = str(input("Are you sure you want to exit the game? (Y/N): "))

        while not are_you_sure or are_you_sure[0].upper() != "Y" and are_you_sure[0].upper() != "N":
            print("Please enter Y (Yes) or N (No)")
            are_you_sure = str(input("Are you sure you want to exit the game? (Y/N): "))

        if are_you_sure.lower()[0] == "y":
            exit()

        else:
            print("Ok, then lets start the game!")
            return True


def create_blank_game_board():
    board = [" "] * 10
    return board


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


def player_markers(player1, player2):
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
            print("Please enter a valid input")


def place_marker(board, player1_marker, player2_marker, player1, player2, turn):
    position = 0

    while not position or not isinstance(position, int) or position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        try:
            position = player_move(player1, player2, turn)
        except ValueError:
            print("Please enter a valid integer between 1 and 9")
        except TypeError:
            print("Please enter a valid integer between 1 and 9")
        else:
            print("Please enter a valid integer between 1 and 9")

    if is_space_free(board, position):

        if turn == ("{}".format(player1)):
            board[position] = player1_marker

        elif turn == ("{}".format(player2)):
            board[position] = player2_marker

    else:
        if player1_marker == "X" and board[position] == "X" and turn == ("{}".format(player1)):
            print("{} you have already placed a marker there! Please try again!".format(player1))
            place_marker(board, player1_marker, player2_marker, player1, player2, turn)

        elif player1_marker == "O" and board[position] == "O" and turn == ("{}".format(player1)):
            print("{} you have already placed a marker there! Please try again!".format(player1))
            place_marker(board, player1_marker, player2_marker, player1, player2, turn)

        elif player1_marker == "X" and board[position] == "X" and turn == ("{}".format(player2)):
            print("{1}, {0} has already placed a marker there! Please try again!".format(player1, player2))
            place_marker(board, player1_marker, player2_marker, player1, player2, turn)

        elif player1_marker == "O" and board[position] == "O" and turn == ("{}".format(player2)):
            print("{1}, {0} has already placed a marker there! Please try again!".format(player1, player2))
            place_marker(board, player1_marker, player2_marker, player1, player2, turn)

        elif player2_marker == "X" and board[position] == "X" and turn == ("{}".format(player2)):
            print("{} you have already placed a marker there! Please try again!".format(player2))
            place_marker(board, player1_marker, player2_marker, player1, player2, turn)

        elif player2_marker == "O" and board[position] == "O" and turn == ("{}".format(player2)):
            print("{} you have already placed a marker there! Please try again!".format(player2))
            place_marker(board, player1_marker, player2_marker, player1, player2, turn)

        elif player2_marker == "X" and board[position] == "X" and turn == ("{}".format(player1)):
            print("{0}, {1} has already placed a marker there! Please try again!".format(player1, player2))
            place_marker(board, player1_marker, player2_marker, player1, player2, turn)

        elif player2_marker == "O" and board[position] == "O" and turn == ("{}".format(player1)):
            print("{0}, {1} has already placed a marker there! Please try again!".format(player1, player2))
            place_marker(board, player1_marker, player2_marker, player1, player2, turn)


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


def player_move(player1, player2, turn):
    if turn == ("{}".format(player1)):
        position = int(input("\n{0} choose a position to place your marker on the grid:".format(player1)))
        return position

    elif turn == ("{}".format(player2)):
        position = int(input("\n{0} choose a position to place your marker on the grid:".format(player2)))
        return position


"""  # Redundant Function

def player_score(player1, player2):
    if player == player1:
        player1_score = player1_score + 1
    elif player == player2:
        player2_score = player2_score + 1
    print("{}'s score is".format(player1), player1_score)
    print("{}'s score is".format(player2), player2_score)
    
"""


def play_again(game_was_played, player1, player2, player1_score, player2_score):
    again = str(input("{0} and {1} would you like to play again? (Y/N): ".format(player1, player2)))

    while not again or again[0].upper() != "Y" and again[0].upper() != "N":
        print("Please enter Y (Yes) or N (No)")
        again = str(input("{0} and {1} would you like to play again? (Y/N): ".format(player1, player2)))

    if again[0].upper() == "Y":
        game_play(game_was_played, player1, player2, player1_score, player2_score)

    else:
        exit(0)


def game_play(game_was_played, player1, player2, player1_score, player2_score):
    if not game_was_played:
        names = player_names()
        player1 = names[0]
        player2 = names[1]
        player1_score = 0
        player2_score = 0

    elif game_was_played:
        new_names = str(input(("{0} and {1} is that you? (Y/N): ".format(player1, player2))))

        while not new_names or new_names[0].upper() != "Y" and new_names[0].upper() \
                != "N":
            print("Please enter Y (Yes) or N (No)")
            new_names = str(input(("{0} and {1} is that you? (Y/N): ".format(player1, player2))))

        if new_names[0].upper() == "N":
            names = player_names()
            player1 = names[0]
            player2 = names[1]
            player1_score = 0
            player2_score = 0

    start_game(player1, player2)
    game_board = create_blank_game_board()
    turn = ("{}".format(player1))
    player1_marker = ""
    player2_marker = ""

    if start_game:
        markers = player_markers(player1, player2)
        player1_marker = markers[0]
        player2_marker = markers[1]

    while start_game:
        if turn == ("{}".format(player1)):
            print_game_board(game_board)
            print("It's your turn {}!".format(player1))
            place_marker(game_board, player1_marker, player2_marker, player1, player2, turn)
            if check_for_win(game_board, player1_marker):
                print_game_board(game_board)
                print("{} has won the game!".format(player1))
                player1_score = player1_score + 1
                break
            else:
                if is_board_full(game_board):
                    print_game_board(game_board)
                    print("The game is a draw")
                    break
                else:
                    turn = ("{}".format(player2))

        if turn == ("{}".format(player2)):
            print_game_board(game_board)
            print("It's your turn {}!".format(player2))
            place_marker(game_board, player1_marker, player2_marker, player1, player2, turn)
            if check_for_win(game_board, player2_marker):
                print_game_board(game_board)
                print("{} has won the game!".format(player2))
                player2_score = player2_score + 1
                break
            else:
                if is_board_full(game_board):
                    print_game_board(game_board)
                    print("The game is a draw")
                    break
                else:
                    turn = ("{}".format(player1))

    print("{0} your score is {2} and {1} your score is {3}".format(player1, player2, player1_score, player2_score))

    play_again(True, player1, player2, player1_score, player2_score)


game_play(False, "", "", 0, 0)
