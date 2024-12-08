MAS_CENTER = 'A'
MAS_EDGES = {'M', 'S'}

class Xmasfinder:
    def find(self, lines):
        matrix = dict()
        for row, line in enumerate(lines):
            for col, value in enumerate(list(line)):
                matrix[(row, col)] = value

        return self.count_xmas(matrix)
    
    def count_xmas(self, matrix):
        total_count = 0
        for coords in matrix.keys():
            row, col = coords
            total_count += self.count_xmas_from_value(matrix, row, col)
        return total_count

    def count_xmas_from_value(self, matrix, row, col):
        if self.is_a_x_mas_cell(matrix, row, col):
            return 1
        return 0
    
    def is_a_x_mas_cell(self, matrix, row, col):
        current_letter = matrix.get((row, col), '-')
        if current_letter != MAS_CENTER:
            return False

        for diagonal_increments in self.get_diagonals():
            if not self.is_a_mas_diagonal(matrix, row, col, diagonal_increments):
                return False
            
        return True
    
    def is_a_mas_diagonal(self, matrix, row, col, diagonal_increments):
        values_in_diagonal = set()
        for increment in diagonal_increments:
            row_inc, col_inc = increment
            next_row, next_col = row+row_inc, col+col_inc
            value = matrix.get((next_row, next_col), '-')
            values_in_diagonal.add(value)
        return values_in_diagonal == MAS_EDGES

    def get_diagonals(self):
        return [[(-1, -1), (+1, +1)], [(+1, -1), (-1, +1)]]