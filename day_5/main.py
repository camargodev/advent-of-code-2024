from src.part_1.MiddlePageFinder import Middlepagefinder as FirstMiddlepagefinder
from src.part_2.MiddlePageFinder import Middlepagefinder as SecondMiddlepagefinder

if __name__ == "__main__":
    lines = [line.replace("\n","") for line in open("day_5/res/input.txt", "r")]
    print(FirstMiddlepagefinder().find_page_and_count(lines))
    print(SecondMiddlepagefinder().find_page_and_count(lines))
