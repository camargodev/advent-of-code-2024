import re
from collections import defaultdict
import math

DEPENDENCY_PATTERN =  r"(\d+)\|(\d+)"
LIST_PATTERN = r"(\d+(?:,\d+)*)"

class Middlepagefinder:
    def find_page_and_count(self, lines):
        dependencies, manual_lists = self.extract_input(lines)
        middle_page_sum = 0
        for manual in manual_lists:
            if self.is_manual_valid(dependencies, manual):
                middle_page = self.extract_middle_page(manual)
                middle_page_sum += middle_page
        return middle_page_sum
    
    def is_manual_valid(self, dependencies, manual):
        for index, page in enumerate(manual):
            for prev_page in manual[:index]:
                if prev_page in dependencies[page]:
                    return False
        return True
    
    def extract_middle_page(self, manual):
        middle_index = math.floor(len(manual)/2)
        return manual[middle_index]
    
    def extract_input(self, lines):
        dependencies = defaultdict(set)
        manual_lists = []
        for line in lines:
            dependency_match = re.fullmatch(DEPENDENCY_PATTERN, line)
            if dependency_match:
                manual, dependency_manual = int(dependency_match.group(1)), int(dependency_match.group(2))
                dependencies[manual].add(dependency_manual)
            list_match = re.fullmatch(LIST_PATTERN, line)
            if list_match:
                number_list = list(map(int, line.split(',')))
                manual_lists.append(number_list)
        return dependencies, manual_lists
