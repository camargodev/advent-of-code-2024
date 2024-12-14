from collections import defaultdict

NO_NODE = '.'

class Antinodesfinder:
    def find(self, lines):
        size = self.get_sizes(lines)
        nodes_by_type = self.get_nodes_by_type(lines)
        antinodes = self.find_antinodes(nodes_by_type, size)
                
        return len(antinodes)

    def find_antinodes(self, nodes_by_type, size):
        antinodes = set()
        for _, nodes in nodes_by_type.items():
            if len(nodes) == 1:
                continue
            type_antinodes = self.calculate_antinodes_for_node_type(nodes, size)
            antinodes.update(type_antinodes)
            antinodes.update(nodes)
        return antinodes

    def calculate_antinodes_for_node_type(self, nodes, size):
        antinodes = set()
        num_nodes = len(nodes)
        for node1_index in range(num_nodes):
            node1 = nodes[node1_index]
            for node2_index in range(node1_index+1, num_nodes):
                node2 = nodes[node2_index]
                distance = self.get_distance(node1, node2)
                valid_antinodes = self.get_antinodes({node1, node2}, distance, size)
                antinodes.update(valid_antinodes)
        return antinodes

    def get_distance(self, node1, node2):
        (n1_row, n1_col) = node1
        (n2_row, n2_col) = node2

        row_dist = n1_row-n2_row
        col_dist = n1_col-n2_col
        return (row_dist, col_dist)


    def get_antinodes(self, nodes, distance, size):
        (row_dist, col_dist) = distance
        opposite_distance = (-row_dist, -col_dist)
        valid_antinodes = set()
        for node in nodes:
            antinodes_in_line_down = self.get_all_antinodes_in_line(node, nodes, distance, size)
            valid_antinodes.update(antinodes_in_line_down)
            antinodes_in_line_up = self.get_all_antinodes_in_line(node, nodes, opposite_distance, size)
            valid_antinodes.update(antinodes_in_line_up)
        return valid_antinodes
    
    def get_all_antinodes_in_line(self, node, nodes, distance, size):
        antinodes = set()
        (antinode_row, antinode_col) = node
        (row_dist, col_dist) = distance
        is_antinode_valid = True 
        while is_antinode_valid:
            antinode_row, antinode_col = antinode_row+row_dist, antinode_col+col_dist
            antinode = (antinode_row, antinode_col)
            if self.is_antinode_valid(antinode, size):
                if antinode not in nodes:
                    antinodes.add(antinode)
            else:
                is_antinode_valid = False
        return antinodes
    
    def is_antinode_valid(self, antinode, size):
        max_rows, max_cols = size
        antinode_row, antinode_col = antinode
        row_valid = antinode_row >= 0 and antinode_row < max_rows
        col_valid = antinode_col >= 0 and antinode_col < max_cols
        return row_valid and col_valid

    def get_nodes_by_type(self, lines):
        nodes_by_type = defaultdict(list)
        for row, line in enumerate(lines):
            for col, value in enumerate(line):
                if value == NO_NODE:
                    continue
                nodes_by_type[value].append((row, col))
        return nodes_by_type
    
    def get_sizes(self, lines):
        return len(lines), len(lines[0])
