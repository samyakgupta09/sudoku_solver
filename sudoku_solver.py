class board:
    def __init__(self):
        self.board = []
        self.filled_squares = 0

    def init_board(self):
        for i in range(9):
            row = [0] * 9  
            self.board.append(row)

    def print_board(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)

            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(self.board[i][j], end=" ")

                if j == 8:
                    print()

    def insert_unsolved_board(self, lst):
        for i in range(9):
            for j in range(9):
                self.board[i][j] = lst[i][j]

    def insert_num(self, row, col, num):
        self.board[row][col] = num
        self.filled_squares += 1

    def isfilled(self):
        if self.filled_squares == 81:
            return True
        else:
            return False
        
    def is_valid(self, row, col, num):
        for i in range(9):
            if self.board[row][i] == num:
                return False

        for i in range(9):
            if self.board[i][col] == num:
                return False

        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[box_row + i][box_col + j] == num:
                    return False

        return True
    
    def find_empty_location(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return i, j
        return None, None
    
def solve_sudoku(board):
    row, col = board.find_empty_location()

    if row is None and col is None:
        return True

    for num in range(1, 10):
        if board.is_valid(row, col, num):
            board.board[row][col] = num

            if solve_sudoku(board):
                return True

            board.board[row][col] = 0

    return False

def main():
    new_board = board()
    new_board.init_board()
    unsolved_board =  [
    [0, 8, 0, 0, 0, 7, 0, 0, 1],
    [0, 0, 6, 0, 0, 3, 0, 0, 0],
    [0, 9, 0, 6, 1, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 6, 0, 0, 0],
    [0, 0, 9, 4, 8, 0, 0, 0, 3],
    [0, 2, 0, 0, 0, 0, 5, 0, 0],
    [0, 0, 4, 1, 9, 0, 0, 0, 8],
    [0, 0, 0, 0, 7, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 3, 0]]
    new_board.insert_unsolved_board(unsolved_board)
    print("unsolved sudoku: ")
    new_board.print_board()

    print("solved sudoku: ")
    if solve_sudoku(new_board):
        new_board.print_board()
    else:
        print("No solution exists.")

main()