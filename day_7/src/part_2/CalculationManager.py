import re
import math

class Calculationmanager:
    def calculate(self, lines):
        calculations = self.process_input(lines)
        right_calculation_total = 0
        for calculation in calculations:
            total, parts = calculation
            ways_to_reach_result = self.attempt_to_reach_total(total, parts, current_amount=parts[0], index=1)
            if ways_to_reach_result > 0:
                right_calculation_total += total
        return right_calculation_total

    def attempt_to_reach_total(self, total, parts, current_amount, index):
        if current_amount > total:
            return 0
        if index == len(parts):
            if current_amount == total:
                return 1
            return 0
        
        num_digits = math.floor(math.log10(parts[index])) + 1

        next_sum_amount = current_amount+parts[index]
        next_mul_amount = current_amount*parts[index]
        next_concat_amount = current_amount*(10 ** num_digits) + parts[index]

        result_sum = self.attempt_to_reach_total(total, parts, next_sum_amount, index+1)
        result_mul = self.attempt_to_reach_total(total, parts, next_mul_amount, index+1)
        result_concat = self.attempt_to_reach_total(total, parts, next_concat_amount, index+1)
        return result_sum + result_mul + result_concat
        
    def process_input(self, lines):
        pattern = r"(\d+):\s([\d\s]+)"
    
        result = []
    
        for line in lines:
            match = re.match(pattern, line)
            if match:
                total = int(match.group(1))
                numbers = list(map(int, match.group(2).split()))
                result.append((total, numbers))
        
        return result
