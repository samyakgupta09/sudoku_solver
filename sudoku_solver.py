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
    new_board.insert_num(0,0,5)
    new_board.insert_num(0,1,3)
    new_board.insert_num(0,4,7)
    new_board.insert_num(1,0,6)
    new_board.insert_num(1,3,1)
    new_board.insert_num(1,4,9)
    new_board.insert_num(1,5,5)
    new_board.insert_num(2,1,9)
    new_board.insert_num(2,2,8)
    new_board.insert_num(2,7,6)
    new_board.insert_num(3,0,8)
    new_board.insert_num(3,4,6)
    new_board.insert_num(3,8,3)
    new_board.insert_num(4,0,4)
    new_board.insert_num(4,3,8)
    new_board.insert_num(4,5,3)
    new_board.insert_num(4,8,1)
    new_board.insert_num(5,0,7)
    new_board.insert_num(5,4,2)
    new_board.insert_num(5,8,6)
    new_board.insert_num(6,1,6)
    new_board.insert_num(6,6,2)
    new_board.insert_num(6,7,8)
    new_board.insert_num(7,3,4)
    new_board.insert_num(7,4,1)
    new_board.insert_num(7,5,9)
    new_board.insert_num(7,8,5)
    new_board.insert_num(8,4,8)
    new_board.insert_num(8,7,7)
    new_board.insert_num(8,8,9)
    print("unsolved sudoku: ")
    new_board.print_board()

    print("solved sudoku: ")
    if solve_sudoku(new_board):
        new_board.print_board()
    else:
        print("No solution exists.")

main()