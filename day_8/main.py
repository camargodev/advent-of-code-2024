from src.part_1.AntinodesFinder import Antinodesfinder as FirstAntinodesfinder
from src.part_2.AntinodesFinder import Antinodesfinder as SecondAntinodesfinder

if __name__ == "__main__":
    lines = [line.replace("\n","") for line in open("day_8/res/input.txt", "r")]
    print(FirstAntinodesfinder().find(lines))
    print(SecondAntinodesfinder().find(lines))
