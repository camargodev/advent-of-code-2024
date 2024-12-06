from collections import defaultdict

MIN_OFFSET = 1
MAX_OFFSET = 3

def extract_reports(lines):
    reports = []
    for line in lines:
        str_levels = line.replace("\n", "").split()
        reports.append([int(level) for level in str_levels])
    return reports

def is_report_valid(report_levels, validation_function):
    last = report_levels[0]
    
    for index in range(1, len(report_levels)):
        current = report_levels[index]
        is_valid = validation_function(current-last)
        if not is_valid:
            return False
        last = current
    
    return True

def validate_increasing(difference):
    return difference >= MIN_OFFSET  and difference <= MAX_OFFSET

def validate_decreasing(difference):
    return difference <= -MIN_OFFSET and difference >= -MAX_OFFSET

def count_valid_reports(reports):
    count = 0
    for report in reports:
        is_increasing_valid = is_report_valid(report, validate_increasing)
        is_decreasing_valid = is_report_valid(report, validate_decreasing)
        if is_increasing_valid or is_decreasing_valid:
            count +=1
    return count

if __name__ == "__main__":
    lines = [line for line in open("day-2/res/input.txt", "r")]
    reports = extract_reports(lines)
    result = count_valid_reports(reports)
    print(result)