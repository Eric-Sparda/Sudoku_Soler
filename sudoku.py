puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

def sudoku(puzzle) -> list:
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                for num in range(1,10):
                    if valid(puzzle, row, col, num):
                        puzzle[row][col] = num
                        if sudoku(puzzle):
                            return puzzle
                        else:
                            puzzle[row][col] = 0
                return False
    else:
        return puzzle
def valid(puzzle, row, col, num) -> bool:
    for i in range(9):
        if puzzle[row][i] == num:
            return False
    for i in range(9):
        if puzzle[i][col] == num:
            return False
    subgrid_row = (row // 3) * 3
    subgrid_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if puzzle[subgrid_row + i][subgrid_col + j] == num:
                return False
    else:
        return True


def main():
    print(sudoku(puzzle))


if __name__ == "__main__":
    main()