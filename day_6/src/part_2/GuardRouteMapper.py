from collections import deque


OBSTACLE = "#"
GUARD_START = "^"
UP = (-1, 0)
DOWN = (+1, 0)
LEFT = (0, -1)
RIGHT = (0, +1)

class Guardroutemapper:
    def map(self, lines):
        return 0
        map_positions, obstacles, start, direction = self.extract_map_data(lines)
        guard_in_loop_count = 0
        for index, additional_obstacle in enumerate([(61, 123)]):
            if additional_obstacle in obstacles or additional_obstacle == start:
                continue
            print(index, additional_obstacle, len(map_positions))
            found_loop = self.is_guard_stuck_on_loop(map_positions, obstacles, additional_obstacle, start, direction)
            if found_loop:
                guard_in_loop_count += 1
        return guard_in_loop_count
    
    def is_guard_stuck_on_loop(self, map_positions, obstacles, additional_obstacle, start, direction):
        visited_movements = set()
        visited_movements.add((start, direction))
        position = start
        while position is not None:
            print(position, direction, visited_movements)
            next = self.get_next(position, direction)
            if (next, direction) in visited_movements:
                return True
            if next not in map_positions:
                position = None
                continue
            if next in obstacles or next == additional_obstacle:
                direction = self.rotate(direction)
                next = self.get_next(position, direction)
                print("rotated to", direction, next)
            visited_movements.add((next, direction))
            position = next
        return False

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