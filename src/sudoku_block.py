# Write your solution here
def block_correct(sudoku: list, row_num: int, col_num: int):
    block = []
    for row in range(row_num, row_num+3):
        for column in range(col_num, col_num+3):
            number = sudoku [row][column]
            if number > 0 and number in block:
                return False
            block.append(number)
    return True

if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
        ]

    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))
