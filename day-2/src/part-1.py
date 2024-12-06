from collections import Counter

MIN_OFFSET = 1
MAX_OFFSET = 3

def extract_reports(lines):
    reports = []
    for line in lines:
        str_levels = line.replace("\n", "").split()
        reports.append([int(level) for level in str_levels])
    return reports

def is_report_increasing(report_levels):
    return report_levels[0] < report_levels[-1]

def is_level_pair_valid(last, current, is_increasing):
    if is_increasing and current >= (last+MIN_OFFSET) and current <= (last+MAX_OFFSET):
        return True
    if (not is_increasing) and current <= (last-MIN_OFFSET) and current >= (last-MAX_OFFSET):
        return True
    
    return False

def is_report_valid(report_levels):
    is_increasing = is_report_increasing(report_levels)

    for index in range(1, len(report_levels)):
        last = report_levels[index-1]
        current = report_levels[index]
        if not is_level_pair_valid(last, current, is_increasing):
            return False
    
    return True


def count_valid_reports(reports):
    count = 0
    for report in reports:
        if is_report_valid(report):
            count +=1
    return count

if __name__ == "__main__":
    lines = [line for line in open("day-2/res/input.txt", "r")]
    reports = extract_reports(lines)
    result = count_valid_reports(reports)
    print(result)