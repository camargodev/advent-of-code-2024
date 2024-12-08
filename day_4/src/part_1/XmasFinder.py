START = 'X'
END = 'S'

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
            total_count += self.count_xmas_from_value(matrix, row, col, letter_to_find=START, increments=self.get_all_increments())
        return total_count

    def count_xmas_from_value(self, matrix, row, col, letter_to_find, increments):
        current_letter = matrix.get((row, col), '-')
        if current_letter != letter_to_find:
            return 0
        if current_letter == letter_to_find and letter_to_find == END:
            return 1
        
        count_from_cell = 0
        for increment in increments:
            row_inc, col_inc = increment
            next_row, next_col = row + row_inc, col + col_inc
            next_letter = self.get_next_letter(current_letter)
            count_from_cell += self.count_xmas_from_value(matrix, next_row, next_col, next_letter, [increment])
        return count_from_cell
    
    def get_next_letter(self, letter):
        next_letter_dict = { 'X': 'M', 'M': 'A', 'A': 'S'}
        return next_letter_dict.get(letter, None)
    
    def get_all_increments(self):
        return [(-1, -1), (-1, 0), (-1, +1), (0, -1), (0, +1), (+1, -1), (+1, 0), (+1, +1)]