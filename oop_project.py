import sys


class Game:
    def __init__(self, board, player1, player2):
        self.board = board
        self.players = [player1, player2]
        self.turn = 0

    def greet_user(self, currplayer):
        print(f"It's your turn, player {currplayer.symbol}")

    def play(self):
        game_over = False

        while not game_over:
            currplayer = self.players[self.turn]
            self.board.print_board()
            self.greet_user(currplayer)
            move = self.board.ask_for_move(currplayer)
            self.board.tiles[move] = currplayer.symbol
            if self.check_win(currplayer.symbol):
                self.game_over(currplayer.symbol)
                game_over = True
            else:
                self.turn = 1 - self.turn

    def check_win(self, player_symbol):
        tiles = self.board.tiles
        lines = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
            [0, 4, 8], [2, 4, 6]             # diagonal
        ]
        return any(all(tiles[pos] == player_symbol for pos in line) for line in lines)

    def game_over(self, player_symbol):
        print(f"It's over! Player {player_symbol} wins!")

class Board:
    def __init__(self):
        self.tiles = list(range(9))

    def print_board(self):
        for row in range(0, 9, 3):
            print('|' + '|'.join(str(self.tiles[pos]) for pos in range(row, row + 3)) + '|')

    def ask_for_move(self, player):
        valid_move = False
        while not valid_move:
            try:
                move = int(input(f"Please enter the number (0-8) where you want to move your {player.symbol}: "))
                if move in range(9) and isinstance(self.tiles[move], int):
                    valid_move = True
                else:
                    print("Invalid move or tile already taken. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        return move

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

class HumanPlayer(Player):
    pass

class ComputerPlayer(Player):
    pass

player1 = HumanPlayer("X")
player2 = HumanPlayer("O")
board = Board()
game = Game(board, player1, player2)
game.play()
