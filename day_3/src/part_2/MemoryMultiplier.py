import re
from collections import defaultdict

MUL_PATTERN =  r"mul\((\d+),(\d+)\)"
DO_PATTERN = r"do\(\)"
DONT_PATTERN = r"don\'t\(\)"

class Memorymultiplier:
    def multiply(self, lines):
        total_multiplication_sum = 0
        should_consider_match = True
        for line in lines:
            match_result_by_index = defaultdict(int)
            
            for match in re.finditer(MUL_PATTERN, line):
                index, number_1, number_2 = self.extract_match_numbers(match)
                match_result_by_index[index] = (number_1*number_2)
            activate_computing_indexes = set([match.start() for match in re.finditer(DO_PATTERN, line)])
            deactivate_computing_indexes = set([match.start() for match in re.finditer(DONT_PATTERN, line)])
            
            for index in range(len(line)):
                if index in activate_computing_indexes:
                    should_consider_match = True
                if index in deactivate_computing_indexes:
                    should_consider_match = False
                    
                match_result = match_result_by_index[index]
                if should_consider_match:
                    total_multiplication_sum += match_result

        return total_multiplication_sum

    def extract_match_numbers(self, match):
        return match.start(), int(match.group(1)), int(match.group(2))
    