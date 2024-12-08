class Xmasfinder:
    def find(self, lines):
        xmas_count = 0
        max_sizes = self.get_max_sizes(lines)
        for row, line in enumerate(lines):
            for col, value in enumerate(list(line)):
                xmas_count += self.count_xmas_from_value(row, col, value, max_sizes)

        return xmas_count
    
    def get_max_sizes(self, lines):
        max_col = len(lines)
        max_row = len(lines[0])
        return max_row, max_col

    def count_xmas_from_value(self, row, col, value, max_sizes):
        print(row, col, value)
        return 0
    
    def get_next_cells(self, row, col, max_sizes):
        nexts = [
            (row-1, col-1), (row-1, col), (row-1, col+1),
            (row, col-1), (row, col+1),
            (row+1, col-1), (row+1, col), (row+1, col+1)
        ]

        valid_nexts = []
        for next in nexts:
            next_row, next_col = next
            if self.can_continue_search(next_row, next_col, max_sizes):
                valid_nexts.append(next)
        
        return valid_nexts
    
    def can_continue_search(self, row, col, max_sizes):
        max_row, max_col = max_sizes
        if row < 0 or row > max_row:
            return False
        if col < 0 or col > max_col:
            return False
        return True
    

    
