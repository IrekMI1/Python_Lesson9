class TicTacToeBoard:

    def __init__(self):
        self.turn = 0
        self.win = None
        self.end_game = False
        self.field = [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-'],
        ]

    def get_field(self):
        return self.field

    def make_move(self, row, col):
        if not self.end_game:
            if self.field[row - 1][col - 1] != '-':
                print(f'Клетка {row}, {col} уже занята!')
            else:
                if self.turn % 2 == 0:
                    self.field[row - 1][col - 1] = 'X'
                else:
                    self.field[row - 1][col - 1] = 'O'
                self.turn += 1
                self.win = self.check_field()
                if self.win is None:
                    print('Продолжаем играть.')
                else:
                    if self.win in ('X', 'O'):
                        print(f'Победил ирок {self.win}')
                    elif self.win == 'D':
                        print('Ничья!')
                    self.end_game = True
        else:
            print('Игра уже завершена!')

    def check_field(self):
        if self.turn == 9:
            return 'D'
        elif self.turn < 9:
            for i in range(3):
                if self.field[i][0] != '-' and all(x == self.field[i][0] for x in self.field[i]):
                    return self.field[i][0]
                elif self.field[0][i] != '-' and all(self.field[y][i] == self.field[0][i] for y in range(3)):
                    return self.field[0][i]
                elif self.field[0][0] != '-' and all(self.field[j][j] == self.field[0][0] for j in range(3)):
                    return self.field[0][0]
                elif self.field[0][2] != '-' and all(self.field[k][2 - k] == self.field[0][2] for k in range(3)):
                    return self.field[0][2]
        else:
            return None


board = TicTacToeBoard()
print(*board.get_field(), sep='\n')
board.make_move(1, 1)
print(*board.get_field(), sep='\n')
board.make_move(1, 1)
board.make_move(1, 2)
print(*board.get_field(), sep='\n')
board.make_move(2, 1)
board.make_move(2, 2)
board.make_move(3, 1)
board.make_move(2, 2)
print(*board.get_field(), sep='\n')
