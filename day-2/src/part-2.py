from collections import defaultdict

MIN_OFFSET = 1
MAX_OFFSET = 3

def extract_reports(lines):
    reports = []
    for line in lines:
        str_levels = line.replace("\n", "").split()
        reports.append([int(level) for level in str_levels])
    return reports

def is_report_valid(report_levels, validate_sequence, has_tolerance = True):
    
    for index in range(1, len(report_levels)):
        last_index = index-1

        if validate_sequence(report_levels[index] - report_levels[last_index]):
            continue

        if has_tolerance:
            is_valid_without_last = is_report_valid_without_element(report_levels, index, validate_sequence)
            is_valid_without_current = is_report_valid_without_element(report_levels, last_index, validate_sequence)
            return is_valid_without_last or is_valid_without_current
        
        return False

    return True

def is_report_valid_without_element(report_levels, index, validation_function):
    levels_without_element = report_levels[:index] + report_levels[index+1:]
    return is_report_valid(levels_without_element, validation_function, has_tolerance=False)

def validate_increasing(difference):
    return difference >= MIN_OFFSET  and difference <= MAX_OFFSET

def validate_decreasing(difference):
    return difference <= -MIN_OFFSET and difference >= -MAX_OFFSET

def count_valid_reports(reports):
    count = 0
    for report in reports:
        is_increasing_valid = is_report_valid(report, validate_increasing)
        is_decreasing_valid = is_report_valid(report, validate_decreasing)
        print(report, is_increasing_valid, is_decreasing_valid, " -> ", is_increasing_valid or is_decreasing_valid)
        if is_increasing_valid or is_decreasing_valid:
            count +=1
    return count

if __name__ == "__main__":
    lines = [line for line in open("day-2/res/input.txt", "r")]
    reports = extract_reports(lines)
    result = count_valid_reports(reports)
    print(result)