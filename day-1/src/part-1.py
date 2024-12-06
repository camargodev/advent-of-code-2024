
def extract_values(lines):
    location_list_1 = []
    location_list_2 = []
    for line in lines:
        value_1, value_2 = line.replace("\n", "").split()
        location_list_1.append(int(value_1))
        location_list_2.append(int(value_2))
    return location_list_1, location_list_2

def calculate_difference(location_list_1, location_list_2):
    sorted_locations_1 = sorted(location_list_1)
    sorted_locations_2 = sorted(location_list_2)
    
    total_difference = 0
    for index in range(len(location_list_1)):
        location_1 = sorted_locations_1[index]
        location_2 = sorted_locations_2[index]
        difference = abs(location_1 - location_2)
        total_difference += difference
    
    return total_difference

if __name__ == "__main__":
    lines = [line for line in open("day-1/res/input.txt", "r")]
    location_list_1, location_list_2 = extract_values(lines)
    result = calculate_difference(location_list_1, location_list_2)
    print(result)