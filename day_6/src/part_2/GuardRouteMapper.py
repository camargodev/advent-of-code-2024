from collections import deque


OBSTACLE = "#"
GUARD_START = "^"
UP = (-1, 0)
DOWN = (+1, 0)
LEFT = (0, -1)
RIGHT = (0, +1)

class Guardroutemapper:
    def map(self, lines):
        map_positions, obstacles, position, direction = self.extract_map_data(lines)
        _, movements = self.run_trough_path( map_positions, obstacles, position, direction)
        visited_cells = set([position for position, _ in movements])
        number_of_loops = 0
        for index, cell in enumerate(visited_cells):
            stuck_in_loop, _ = self.run_trough_path( map_positions, obstacles, position, direction, add_obstacle=cell)
            if stuck_in_loop:
                number_of_loops += 1
        return number_of_loops
    
    def run_trough_path(self,  map_positions, obstacles, position, direction, add_obstacle=None):
        visited_movements = set()
        visited_movements.add((position, direction))
        while position is not None:
            next = self.get_next(position, direction)
            if (next, direction) in visited_movements:
                return True, visited_movements
            if next not in map_positions:
                position = None
                continue
            if next in obstacles or next == add_obstacle:
                direction = self.rotate(direction)
                next = self.get_next(position, direction)
            visited_movements.add((next, direction))
            position = next
        return False, visited_movements

    def rotate(self, direction):
        if direction == UP:
            return RIGHT
        if direction == RIGHT:
            return DOWN
        if direction == DOWN:
            return LEFT
        return UP

    def get_next(self, position, direction):
        row, col = position
        row_offset, col_offset = direction
        return row+row_offset, col+col_offset

    def extract_map_data(self, lines):
        initial_position = None
        map_positions = set()
        obstacles = set()
        for row, line in enumerate(lines):
            for col, value in enumerate(line):
                map_positions.add((row, col))
                if value == OBSTACLE:
                    obstacles.add((row, col))
                if value == GUARD_START:
                    initial_position = (row, col)
        return map_positions, obstacles, initial_position, UP 