import re

MUL_PATTERN =  r"mul\((\d+),(\d+)\)"

class Memorymultiplier:
    def multiply(self, lines):
        total_multiplication_sum = 0
        for line in lines:
            matches = re.findall(MUL_PATTERN, line)
            for match in matches:
                number_1, number_2 = self.extract_match_numbers(match)
                total_multiplication_sum += number_1 * number_2
        return total_multiplication_sum

    def extract_match_numbers(self, match):
        return int(match[0]), int(match[1])