"""
Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where 
"adjacent" cells are those horizontally or vertically neighboring. The same 
letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, 
exists(board, "ABCB") returns false.
"""


def find_word_in_board(board: list[list], word: str) -> bool:
    rows, columns = len(board), len(board[0])

    def dfs(
        board: list[list], row: int, column: int, word: str, word_index: int
    ) -> bool:
        if word_index == len(word):
            return True

        if (
            row < 0
            or row >= rows
            or column < 0
            or column >= columns
            or board[row][column] != word[word_index]
        ):
            return False

        board[row][column] = "*"
        result = (
            dfs(board, row - 1, column, word, word_index + 1)
            or dfs(board, row + 1, column, word, word_index + 1)
            or dfs(board, row, column - 1, word, word_index + 1)
            or dfs(board, row, column + 1, word, word_index + 1)
        )
        board[row][column] = word[word_index]
        return result

    for row in range(rows):
        for column in range(columns):
            if board[row][column] == word[0]:
                if dfs(board, row, column, word, 0):
                    return True

    return False


if __name__ == "__main__":
    _matrix = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert find_word_in_board(_matrix, "ABCCED") is True
    assert find_word_in_board(_matrix, "SEE") is True
    assert find_word_in_board(_matrix, "ABCB") is False
