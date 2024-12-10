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
        visited_movements = set()
        visited_movements.add((position, direction))
        while position is not None:
            next = self.get_next(position, direction)
            if next not in map_positions or (next, position) in visited_movements:
                position = None
                continue
            if next in obstacles:
                direction = self.rotate(direction)
                next = self.get_next(position, direction)
            visited_movements.add((next, direction))
            position = next
        visited_cells = set([position for position, _ in visited_movements])
        return len(visited_cells)

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