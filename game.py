from board import Board
from player import Player


class TicTacToeGame:

    def start(self):
        print("***********************")
        print("Welcome to the Game")
        print("***********************")

        board= Board()
        player = Player()
        computer = Player(False)

        board.print_board()

        while True:

            while True:

                player_move = player.get_move()
                board.submit_move(player, player_move)
                board.print_board()

                if board.check_is_tie():
                    print("It's tie! Try again")
                    break
                elif board.check_is_game_over(player, player_move):
                    print("You won the game!!")
                    break
                else:
                    computer_move = computer.get_move()
                    board.submit_move(computer, computer_move)
                    board.print_board()

                    if board.check_is_game_over(computer, computer_move):
                        print("Computer won!!")
                        break

            play_again = input("Would you like to play again? Y or N? ").upper()

            if play_again == "N":
                print("Bye bye!!")
                break

            elif play_again == "Y":
                self.start_new_round(board)
            else:
                print("Again!!")
                self.start_new_round(board)

    def start_new_round(self, board):
        print("*********************")
        print("New Round")
        print("*********************")

        board.reset()
        board.print_board()

game = TicTacToeGame()
game.start()