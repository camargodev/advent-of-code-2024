MIN_OFFSET = 1
MAX_OFFSET = 3

def extract_reports(lines):
    reports = []
    for line in lines:
        str_levels = line.replace("\n", "").split()
        reports.append([int(level) for level in str_levels])
    return reports

def is_report_valid(report_levels):
    differences = []
    for index in range(1, len(report_levels)):
        last = report_levels[index-1]
        current = report_levels[index]
        differences.append(current-last)

    is_valid_increasing_list = all(difference >= MIN_OFFSET  and difference <= MAX_OFFSET  for difference in differences)
    is_valid_decreasing_list = all(difference <= -MIN_OFFSET and difference >= -MAX_OFFSET for difference in differences)
    
    return is_valid_increasing_list or is_valid_decreasing_list


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