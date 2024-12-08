from src.part_1.XmasFinder import Xmasfinder as FirstXmasfinder
from src.part_2.XmasFinder import Xmasfinder as SecondXmasfinder

if __name__ == "__main__":
    lines = [line.replace("\n","") for line in open("day_4/res/example.txt", "r")]
    print(FirstXmasfinder().find(lines))
    print(SecondXmasfinder().find(lines))
