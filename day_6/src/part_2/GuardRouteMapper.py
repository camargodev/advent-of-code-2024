from collections import defaultdict

OBSTACLE = "#"
GUARD_START = "^"
UP = (-1, 0)
DOWN = (+1, 0)
LEFT = (0, -1)
RIGHT = (0, +1)

class Guardroutemapper:
    def map(self, lines):
        num_rows, num_cols, map_positions, obstacles, start, direction = self.extract_map_data(lines)
        next_obstacles_by_direction = self.get_next_obstacles(num_rows, num_cols, obstacles)
        guard_in_loop_count = 0
        loop, visited = self.is_guard_stuck_on_loop(map_positions, obstacles, None, start, direction, next_obstacles_by_direction)
        return len(visited)
        for index, additional_obstacle in enumerate(map_positions):
            if additional_obstacle in obstacles or additional_obstacle == start:
                continue
            print(index, additional_obstacle, len(map_positions))
            found_loop = self.is_guard_stuck_on_loop(map_positions, obstacles, additional_obstacle, start, direction, next_obstacles_by_direction)
            if found_loop:
                guard_in_loop_count += 1
        return guard_in_loop_count
    
    def is_guard_stuck_on_loop(self, map_positions, obstacles, additional_obstacle, start, direction, next_obstacles_by_direction):
        visited_movements = set()
        visited_movements.add((start, direction))
        position = start
        while position is not None:
            next_obstacle = next_obstacles_by_direction[direction].get(position, None)
            if next_obstacle is None: 
                return False, set([position for position, _ in visited_movements])
            last_before_obstacle = self.get_previous(position, self.get_opposite(direction))
            if (last_before_obstacle, direction) in visited_movements:
                return True, set([position for position, _ in visited_movements])
            direction = self.rotate(direction)
            position = last_before_obstacle
            visited_movements.add((position, direction))
        visited_cells = set([position for position, _ in visited_movements])
        return False, visited_cells

    def rotate(self, direction):
        if direction == UP:
            return RIGHT
        if direction == RIGHT:
            return DOWN
        if direction == DOWN:
            return LEFT
        return UP
    
    def get_opposite(self, direction):
        if direction == UP:
            return DOWN
        if direction == DOWN:
            return UP
        if direction == RIGHT:
            return LEFT
        return RIGHT

    def get_next(self, position, direction):
        row, col = position
        row_offset, col_offset = direction
        return row+row_offset, col+col_offset
    
    def get_previous(self, position, direction):
        row, col = position
        row_offset, col_offset = direction
        return row-row_offset, col-col_offset
    
    def get_next_obstacles(self, num_rows, num_cols, obstacles):
        next_obstacles_by_direction = dict()
        next_obstacle_left = dict()
        next_obstacle_right = dict()
        next_obstacle_down = dict()
        next_obstacle_up = dict()
        for row in range(num_rows):
            last_obstacle_left = None
            for col in range(num_cols):
                if (row, col) in obstacles:
                    last_obstacle_left = (row, col)
                if last_obstacle_left is not None:
                    next_obstacle_left[(row, col)] = last_obstacle_left
            next_obstacles_by_direction[LEFT] = next_obstacle_left

            last_obstacle_right = None
            for col in range(num_cols, -1, -1):
                if (row, col) in obstacles:
                    last_obstacle_right = (row, col)
                if last_obstacle_right is not None:
                    next_obstacle_right[(row, col)] = last_obstacle_right
            next_obstacles_by_direction[RIGHT] = next_obstacle_right

        for col in range(num_cols):
            last_obstacle_down = None
            for row in range(num_rows, -1, -1):
                if (row, col) in obstacles:
                    last_obstacle_down = (row, col)
                if last_obstacle_down is not None:
                    next_obstacle_down[(row, col)] = last_obstacle_down
            next_obstacles_by_direction[DOWN] = next_obstacle_down

            last_obstacle_up= None
            for row in range(num_rows):
                if (row, col) in obstacles:
                    last_obstacle_up = (row, col)
                if last_obstacle_up is not None:
                    next_obstacle_up[(row, col)] = last_obstacle_up
            next_obstacles_by_direction[UP] = next_obstacle_up

        return next_obstacles_by_direction

    def extract_map_data(self, lines):
        initial_position = None
        map_positions = dict()
        obstacles = set()
        num_rows = len(lines)
        num_cols = len(lines[0])
        for row, line in enumerate(lines):
            for col, value in enumerate(line):
                map_positions[(row, col)] = value
                if value == OBSTACLE:
                    obstacles.add((row, col))
                if value == GUARD_START:
                    initial_position = (row, col)
        return num_rows, num_cols, map_positions, obstacles, initial_position, UP 