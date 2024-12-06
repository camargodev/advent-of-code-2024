from collections import Counter

def extract_values(lines):
    location_list_1 = []
    location_list_2 = []
    for line in lines:
        value_1, value_2 = line.replace("\n", "").split()
        location_list_1.append(int(value_1))
        location_list_2.append(int(value_2))
    return location_list_1, location_list_2

def calculate_similiarity(location_list_1, location_list_2):
    ocurrence_dict = dict(Counter(location_list_2))

    total_similarity = 0
    for number in location_list_1:
        ocurrences = ocurrence_dict.get(number, 0)
        similarity = number * ocurrences
        total_similarity += similarity
    
    return total_similarity

if __name__ == "__main__":
    lines = [line for line in open("day-1/res/input.txt", "r")]
    location_list_1, location_list_2 = extract_values(lines)
    result = calculate_similiarity(location_list_1, location_list_2)
    print(result)